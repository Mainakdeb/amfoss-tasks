require "open-uri"

doc_final = open('#paste link here')



html = doc_final.read

identifier = "<div class=\"BNeawe vvjwJb AP7Wnd\">"

indexes = (0..html.length).find_all{ |char| html[char, identifier.length] == identifier}

found_indexes = []

current_index = 0

while current_index != nil

current_index = html[(current_index + 1)..-1].index(identifier)


if current_index != nil

current_index = current_index + 1

if found_indexes.any?

current_index = found_indexes.last + current_index

end

found_indexes << current_index

end

end

# get a nil

#headline_start = index + identifier.length

headlines = found_indexes.map do |index|
 # star

headline_start = index + identifier.length

headline_end = html[headline_start..-1].index("</div>") - 1

html[headline_start..(headline_start + headline_end)]

end
######################

headlines.each do |headline|
#star thing
puts headline
puts "************"
end

































