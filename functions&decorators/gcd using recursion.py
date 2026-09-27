def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
a = 12
b = 18
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))
#output:
GCD: 6
LCM: 36
