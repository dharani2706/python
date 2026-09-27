def simple_interest(principal,rate,time):
    simple_interest=(principal*time*rate)/100
    return simple_interest
p=float(input("enter amount"))
r=float(input("enter rate"))
t=float(input("enter the years"))
SI=(p*t*r)/100
print("simple_interest:",SI)
#output:
enter amount200000
enter rate1.5
enter the years2
simple_interest: 6000.0
