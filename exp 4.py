def pluralize(noun):
    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'


words = ['cat', 'bus', 'box', 'dog']

for word in words:
    print(word, "→", pluralize(word))
