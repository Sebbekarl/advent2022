
file = open("input.txt")

sum = 0;
sum_2 = 0;

file.each_line do |line|
    temp = line.split(',')
    i1 = temp[0].split('-').map(&:to_i)
    i2 = temp[1].split('-').map(&:to_i)
    range1 = (i1[0]..i1[1])
    range2 = (i2[0]..i2[1])

    if  (range1.cover?(i2[0]) and range1.cover?(i2[1])) or (range2.cover?(i1[0]) and range2.cover?(i1[1]))
      sum += 1
    end

    if range1.cover?(i2[0]) or range1.cover?(i2[1]) or range2.cover?(i1[0]) or range2.cover?(i1[1])
      sum_2 += 1
    end
end

puts sum
puts sum_2

file.close()
