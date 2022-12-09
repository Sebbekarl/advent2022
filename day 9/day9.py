import numpy as np


visited = set()

directions = {"R" : np.array([1, 0]), "L" : np.array([-1, 0]), "U" : np.array([0, -1]), "D" : np.array([0, 1])}

head_pos = np.array([0, 0])
tail_pos = np.array([0, 0])

with open("input.txt") as input:
    for line in input:
        direction, times = line.split(" ")
        for i in range(int(times)):
            head_pos += directions[direction]

            if np.linalg.norm(head_pos-tail_pos) >= 2:
                if head_pos[0] == tail_pos[0] or head_pos[1] == tail_pos[1]:
                    tail_pos += directions[direction]

                else:
                    if abs(tail_pos[0] - head_pos[0]) == 2:
                        tail_pos += directions[direction]
                        tail_pos[1] = head_pos[1]
                    else:
                        tail_pos += directions[direction]
                        tail_pos[0] = head_pos[0]

            visited.add((tail_pos[0],tail_pos[1]))

print(len(visited))



