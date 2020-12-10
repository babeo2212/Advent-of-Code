# Part 1
inputs = []
with open('D:/Hung/Data Science/Random_thing_that_I_learn_online/AvendofCode/2020/input_day1.txt', 'r') as f:
    d=0
    for row in f:
        inputs.append(int(row))
        if row != '\n': 
            d+=1    

for i in range(0, len(inputs)):
    for j in range(i, len(inputs)):
        if inputs[i] + inputs[j] == 2020:
            print(inputs[i] * inputs[j])

# Part 2
for i in range(0, len(inputs)):
    for j in range(i, len(inputs)):
        for z in range(j, len(inputs)):
            if inputs[i] + inputs[j] + inputs[z] == 2020:
                print(inputs[i] * inputs[j] * inputs[z])