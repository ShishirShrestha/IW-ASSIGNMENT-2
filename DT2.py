def first_and_last_two(str):
    if len(str)<2:
        return ''

    return str[0:2] + str[-2:]

print(first_and_last_two('Python'))
print(first_and_last_two('Py'))
print(first_and_last_two('w'))
