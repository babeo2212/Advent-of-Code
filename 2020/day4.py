# Part 1
import re
import pandas as pd
import numpy as np
with open('D:/Hung/Data Science/Random_thing_that_I_learn_online/AvendofCode/2020/input_day4.txt', 'r') as f:
    inputs = f.readlines()
    
    people = []

    lst = []
    i = 0
    for item in range(0, len(inputs)):
  
        if inputs[item] != '\n':
            inputs[item] = inputs[item].strip('\n')
            lst.append(inputs[item])
        if inputs[item] == '\n' or item == len(inputs)-1:
            people.append(lst)
            lst = []

required_field = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
pattern = 'byr|iyr|eyr|hgt|hcl|ecl|pid|cid'

count_invalid = 0
people_valid = []
# for person in people:
#     # print(person)
#     attr_lst = []
#     for attr in person:
#         attr_lst += re.findall(pattern, attr)
#     # print(attr_lst)
#     if len(attr_lst) == 7:
#         if 'cid' in attr_lst:
#             count_invalid += 1
#     elif len(attr_lst) < 7:
#         count_invalid += 1

for person in people:
    # print(person)
    attr_lst = []
    for attr in person:
        attr_lst += re.findall(pattern, attr)
    # print(attr_lst)
    if len(attr_lst) == 7:
        if 'cid' not in attr_lst:
            people_valid.append(person)
    elif len(attr_lst) == 8:
        people_valid.append(person)


people = []

for person in people_valid:
    temp_lst = []
    for attr in person:
        temp_lst += attr.split(' ')
    people.append(temp_lst)
print(len(people))

df_attr = pd.DataFrame(columns=required_field)

def define_attr(astring):
    pattern_2 = 'byr:\d{4}|iyr:\d{4}|eyr:\d{4}|hgt:\d+(in|cm)|hcl:#[0-9a-f]{6}|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:\d{9}|cid:\d*'
    dict_attr = {}
    for attr in astring:
        result = re.search(pattern_2, attr)
        if result:
            tmp = result.group().partition(':')
            dict_attr[tmp[0]] = [tmp[2]]
    return pd.DataFrame(dict_attr)

for person in people:
    df_attr = pd.concat([df_attr, define_attr(person)], sort=False, ignore_index=True)
print(df_attr.head())
df_attr