d = { 'val1': 5, 'val2': 4, 'val3': 3, 'val4': 2, 'val5': 1, }
result=1
for key in d:
    result=result * d[key]

print(result)