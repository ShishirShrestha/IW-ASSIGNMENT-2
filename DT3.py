def change_first_occ(str):
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]

    return str
print(change_first_occ('restart'))
