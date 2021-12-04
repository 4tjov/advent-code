report = File.readlines('input03.txt', chomp: true)
             .map(&:chars)

gamma_rate_bin = report.transpose
                       .map { |l| l.tally.max_by { _2 }.first }
                       .join

gamma_rate   = gamma_rate_bin.to_i(2)
epsilon_rate = ("1" * gamma_rate_bin.length).to_i(2) - gamma_rate

puts "Part 1: #{ gamma_rate * epsilon_rate }"

potential_ratings = { oxygen_generator: report, co2_scrubber: report }

report.first.size.times.with_index do |i|
  not_found_ratings = potential_ratings.keys.select { |key| potential_ratings[key].size > 1 }

  break if not_found_ratings.empty?

  not_found_ratings.each do |rating|
    bit = potential_ratings[rating].map { |a| a[i] }
                                   .tally
                                   .sort_by { _1 }.reverse
                                   .max_by { _2 }
                                   .first

    case rating
    when :oxygen_generator
      potential_ratings[:oxygen_generator] = potential_ratings[:oxygen_generator].reject { |a| a[i] != bit }
    when :co2_scrubber
      potential_ratings[:co2_scrubber]     = potential_ratings[:co2_scrubber].reject { |a| a[i] == bit }
    end
  end
end

puts "Part 2: #{ potential_ratings.values.map { |a| a.flatten.join.to_i(2)}.reduce(&:*) }"