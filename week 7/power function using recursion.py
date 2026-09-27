def power(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * power(base, exp - 1)
    else:
        return 1 / power(base, -exp)
print("2^5 =", power(2, 5))
print("5^0 =", power(5, 0))
print("2^-3 =", power(2, -3))
#output:
2^5 = 32
5^0 = 1
2^-3 = 0.125
