puts ""
puts "Tabuada basica de multiplicação"
puts ""
puts "Informe o valor?"
valor=gets.to_i
puts "Resultado da tabuada do #{valor}"
    sleep 1
    valores=1..10.to_i
puts ""
valores.each do |y|
    resultado=valor*y
    puts"#{valor}x#{y}=#{resultado}"
end
sleep 5
puts ""
puts "Gostaria de fazer uma nova conta?[sn]"
resp=gets.chomp
if resp=="s" then
    puts "Informe o valor?"
    valor=gets.to_i
    puts "Resultado da tabuada do #{valor}"
    sleep 1
    valores=1..10.to_i
puts ""
valores.each do |y|
    resultado=valor*y
    puts"#{valor}x#{y}=#{resultado}"
end

else
    puts ""
    puts "Saindo do script"
exit
end
}