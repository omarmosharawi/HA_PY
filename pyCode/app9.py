# print words with length

words = ['Omar','Mohamed','Ali','Nova','Ahmed']

for i in words:
    print('word:', i, ', word length:', len(i))



# another way
char_words = {i: len(i) for i in words}
print('\n', char_words)
