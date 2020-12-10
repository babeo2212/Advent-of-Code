import re
# part 1
# with open('D:/Hung/Data Science/Random_thing_that_I_learn_online/AvendofCode/2020/input_day2.txt', 'r') as f:
#     inputs = f.readlines()
# # print(inputs)
# count = 0
# for code in inputs:
#     code = code.strip('\n').split(' ')
#     range_count = list(map(lambda x: int(x), code[0].split('-')))
#     count_char = code[1][0]
#     string = code[2]
#     if string.count(count_char) in range(range_count[0], range_count[1]+1):
#         count += 1
#     # print(pattern, string)
# print(len(inputs))
# print(count)

# part 2
with open('D:/Hung/Data Science/Random_thing_that_I_learn_online/AvendofCode/2020/input_day2.txt', 'r') as f:
    inputs = f.readlines()
# print(inputs)
count_or = 0
count_and = 0
for code in inputs:
    code = code.strip('\n').split(' ')
    range_count = list(map(lambda x: int(x), code[0].split('-')))
    count_char = code[1][0]
    string = code[2]
    if count_char == string[range_count[0] - 1] or count_char == string[range_count[1] - 1]:
        count_or += 1
    if count_char == string[range_count[0] - 1] and count_char == string[range_count[1] - 1]:
        count_and += 1
print(count_or - count_and)