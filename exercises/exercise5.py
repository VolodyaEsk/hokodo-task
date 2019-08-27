from collections import Counter

line = input("Input the string to computes the frequency of the words >> ")

words = [word.strip() for word in line.split(" ")]
word_counter = Counter(words)
for key in sorted(word_counter):
    print(":".join([key, str(word_counter[key])]))

