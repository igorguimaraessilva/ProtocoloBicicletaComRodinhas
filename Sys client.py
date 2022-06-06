from distutils import command
from msilib.schema import Shortcut
import os
import datetime
from re import S
import tkinter
import sqlite3
from tkinter.constants import FALSE
import xml.etree.ElementTree
import xml.parsers.expat
import xml.sax.saxutils

from tkinter import Frame, StringVar, ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename, askopenfilename


class OpenWindow(tkinter.Toplevel):

    def __init__(self, parent, name=None):
        super().__init__(parent)
        self.title("Localizar Paciente")
        self.parent = parent
        self.accepted = False
        self.nameVar = tkinter.StringVar()
        if name is not None:
            self.nameVar.set(name)

        Frame = tkinter.Frame(self)
        nameLabel = tkinter.Label(Frame, text="Nome", underline=0)
        nameEntry = tkinter.Entry(Frame, textvariable=self.nameVar)
        nameEntry.focus_set()
        okButton = tkinter.Button(Frame, text="Localizar", command=self.ok)
        cancelButton = tkinter.Button(Frame,
                                      text="Cancelar",
                                      command=self.close)
        nameLabel.grid(row=0, column=0, sticky=tkinter.W, pady=3, padx=3)
        nameEntry.grid(row=0,
                       column=1,
                       columnspan=3,
                       sticky=tkinter.EW,
                       pady=3,
                       padx=3)
        okButton.grid(row=2, cloumn=2, sticky=tkinter.EW, pady=3, padx=3)
        cancelButton.grid(row=2, column=3, sticky=tkinter.EW, pady=3, padx=3)
        Frame.grid(row=0, column=0, sticky=tkinter.NSEW)
        Frame.columnconfigure(1, weight=1)
        window = self.winfo_toplevel()
        window.columnconfigure(0, weight=1)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.close)

        self.protocol("WM_DELETE_WINDOW", self.close)
        self.grab_set()
        self.wait_window(self)

    def ok(self, event=None):
        self.name = self.nameVar.get()
        self.accepted = True
        self.close()

    def close(self, event=None):
        self.parent.focus_set()
        self.destroy()


