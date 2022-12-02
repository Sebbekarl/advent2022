import tables

let input = open("input.txt")
var
    lookup = {"A X" : 3+1,"A Y":6+2,"A Z":0+3,"B X":0+1,"B Y":3+2,"B Z":6+3,"C X":6+1,"C Y":0+2,"C Z":3+3}.toTable
    lookup2 = {"A X" : 0+3,"A Y":3+1,"A Z":6+2,"B X":0+1,"B Y":3+2,"B Z":6+3,"C X":0+2,"C Y":3+3,"C Z":6+1}.toTable
    sum = 0
    sum2 = 0

for line in input.lines:
    sum += lookup[line]
    sum2 += lookup2[line]

input.close()

echo sum
echo sum2