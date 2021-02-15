def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [1, 2, 3, 9]
list2 = [3, 2, 4, 12]
print(multiplyList(list1))
print(multiplyList(list2))