class MainWindow(tkinter.Tk):

    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), "patients.sdb")
        self.db = self.connect(self.filename)

        tkinter.Tk.__init__(self)
        self.wm_title("Cadastro de pacientes")
        self.protocol("WM_DELETE_WINDOW", self.sair)
        self.resizable(tkinter.FALSE, tkinter.FALSE)

        # MenuBar
        menubar = tkinter.Menu(menubar)
        self["menu"] = menubar
        self.option_add('*tearOff', tkinter.FALSE)

        # MenuArchive
        menuArquivo = tkinter.Menu(menubar)
        for label, command, shortcut_text, Shortcut in (
            ("Novo", self.novo, "Ctrl+N",
             "<Control-n>"), ("Abrir", self.abrir, "Ctrl+A", "<Control-a>"),
            ("Salvar", self.salvar, "Ctrl+S",
             "<Control-s>"), ("Excluir", self.remover, "Ctrl+E",
                              "<Control-e>"), (None, None, None, None),
            ("Fechar", self.sair, "Ctrl+Q", "<Control-q>")):
            if label is None:
                menuArquivo.add_separator()
            else:
                menuArquivo.add_command(label=label,
                                        underline=0,
                                        command=command,
                                        accelerator=shortcut_text)
                self.bind(Shortcut, command)
        menubar.add_cascade(label="Arquivo", menu=menuArquivo, underline=0)

        # MenuEdit
        menuEditar = tkinter.Menu(menubar)
        for label, command, Shortcut_text, Shortcut in (("Copiar", self.copiar,
                                                         "Ctrl+C",
                                                         "<Control-C"),
                                                        ("Colar", self.colar,
                                                         "Ctrl+V",
                                                         "<Control-V>")(
                                                             "Recortar",
                                                             self.recortar,
                                                             "Ctrl+X",
                                                             "<Control-X>")):
            menuEditar.add_command(label=label,
                                   underline=0 if label != "Colar" else 1,
                                   command=command,
                                   accelerator=shortcut_text)
            #self.bind(shortcut, command)
        menuEditar.add_separator()
        menuEditar.add_command(label="Importar XML",
                               underline=0,
                               command=self.importar_db)
        menuEditar.add_command(label="Exportar XML",
                               underline=0,
                               command=self.exportar_db)

        menubar.add_cascade(label="Editar", menu=menuEditar, underline=0)

        # MenuHelp
        menuAjuda = tkinter.Menu(menubar)
        menuAjuda.add_command(label="Sobre",
                              underline=0,
                              command=self.sobre,
                              accelerator="Ctrl+H")
        self.bind("<Control-h>", self.sobre)
        menubar.add_cascade(label="Ajuda", menu=menuAjuda, underline=2)

        # MenuMouse
        self.MENUmouse = tkinter.Menu(self, tearoff=0)
        self.MENUmouse.add_command(label="Copiar")
        self.MENUmouse.add_command(label="Colar")
        self.MENUmouse.add_command(label="Recortar")
        self.bind("<Button-3><ButtonRelease-3>", self.show_mouse_menu)

        # Toolbar
        self.mainframe = tkinter.Frame(self)
        self.toolbar = tkinter.Frame(self.mainfreame)
        for image, commad in (("images/filenew.gif",
                               self.novo), ("images/fileopen.gif", self.abrir),
                              ("images/trash.gif", self.remover),
                              ("images/filesave.gif",
                               self.salvar), ("images/exit.gif", self.sair)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.image_keepmem.append(image)
                button = tkinter.Button(self.toolbar,
                                        imagee=image,
                                        command=command)
                button.grid(row=0, column=len(self.images_keepmem) - 2)
            except tkinter.TclError as err:
                print(err)
        self.toolbar.grid(row=0, column=0, columnspan=5, sticky=tkinter.NW)
        self.mainframe.grid(row=0, column=5, cticky=tkinter.EW)

        # Name
        ttk.Label(self.mainframe, text="Nome: ").grid(row=1,
                                                      column=1,
                                                      sticky=tkinter.E)
        self.nome = tkinter.StringVar()
        self.name_entry = ttk.Combobox(self.mainframe,
                                       width=50,
                                       textvariable=self.nome)
        self.name_entry_grid(row=1, column=2, columnspan=9, sticky=tkinter.W)
        self.name_entry['values'] = self.list_pac(self.db)
        self.name_entry.bind('<<ComboboxSelect>>', self.abrir_nome)

        # Sexo
        ttk.Label(self.mainframe, text='Sexo: ').grid(row=2,
                                                      column=1,
                                                      sticky=tkinter.E)
        self.sexo = tkinter.StringVar()
        self.masculino = ttk.Radiobutton(self.mainframe,
                                         text='Masculino',
                                         variable=self.sexo,
                                         value='Masculino')
        self.feminino = ttk.Radiobutton(self.mainframe,
                                        text='Feminino',
                                        variable=self.sexo,
                                        value='Feminino')
        self.masculino.grid(row=2, column=2, sticky=tkinter.W)
        self.feminino.grid(row=2, column=3, sticky=tkinter.W)

        # HealthPlan
        ttk.Label(self.mainframe, text='Plano: ').grid(row=3,
                                                       column=1,
                                                       sticky=tkinter.E)
        self.plano = tkinter.StringVar()
        self.plano_entry = ttk.Combobox(self.mainframe,
                                        textvariable=self.plano)
        self.plano_entry.grid(row=3, column=2, columnspan=3, sticky=tkinter.W)
        self.plano_entry['values'] = self.list_planos(self.db)

        # NumberCard
        ttk.Label(self.mainframe, text='Cartão: ').grid(row=4,
                                                        column=1,
                                                        sticky=tkinter.E)
        self.cartao = tkinter.StringVar()
        ttk.Entry(self.mainframe, width=20,
                  textvariable=self.cartao).grid(row=4,
                                                 column=2,
                                                 columnspan=3,
                                                 sticky=tkinter.W)

        # DateOfBirth
        self.ageframe = tkinter.Frame(self.mainframe)
        self.ageframe.grid(row=5, column=1, columnspan=10, sticky=tkinter.EW)
        ttk.Label(self.ageframe,
                  text='Data de nascimento: ').grid(row=1,
                                                    column=1,
                                                    sticky=tkinter.E)
        self.dia_nasc = tkinter.StringVar()
        self.dia_nasc.set('01')
        self.mes_nasc = tkinter.StringVar()
        self.mes_nasc.set('Janeiro')
        self.ano_nasc = tkinter.StringVar()
        self.ano_nasc.set('1950')
        self.idade = tkinter.StringVar()
        ttk.Entry(self.ageframe, width=4,
                  textvariable=self.dia_nasc).grid(row=1,
                                                   column=1,
                                                   sticky=tkinter.E)
        ttk.Label(self.ageframe, text='/').grid(row=1,
                                                column=3,
                                                sticky=tkinter.EW)
        self.mes = ttk.Combobox(self.ageframe, textvariable=self.mes_nasc)
        self.mes.grid(row=1, column=4, sticky=tkinter.EW)
        ttk.Label(self.ageframe, texte='/').grid(row=1,
                                                 column=5,
                                                 sticky=tkinter.EW)
        ttk.Entry(self.ageframe, width=6,
                  textvariable=self.ano_nasc).grid(row=1,
                                                   column=6,
                                                   sticky=tkinter.W)
        self.mes['values'] = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
                              'Junho', 'Julho', 'Agosto', 'Setembro',
                              'Outubro', 'Novembro', 'Dezembro')
        ttk.Label(self.ageframe, text='Idade: ').grid(row=1,
                                                      column=7,
                                                      sticky=tkinter.E)
        ttk.Label(self.ageframe,
                  textvariable=self.idade).grid(row=1,
                                                column=8,
                                                sticky=tkinter.W)
        ttk.Label(self.ageframe, text='anos').grid(row=1,
                                                   column=9,
                                                   sticky=tkinter.E)
        self.mes.bind('<<ComboboxSelected>>', self.callback)
        self.dia_nasc.trace("w", self.callback)
        self.ano_nasc.trace("w", self.callback)
        self.callback()

        # Address
        ttk.Label(self.mainframe, text='Cidade: ').grid(row=7,
                                                        column=3,
                                                        sticky=tkinter.E)
        self.endereço = tkinter.StringVar()
        ttk.Entry(self.mainframe, width=30,
                  textvariable=self.endereço).grid(row=7,
                                                   cloumn=3,
                                                   sticky=tkinter.W)

        # State
        ttk.Label(self.mainframe, text='Estado: ').grid(grid=7,
                                                        column=3,
                                                        sticky=tkinter.E)
        self.estado = tkinter.StringVar()
        self.estado_Entry = ttk.Combobox(self.mainframe,
                                         width=4,
                                         textvariable=self.estado)
        self.estado_Entry.grid(row=7, column=4, sticky=tkinter.W)
        self.estado_entry['values'] = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE',
                                       'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                                       'MG', 'PA', 'PB', 'PR', 'PI', 'RJ',
                                       'RN', 'RS', 'RO', 'RR', 'SC', 'SP',
                                       'SE', 'TO')

        # CEP
        ttk.Label(self.mainframe, text='CEP: ').grid(row=8,
                                                     column=1,
                                                     sticky=tkinter.E)
        self.cep = tkinter.StringVar()
        ttk.Entry(self.mainframe, width=30,
                  textvariable=self.cep).grid(row=8,
                                              column=2,
                                              sticky=tkinter.W)

        # Phone
        ttk.Label(self.mainframe,
                  textvariable='Telefone: ').grid(row=9,
                                                  column=1,
                                                  stciky=tkinter.E)
        self.telefone = tkinter.StringVar()
        ttk.Entry(self.mainframe, width=20,
                  textvariable=self.telefone).grid(row=9,
                                                   column=2,
                                                   columnspan=3,
                                                   sticky=tkinter.W)

        # CellPhone
        ttk.Label(self.mainframe, text='Celular: ').grid(row=10,
                                                         column=1,
                                                         sticky=tkinter.E)
        self.celular = StringVar()
        ttk.Entry(self.mainframe, width=20,
                  textvariable=self.celular).grid(row=10,
                                                  column=2,
                                                  columnspan=3,
                                                  sticky=tkinter.W)

        # Register
        ttk.Label(self.mainframe, text='Registro: ').grid(row=10,
                                                          column=5,
                                                          sticky=tkinter.E)
        self.registro = tkinter.StringVar()
        self.reg_entry = ttk.Combobox(self.mainframe,
                                      width=5,
                                      textvariable=self.registro)
        self.reg_entry.grid(row=10, column=6, sticky=tkinter.W)
        self.reg_entry['values'] = self.list_id(self.db)
        self.reg_entry.bind('<<ComboboxSelected>>', self.abrir_id)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=3, pady=3)

        for child in self.toolbar.winfo_children():
            child.grid_configure(padx=2, pady=3)

    def __del__(self):
        if self.db is not None:
            self.db.close()

    def connect(self, filename):
        create = not os.path.exists(filename)
        db = sqlite3.connect(filename)
        if create:
            cursor = db.cursor()
            cursor.execute(
                "CREATE TABLE planos("
                "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                "nome TEXT UNIQUE NOT NULL)")
            cursor.execute(
                "CREATE TABLE pacientes ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                "nome TEXT NOT NULL, "
                "sexo TEXT, "
                "cartao TEXT, "
                "dia_nasc TEXT, "
                "mes_nasc TEXT, "
                "ano_nasc TEXT, "
                "endereco TEXT, "
                "cidade TEXT, "
                "estado TEXT, "
                "cep TEXT, "
                "telefone TEXT NOT NULL, "
                "celular TEXT, "
                "plano_id INTEGER NOT NULL, "
                "FOREIGN KEY (plano_id) REFERENCES planos)")
            db.commit()
        return db

    def get_and_set_plano(self, db, plano):
        plano_id = self.get_plano_id(db, plano.upper())
        if plano_id is not None:
            return plano_id
        cursor = db.cursor()
        cursor.execute(" INSERT INTO planos(nome) VALUES(?)",
                       (plano.upper(), ))
        db.commit()
        return self.get_plano_id(db, plano)
