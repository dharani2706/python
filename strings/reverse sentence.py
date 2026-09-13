sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
result = " ".join(words)
print("Reversed sentence:", result)
#output:
Enter a sentence: please rotate your phone
Reversed sentence: phone your rotate please
