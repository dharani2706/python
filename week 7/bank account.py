balance = 1000
def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited:", amount)
    print("Current balance:", balance)
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance = balance - amount
        print("Amount withdrawn:", amount)
        print("Current balance:", balance)
def check_balance():
    print("Current balance:", balance)
while True:
    print("Bank Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
#output:
Bank Menu
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 200000
Amount deposited: 200000.0
Current balance: 201000.0
Bank Menu
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 2
Enter withdrawal amount: 100000
Amount withdrawn: 100000.0
Current balance: 101000.0
Bank Menu
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current balance: 101000.0
Bank Menu
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
Thank you!
