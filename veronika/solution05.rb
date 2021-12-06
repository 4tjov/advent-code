lines = File.readlines('input05.txt', chomp: true)
            .map { |line| line.split(' -> ').map { |points| points.split(',').map(&:to_i) } }


def line_crossings(lines, consider_diagonals: false)
  crossings = {}

  lines.each do |line|
    x1, y1 = line.first
    x2, y2 = line.last

    xs = (x1..x2).to_a.empty? ? (x2..x1).to_a : (x1..x2).to_a
    ys = (y1..y2).to_a.empty? ? (y2..y1).to_a : (y1..y2).to_a

    if x1 == x2
      crossings[x1] ||= Hash.new(0)
      ys.each { |y| crossings[x1][y] += 1 }

    elsif y1 == y2
      xs.each do |x|
        crossings[x] ||= Hash.new(0)
        crossings[x][y1] += 1
      end

    elsif consider_diagonals
      xs.size.times.with_index do |index|
        x = x1 <= x2 ? xs[index] : xs[ys.size - index - 1]

        y = y1 <= y2 ? ys[index] : ys[ys.size - index - 1]

        (crossings[x] ||= Hash.new(0))[y] += 1
      end
    end
  end

  crossings
end

def multiple_crossings(crossings)
  crossings.values.map { |h| h.values }.flatten.select { _1 >= 2 }.size
end

puts "Part 1: #{multiple_crossings(line_crossings(lines))}"
puts "Part 2: #{multiple_crossings(line_crossings(lines, consider_diagonals: true))}"

