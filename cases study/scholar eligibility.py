percentage = int(input("enter percentage: "))
income =int(input("enter income: "))
eligible = percentage > 85 or (percentage > 75 and income < 200000)
print("Eligible for scholarship:", eligible)

output:
    
enter percentage: 92
enter income: 150000
Eligible for scholarship: True
