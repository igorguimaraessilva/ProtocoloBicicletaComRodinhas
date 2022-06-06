#!/usr/bin/ruby
puts "Quantos amigos?"
amigos=gets.chomp
count=1
friends=[]
amigos.to_i.times do
    puts"Digite o nome do "+count.to_s+"° amigo: "
        amigo=gets
        friends=[amigo.to_s]
        friends=friends+friends
        count+=1
end
puts"-------------------------"
friends.sort.each do[i]
    puts "Tenho um(a) amigo(a) chamado(a): "+i.capitalize
end