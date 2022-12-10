sum = 1
clock = 1
result = 0

def checkClock():
    global result
    if (clock-20) % 40 == 0:
        result += sum*clock

with open("input2.txt") as input:
    for line in input:
        checkClock()
        clock += 1

        if line.strip() == "noop":
            continue

        checkClock()
        ins, data = line.split(" ")

        if ins == "addx":
            clock += 1
            sum += int(data)

print(result)
