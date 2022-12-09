import numpy as np

visited = set()
directions = {"R" : np.array([1, 0]), "L" : np.array([-1, 0]), "U" : np.array([0, -1]), "D" : np.array([0, 1])}
tails = [np.array([0, 0]) for i in range(10)] # range(2) for part 1

with open("input.txt") as input:
    for line in input:
        direction, times = line.split(" ")
        for i in range(int(times)):
            tails[0] += directions[direction]
            last_tail = tails[0]

            for tail in tails[1:]:
                if np.linalg.norm(last_tail-tail) >= 2: # check if tail is more the 2 units away
                    if last_tail[0] == tail[0]: # straight line x
                        tail[1] += (last_tail[1]-tail[1])/2

                    elif last_tail[1] == tail[1]: # straight line y
                        tail[0] += (last_tail[0]-tail[0])/2

                    else:
                        # diagonal x
                        if abs(tail[0] - last_tail[0]) == 2:
                            tail[0] += (last_tail[0]-tail[0])/2
                        else:
                            tail[0] = last_tail[0]

                        # diagonal y
                        if abs(tail[1] - last_tail[1]) == 2:
                            tail[1] += (last_tail[1]-tail[1])/2
                        else:
                            tail[1] = last_tail[1]

                last_tail = tail
            visited.add((tails[len(tails)-1][0],tails[len(tails)-1][1]))

print(len(visited))

for i in range(-50, 50):
    temp = ""
    for j in range(-50, 50):
        if (i,j) in visited:
            temp += "# "
        else:
            temp += ". "
    print(temp)



