s = input("Enter a string: ")
ch = input("Enter character to count: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Occurrences:", count)
#output:
Enter a string: dharani
Enter character to count: r
Occurrences: 1
