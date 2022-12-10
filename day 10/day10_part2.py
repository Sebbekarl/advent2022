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

def updateScreen():
    global col
    global row
    global screen_line

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


with open("input.txt") as input:
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

screen = np.array(screen)
plt.imshow(screen, interpolation='nearest')
for x, y in draw_coords:
    plt.scatter(x,y,color='red')
    plt.pause(0.00005)
plt.show()



