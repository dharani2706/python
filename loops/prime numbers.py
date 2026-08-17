start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print("Prime numbers are:")
for n in range(start, end + 1):
    if n >= 2:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n, end=" ")
output:
    Enter starting number: 2
Enter ending number: 73
Prime numbers are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 
