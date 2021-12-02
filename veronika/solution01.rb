depths = File.readlines('input01.txt').map{ |number| number.strip.to_i }

increases = depths.select.with_index { |depth, index| depth > depths[index - 1] }.size

puts "Part 1: #{increases}"

sums      = depths.each_cons(3).to_a.map(&:sum)
increases = sums.select.with_index { |sum, index| sum > sums[index - 1] }.size

puts "Part 2: #{increases}"
