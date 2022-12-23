import sympy

monkey_jobs = {}

with open("input.txt") as input:
    for line in input:
        monkey, job = line.strip().split(": ")
        monkey_jobs[monkey] = job
finalM1, _, finalM2 = monkey_jobs["root"].split(" ")


def get_result(monkey):
    if monkey_jobs[monkey].find(" ") != -1:
        m1, op, m2 = monkey_jobs[monkey].split(" ")
        #return str(eval(get_result(m1)+op+get_result(m2)))
        m1Num = get_result(m1)
        m2Num = get_result(m2)
        if op == "+":
            return m1Num+m2Num
        elif op == "-":
            return m1Num-m2Num
        elif op == "*":
            return m1Num*m2Num
        elif op == "/":
            return m1Num/m2Num
    else:
        return float(monkey_jobs[monkey])
    
def get_eq(monkey):
    if monkey_jobs[monkey].find(" ") != -1:
        m1, op, m2 = monkey_jobs[monkey].split(" ")
        #return str(eval(get_result(m1)+op+get_result(m2)))
        m1eq = get_eq(m1)
        m2eq = get_eq(m2)
        return "("+m1eq+op+m2eq+")"
    if monkey == "humn":
        return "humn" 
    else:
        return monkey_jobs[monkey]

eq1 = get_eq(finalM1)
eq2 = get_eq(finalM2)
humn = sympy.Symbol("humn")

f1 = lambda humn: eval(eq1)
f2 =lambda humn: eval(eq2)

# for i in range(100000):
#     humn = i
#     #print(get_result(finalM1),get_result(finalM2), monkey_jobs["humn"])
#     if i % 1000 == 0: print(i)
#     if float(f1(i)) == float(f2(i)):
#     #if float(eval(eq1)) == float(eval(eq2)):
#         print(i)
#         break
print(sympy.solve(f1(humn)-f2(humn), humn))

print(get_result("root"))

    