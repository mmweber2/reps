import re
from time import sleep

def word_cloud(text):
    words = dict()
    pos = 0
    while pos < len(text):
        word = ""
        # Other separators may be needed, but we want to be sure that ' is not
        # used. It is unclear whether hyphens count as one word or two.
        separators = (" ", "\n", ";", ":", "?", "!", ".", "\"")
        while pos < len(text) and text[pos] not in separators:
            word += text[pos]
            pos += 1
        pos += 1
        if len(word) < 1:
            continue
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

print word_cloud('After beating the eggs, Dana read the next step:' +
    ' Add milk and eggs, then add flour and sugar.')
print word_cloud("I can't tell what you're asking.")
print word_cloud("You'll need a cheese-cloth for this one. Are you ready?")

