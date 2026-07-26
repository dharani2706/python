#Y.dharani
#A word is a keyword
import keyword
word = input("Enter a word to check if it is a keyword: ")
if keyword.iskeyword(word):
    print(word, is a python keyword.")
else:
    print(word, is not a python  keyword.")