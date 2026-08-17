a=int(input("enter the  first side"));
b=int(input("enter the  second side"));
c=int(input("enter the third side"));
if a==b and b==c and c==a:
    print("equilateral triangle");
elif a==b or b==c or c==a:
    print("isosceles triangle");
elif a+b<=c or b+c<=a or c+a<=b:
    print("not a triangle");
else:
    print("scalene triangle");
output:enter the  first side5
enter the  second side5
enter the third side5
equilateral triangle
