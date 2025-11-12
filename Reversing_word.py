# Reversing a word without using slicing
word = input("Enter a word: ")
print(word)
rev = ""
for char in word:
    rev = char + rev
    print(rev)
