def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
def reverse_number(n):
    def reverse_helper(n, result):
        if n == 0:
            return result
        else:
            return reverse_helper(n // 10, result * 10 + n % 10)
    return reverse_helper(n, 0)
n=int(input("enter a number"))
print("Number:", n)
print("Sum of digits:", sum_of_digits(n))
print("Reversed number:", reverse_number(n))
#output:
enter a number2356
Number: 2356
Sum of digits: 16
Reversed number: 6532
