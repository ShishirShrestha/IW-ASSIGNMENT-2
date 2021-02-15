def all_empty(list):
    list1= True
    for i in list:
        if i:
             list1 = False
    return list1
print(all_empty([{},{},{}]))
print(all_empty([{1,2},{},{}]))