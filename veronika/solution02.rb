commands = File.readlines('input02.txt')
               .map { |line| line.strip.split(" ") }

coordinates = commands.each_with_object(Hash.new(0)) do |(command, magnitude), coordinates|
  case command
  when "forward"
    coordinates[:x] += magnitude.to_i
  when "down"
    coordinates[:depth] += magnitude.to_i
  when "up"
    coordinates[:depth] -= magnitude.to_i
  end
end
puts "Part 1: #{coordinates.values.reduce(&:*)}"

coordinates = commands.each_with_object(Hash.new(0)) do |(command, magnitude), coordinates|
  case command
  when "forward"
    coordinates[:x] += magnitude.to_i
    coordinates[:depth] += coordinates[:aim] * magnitude.to_i
  when "down"
    coordinates[:aim] += magnitude.to_i
  when "up"
    coordinates[:aim] -= magnitude.to_i
  end
end
puts "Part 2: #{coordinates.values_at(:x, :depth).reduce(&:*)}"