#!/usr/bin/env python
# coding: utf-8

import re
from pprint import pprint

with open('input_day7.txt', 'r') as f:
    inputs = f.readlines()


inputs = [x.strip('\n') for x in inputs]


inputs[0]


pattern = '(\w*\s\w*\sbag)'

for i in inputs:
    print(re.findall(pattern, i))

re.findall(pattern, inputs[0])[0].strip(' bag')

pattern = '(\w*\s\w*\sbag)|(\d\s\w*\s\w*\sbag)'

def extract_bag_color(x):
    pattern = '(\w*\s\w*\sbag)'
    result = re.findall(pattern, x)
    if result:
        result = [x.strip('bag').strip(' ') for x in result]
        key = result[0]
        value = result[1:]
    return key, value


print(extract_bag_color(inputs[593]))



keys = []
values = []
for item in inputs:
    key, value = extract_bag_color(item)
    keys.append(key)
    values.append(value)

dict_color = {key:value for key, value in zip(keys, values)}

len(dict_color)

count_all = 0
control_recursive = 0
color_ = set()

def count_color(values):
    global count_all, control_recursive, color_
    while control_recursive <= 20:
        color_values = set()
        for key in dict_color.keys():
            for value in values:
                if value in dict_color[key]:
                    color_values.add(key)
                    color_.add(key)
        count_all += len(color_values)
        new_keys = color_values
        control_recursive += 1
        count_color(new_keys)


values = ['shiny gold']
count_color(values)


len(color_)


dict_color['shiny gold']


def extract_bag_color2(x):
    ''' This function is to find patterns in an input then arrange them inside a dictionary'''
    pattern = '(\w*\s\w*\sbag)'
    result = re.findall(pattern, x)
    if result:
        result = [x.replace(' bag','') for x in result]
        key = result[0]
        values = result[1:]
    numbers = []
    for value in values:
        
        pattern2 = '\d+\s' + value
        result = re.search(pattern2, x)
        if result:
            number = int(result.group().partition(' ')[0])
            numbers.append(number)
        else:
            numbers = 1
            break   
    if values == ['no other']:
         dict_bags = {key: numbers}
    else:
        dict_bags = {key:{value:number for value, number in zip(values, numbers)}}
        
    return dict_bags


big_dict = {}
for i in inputs:
    big_dict.update(extract_bag_color2(i))



pprint(big_dict)


tmp_num = 1
list_all = []

i = 0
def count_bags(dict_ = big_dict['shiny gold']):
    global list_all, i, tmp_num
    keys = dict_.keys()   
    for key in keys:
        save_tmp = tmp_num     
        print(key)      
        new_dict = big_dict[key]
        value = dict_[key]
        
        tmp_num *= value
        
        print(value)
        if new_dict == 1:
            list_all.append(tmp_num)
            tmp_num = save_tmp
        else:
            count_bags(dict_ = new_dict)
        
count_bags()
print(i)
