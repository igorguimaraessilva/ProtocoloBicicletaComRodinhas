import random
import math
import os


def start():
    Q1 = (input("pressione S ou N e digite a resposta respeitada "))
    if Q1 == ("S") or Q1 == ("s"):
        str(data_test())
    elif Q1 == ("N") or Q1 == ("n"):
        print("termanating...")
    else:
        print("invalid input")
        str(start())


def data_test():
    global name1
    global name2
    global ski1
    global str1
    global ski2
    global str2
    name1 = ("player 1")
    name2 = ("palyer 2")
    ski1 = 10
    str1 = 10
    ski2 = 10
    str2 = 10
    ski_mod = 0
    str_mod = 0
    if os.path.exists('D&D A.txt') == True:
        print("Seus dados já estão salvos neste arquivo, deseja processar esses dados?")
        Q2 = (input("pressione S ou N e digite a resposta respeitada"))
        if Q2 == ("S") or Q2 == ("s"):
            print("Carregando...")
            str(load_player_data())
        elif Q2 == ("N") or Q2 == ("n"):
            print("ok Prosseguindo para inserir manualmente os dados do jogador ")
            str(set_player_name())
        else:
            print("Invalided input")
            str(data_test())
    else:
        print("Nenhum dado salvo detectado, procedendo à inserção manual dos dados do jogador ")
        str(set_player_name())


def set_player_name():
    global name1
    global name2
    print("Vamos dar nomes aos nossos personagens")
    print("ok agora dê um nome para o personagem um:")
    name1 = (input("Insira o nome do personagem um:"))
    print("bom agora vamos dar um nome ao segundo personagem ")
    name2 = (input("Insira o nome do personagem dois:"))
    print("")
    print("Agora que ambos os personagens têm nomes, vamos dar-lhes atributos ")
    print("Como fazemos isso é ")
    print("Cada atributo é inicialmente definido para 10")
    print("Então nos rolamos dois dados")
    print("A pontuação nos dados de 12 é dividida por")
    print("A pontuação nos dados de 4 lados e arredondada para baixo.")
    print("Então repetimos o processo para os atibutos de cada personagem")
    str(set_player_1_ski())

# definir o nome do jogador 1 e definir a habilidade


def set_player_1_ski():
    global ski1
    global name1
    Q3 = input(
        (name1)+("pressione r para lançar os dados de 12 e 4 lados para determinar sua 'HABILIDADE' "))
    if Q3 == ("r") or Q3 == ("R"):
        roll12 = random.randint(1, 12)
        roll4 = random.randint(1, 4)
        print("os 12 lados rolados:")
        print(roll12)
        print("e os 4 lados rolados")
        print(roll4)
        print("sua 'HABILIDADE': ")
        ski1 = math.floor(((roll12)/(roll4))+(ski1))
        print(ski1)
        str(set_player_1_str())
    else:
        print("invalid input")
        str(set_player_1_ski())

# definir força do jogador 1


def set_player_1_str():
    global name1
    global str1
    global ski1
    Q4 = input(
        (name1)+("pressione r para lançar os dados de 12 e 4 lados para determinar sua 'FORÇA' "))
    if Q4 == ("r") or Q4 == ("R"):
        roll12 = random.randint(1, 12)
        roll4 = random.randint(1, 4)
        print("Os 12 lados rolados: ")
        print(roll12)
        print("W os 4 lados rolados")
        print(roll4)
        str1 = math.floor(((roll12)/(roll4))+(str1))
        print("Sua FORÇA é: ")
        print(str1)
        print("bom" + str(name1) + "e sua HABILIDADE é " + str(ski1))
    else:
        print("invalid input")
        str(set_player_1_str())

# definir habilidade do jogador2


def set_player_2_ski():
    print("")
    global name2
    global ski2
    print((name2)+("Agora é a sua vez de rolar os dados"))
    Q5 = input("Pressione 'R' para lançar os dados e determinar sua 'SKILL'")
    if Q5 == ("r") or Q5 == ("R"):
        roll12 = random.randint(1, 12)
        roll4 = random.randint(1, 4)
        print("O d12 rolou: ")
        print(roll12)
        print("e o d4 rolou: ")
        print(roll4)
        print("Niceee, essa é sua Skill:")
        ski2 = math.floor(((roll12)/(roll4))+(ski2))
        print(ski2)
        print("Pressione 'R' para descobrir sua FORÇA")
        str(set_player_2_str())
    else:
        print("invalid input")
        str(set_player_2_ski())
# definir força do player2


def set_player_2_str():
    print("")
    global name2
    global ski2
    roll12 = random.randint(1, 12)
    roll4 = random.randint(1, 4)
    Q6 = input("Pressione R para rolar os dados e determinar sua FORÇA")
    if Q6 == ("r") or Q6 == ("R")
