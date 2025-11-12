# Reversing a word
word = input("Enter a word: ")
print(word)
rev = ""
for char in word:
    rev = char + rev
    print(rev)
