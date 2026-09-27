def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
for i in range(5):
    n = int(input("Enter a number: "))
    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd")
#output:
 Enter a number: 4
4 is Even
Enter a number: 27
27 is Odd
Enter a number: 29
29 is Odd
Enter a number: 6
6 is Even
Enter a number: 12
12 is Even
