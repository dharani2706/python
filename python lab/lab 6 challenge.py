#y.dharani
#three levels of nested indentation
for i in range(1, 6):
    if i > 0:
        for j in range(i):
            print("*", end=" ")
        print()