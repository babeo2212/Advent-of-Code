with open('input_day8.txt', 'r') as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs]

accumulate = 0
line = 0
instruction_list = []

def operation(x):
    global accumulate, line, instruction_list
    x = x.split(' ')
    operation = x[0]
    argument = int(x[1])
    if operation == 'acc':
        accumulate += argument
        line += 1
    elif operation == 'jmp':
        line += argument
    elif operation == 'nop':
        line += 1

    if line not in instruction_list:
        instruction_list.append(line)
    else:
        line = 'a'
        print(accumulate)

# while True:
#     operation(inputs[line])

def operation2(x):
    global line, accumulate
    x = x.split(' ')
    operation = x[0]
    argument = int(x[1])
    if operation == 'acc':
        accumulate += argument
        line += 1
    elif operation == 'jmp':
        line += argument
    elif operation == 'nop':
        line += 1
    
accumulate_list = []   

def jmp_nop(inputs=inputs):
    global accumulate_list
    for i in range(0, len(inputs)):
        # inputs[i] = inputs[i].split(' ')
        if inputs[i].split(' ')[0] == 'jmp':
            inputs[i] = 'nop ' + inputs[i].split(' ')[1]
 
            line = 0
            count_loop = 0
            # instruction_list = []
            while count_loop < 1000:
                count_loop += 1
                operation2(inputs[line])
                # instruction_list.append(line)

            accumulate_list.append(accumulate)

            print(f'i: {i}, accumulate: {accumulate}, count_loop: {count_loop}')

jmp_nop()
print(accumulate_list)