import numpy as np

tree_input = []

with open("input.txt") as input:
    for line in input:
        temp = []
        line = line.strip()
        for num in line:
            temp.append(int(num))
        tree_input.append(temp)

trees = np.array(tree_input)

sum = 0

for i in range(len(trees)):
    for j in range(len(trees[i])):

        if i == 0 or i == (len(trees) - 1) or j == 0 or j == (len(trees[0])-1):
            sum += 1

        elif np.amax(trees[:i, j]) < trees[i, j]:
            sum += 1

        elif np.amax(trees[(i+1):, j]) < trees[i, j]:
            sum += 1

        elif np.amax(trees[i, :j]) < trees[i, j]:
            sum += 1

        elif np.amax(trees[i, (j+1):]) < trees[i, j]:
            sum += 1


print(sum)


