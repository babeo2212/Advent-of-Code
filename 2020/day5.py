from math import ceil, floor

with open('input_day5.txt', 'r') as f:
    inputs = f.readlines()
    inputs = list(map(lambda x: x.strip('\n'), inputs))

def get_row(stringa):
    lowerbound = 0
    upperbound = 127
    for i in stringa[:8]:
        floor_val = floor((upperbound + lowerbound)/2)
        ceil_val = ceil((upperbound + lowerbound)/2)
        if i == 'F':
            lowerbound = lowerbound
            upperbound = floor_val
        elif i == 'B':
            lowerbound = ceil_val
            upperbound = upperbound
    return upperbound

def get_col(stringa):
    lowerbound = 0
    upperbound = 7
    for i in stringa[7:]:
        floor_val = floor((upperbound + lowerbound)/2)
        ceil_val = ceil((upperbound + lowerbound)/2)
        if i == 'L':
            lowerbound = lowerbound
            upperbound = floor_val
        elif i == 'R':
            lowerbound = ceil_val
            upperbound = upperbound
    return upperbound
ids = []
row_col = []
for id in inputs:
    row = get_row(id)
    col = get_col(id)
    ids.append(row * 8 + col)
    row_col.append((row, col))
print(max(ids))

dict_ids = {key: value for key, value in zip(ids, row_col)}

for i in range(13, 881):
    if i not in dict_ids.keys():
        print(i)
