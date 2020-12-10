from math import ceil

# Part 1
with open('D:/Hung/Data Science/Random_thing_that_I_learn_online/AvendofCode/2020/input_day3.txt', 'r') as f:
    inputs = f.readlines()

# inputs = list(map(lambda x: x.strip('\n') * 32, inputs))

# count_tree = 0
# for i in range(1, len(inputs), 1):
#     index = i * 3
#     if inputs[i][index] == '#':
#         count_tree += 1
# print(count_tree)

# Part 2
def count_tree(inputs, right, down=1):

    inputs = list(map(lambda x: x.strip('\n'), inputs))
    col_inputs = len(inputs[0])
    row_inputs = len(inputs)
    inputs = list(map(lambda x: x * (ceil(row_inputs * right / col_inputs) + 1) , inputs))
    
    count_tree = 0
    for i in range(down, len(inputs), down):
        index = int((i * right)/down)
        if inputs[i][index] == '#':
            count_tree += 1
    return(count_tree)

print(count_tree(inputs, 1, 1) * count_tree(inputs, 3, 1)\
    * count_tree(inputs, 5, 1) * count_tree(inputs, 7, 1) * count_tree(inputs, 1, 2))