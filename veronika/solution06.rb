lanternfish_by_age = File.read('input06.txt').split(',').map(&:to_i).tally

def state_after_day(lanternfish_by_age)
  new_state = Hash.new(0)

  lanternfish_by_age.each do |(age, count)|
    if age == 0
      new_state[8] = count
      new_state[6] += count
    else
      new_state[age - 1] += count
    end
  end

  new_state
end

def run_simulation(lanternfish_by_age, number_of_days:)
  number_of_days.times do
    lanternfish_by_age = state_after_day(lanternfish_by_age)
  end
  lanternfish_by_age
end

age_counts_after_80_days = run_simulation(lanternfish_by_age, number_of_days: 80)

puts "Part 1: #{age_counts_after_80_days.values.sum}"
puts "Part 2: #{run_simulation(age_counts_after_80_days, number_of_days: 256 - 80).values.sum}"