s = input("Enter a string: ")
ch = input("Enter character: ")
first = s.find(ch)
last = s.rfind(ch)
print("First occurrence index:", first)
print("Last occurrence index:", last)
#output:

Enter a string: beautiful
Enter character: u
First occurrence index: 3
Last occurrence index: 7
