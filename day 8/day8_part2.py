tree_input = []

with open("input.txt") as input:
    for line in input:
        temp = []
        line = line.strip()
        for num in line:
            temp.append(int(num))
        tree_input.append(temp)

result = 0
for i in range(len(tree_input)):
    for j in range(len(tree_input)):
        score = 1

        for updown in [-1, 1]:
            for coord in [0, 1]:
                directions = [0, 0]
                directions[coord] = updown
                curr_i = i + directions[0]
                curr_j = j + directions[1]
                length = 0

                while (0 <= curr_i < len(tree_input) and 0 <= curr_j < len(tree_input)) and tree_input[curr_i][curr_j] < tree_input[i][j]:
                    length += 1
                    curr_i += directions[0]
                    curr_j += directions[1]

                if (0 <= curr_i < len(tree_input) and 0 <= curr_j < len(tree_input)) and tree_input[curr_i][curr_j] >= tree_input[i][j]:
                    length += 1

                score *= length

        result = max(result, score)

print(result)
