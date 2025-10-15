"""
CP1404/CP5632 Practical
Program to count the occurrences of words in a string
Estimate: 25 minutes
Actual: 18 minutes
"""

word_to_occurrence = {}

text = input("Text: ")
words = text.split(" ")
for word in words:
    if word not in word_to_occurrence:
        word_to_occurrence[word] = 1
    else:
        word_to_occurrence[word] += 1

max_length = max(len(word) for word in words)

for word, occurrence in sorted(word_to_occurrence.items()):
    print(f"{word:{max_length}} : {occurrence}")
