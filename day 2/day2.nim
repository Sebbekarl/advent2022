import std/tables
from std/sequtils import zip
# r p s
# 1 2 3
# L D W
# 0 3 6
let
    games = ["A X","A Y","A Z","B X","B Y","B Z","C X","C Y","C Z"]
    #outcome = [3+1,6+2,0+3,0+1,3+2,6+3,6+1,0+2,3+3]
    outcome = [0+3,3+1,6+2,0+1,3+2,6+3,0+2,3+3,6+1]
    input = open("input.txt")
var 
  lookup = initTable[string,int]()
  sum = 0


for pairs in zip(games, outcome):
  let (games, outcome) = pairs
  lookup[games] = outcome


for line in input.lines:
  sum += lookup[line]

input.close()

echo sum