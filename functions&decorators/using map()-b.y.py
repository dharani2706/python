def to_uppercase(word):
    return word.upper()
words = ["python", "java", "c", "programming"]
uppercase_words = list(map(to_uppercase, words))
print("Uppercase words:", uppercase_words)
#output:
Uppercase words: ['PYTHON', 'JAVA', 'C', 'PROGRAMMING']
