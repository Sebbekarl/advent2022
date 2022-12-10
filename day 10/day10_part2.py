import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import time

sprite = 1
clock = 1
row = 0
col = 0
screen = []
screen_line = []
draw_coords = []
sprite_pos = []

def updateScreen():
    global col
    global row
    global screen_line
    sprite_pos.append(sprite)
    if abs(sprite-col) <= 1:
        screen_line.append([255,255,255])
        draw_coords.append([col,row])
    else:
        screen_line.append([255 ,255 ,255])
    col += 1
    if clock % 40 == 0:
            screen.append(screen_line)
            screen_line = []
            col = 0
            row += 1


with open("input2.txt") as input:
    for line in input:
        updateScreen()
        clock += 1

        if line.strip() == "noop":
            continue

        updateScreen()
        ins, data = line.split(" ")

        if ins == "addx":
            clock += 1
            sprite += int(data)

#fig, axs = plt.subplots(2, 1)

scanner = []

screen = np.array(screen)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.imshow(screen, interpolation='nearest')
plt.pause(10)
for y in range(6):
    for x in range(40):
        test = ax.scatter(x,-2,color = 'yellow')
        test1 = ax.scatter(sprite_pos[x+(40*y)],-1,color = 'green')
        test2 = ax.scatter(sprite_pos[x+(40*y)]+1,-1,color = 'green')
        test3 = ax.scatter(sprite_pos[x+(40*y)]-1,-1,color = 'green')

        if [x, y] in draw_coords:
            plt.scatter(x,y,color='red')

        plt.pause(0.2)
        test.remove()
        test1.remove()
        test2.remove()
        test3.remove()

plt.show()



