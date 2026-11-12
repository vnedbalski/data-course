# "Kot pies kot"   # {'kot': 2, 'pies': 1}
example = "Kot pies kot"


def words_count(text):
    new_text = text.lower().split()
    words = {}
    for word in new_text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

print(words_count(example))

