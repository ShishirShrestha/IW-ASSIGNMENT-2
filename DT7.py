def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]


print(len(find_longest_word(["shishir", "shrestha", "kavrepalanchok"])))