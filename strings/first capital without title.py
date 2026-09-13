sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""
for word in words:
    result = result + word[0].upper() + word[1:] + " "
print("Title Case:", result.strip())
#output:
Enter a sentence: we play kho kho
Title Case: We Play Kho Kho
