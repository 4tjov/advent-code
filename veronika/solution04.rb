input = File.readlines('input04.txt', chomp: true)

drawn_numbers = input.first.split(',').map(&:to_i)
boards        = input[2..-1].reject(&:empty?).each_slice(5).map { |slice| slice.map { |s| s.split.map(&:to_i) } }

score = 0
drawn_numbers.size.times.with_index do |i|
  winning_board = boards.detect do |board|
    board.any? { |row| row.all? { |num| drawn_numbers[0..i].include?(num) } }  ||
        board.transpose.any? { |row| row.all? { |num| drawn_numbers[0..i].include?(num) } }
  end

  if winning_board
    sum_of_unmarked = winning_board.flatten.reject { |num| drawn_numbers[0..i].include?(num) }.sum
    score = sum_of_unmarked * drawn_numbers[i]
    break
  end
end
puts "Winning board score: #{score}"

score = 0
already_won = []

drawn_numbers.size.times.with_index do |i|
  winning_boards, loosing_boards = (boards - already_won).partition do |board|
    board.any? { |row| row.all? { |num| drawn_numbers[0..i].include?(num) } }  ||
        board.transpose.any? { |row| row.all? { |num| drawn_numbers[0..i].include?(num) } }
  end

  if loosing_boards.empty?
    loosing_board   = winning_boards.first
    sum_of_unmarked = loosing_board.flatten.reject { |num| drawn_numbers[0..i].include?(num) }.sum
    score = sum_of_unmarked * drawn_numbers[i]
    break
  end

  already_won += winning_boards
end
puts "Loosing board score: #{score}"
