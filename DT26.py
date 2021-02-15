def add_sting(list, str):

    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)

list = [1, 2, 3, 4]
str = 'emp'
print(add_sting(list, str))