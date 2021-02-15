def adding_words(str):

    if len(str)>2:
        if str[-3:] =='ing':
            str += 'ly'
        else:
            str += 'ing'
    return str
print(adding_words('abc'))
print(adding_words('string'))
