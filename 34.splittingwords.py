sentence = "This is a sample sentence without built-in functions"
current_word = ''
words = []

for char in sentence:
    if char == ' ':
        if current_word:
            words.append(current_word)
            current_word = ''
    else:
        current_word += char

# Add the last word if it's not empty
if current_word:
    words.append(current_word)

# Print the split words
for word in words:
    print(word)
