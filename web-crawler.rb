#!/usr/bin/env ruby
require 'open-url'
require 'nokogiri'

html=open 'https://www.vivaolinux.com.br'

puts "LISTA DOS ULTIMOS SCRIPTS"
puts '='*60

doc=Nokogiri::HTML(html)
id=1

doc.css('div#scripts>.media').each do |d|

puts "\n#{id} - "+d.at_css('h3').content
puts "Escrito por: "+d.at_css('em').content
id+=1

end
