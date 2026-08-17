n = int(input("Enter a number: "))
if n < 2:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime number")
    else:
        print("not a prime number")
output:
    Enter a number: 27
not a prime number
