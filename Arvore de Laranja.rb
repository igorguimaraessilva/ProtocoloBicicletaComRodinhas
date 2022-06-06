puts 'Quntos mentros sua árvore terá inicialmente? '
metros=gets.chomp
$arvore=ArvoreDeLaranja.new metros.to_s
puts
menu

class ArvoreDeLaranja
    def initialize altura
        @altura=altura
        @anos=1
        @numero_de_laranjas=0
        puts 'Altura da é '+@altura+' metros'
    end

    def crescer
        passar_um_ano
        puts 'Um ano se passou, sua árvore tem '+@anos.to_s+' anos'
        puts 'E tem '+@altura.to_s+' metros de altura'
        puts
        menu
    end

    def pegar_laranjas
        puts 'Quantas Laranjas deseja colher?'
        pegar=get.chomp.to_i
        if(pegar>@numero_de_laranjas)
            puts 'A árvore não tem laranjas suficientes'
            puts
            menu
        elsif(pegar<=@numero_de_laranjas)
            @numero_de_laranjas=@numero_de_laranjas-pegar
            puts 'Que laranja deliciosa!'
            puts 'Agora a árvore só tem '+@numero_de_laranja.to_s+' laranjas'
            puts
            menu
        end
    end

    def contar_laranjas
        puts 'A árvore tem atualmente '+@numero_de_laranjas.to_s+' laranjas.'
        puts
        menu
    end

    private

    def passar_um_ano
        @anos=@anos+1
        @numero_de_laranjas=0
        if (@anos>2 and @anos<5)
            @numero_de_laranjas=rand(15)+1
            @altura=@altura.to_i+rand(3)+1
        else
            @numero_de_laranjas=rand(30)+1
        end
        
        if(@anos>10)
            puts 'A árvore com altura de '+@altura.to_s+' metros de altura e '+@anos.to_s+' anos morreu'
            exit
        end
    end
end

def menu
    puts "suas escolhas são:"
    puts ""
    puts '1) Passar um ano'
    puts '2) Contar Laranjas'
    puts '3) Colher laranjas'
    puts '0) Sair do programa'
    puts
    puts 'Escolha uma opção: '
    opcao=gets.chomp.to_i
    while not(0<=opcao and opcao<=3)
        puts 'Escolha umaopcao de 0 a 3: '
        opcao=gets.chomp.to_i
    end

    if opcao==1
        $arvore.crescer
    elsif opcao==2
        $arvore.contar_laranjas
    elsif opcao==3
        $arvore.pegar_laranjas
    elsif opcao==0
        puts 'Você está saindo do programa'
    end
end
