s = input("Enter a string: ")
result = ""
for ch in s:
    if not ch.isspace():
        result += ch
print("String without whitespace:", result)
#output:
Enter a string: python is easy
String without whitespace: pythoniseasy
