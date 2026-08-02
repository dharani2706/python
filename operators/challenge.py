#dharani satya
# challenge program
username = "student"
password = "1879"
user = input("Enter username: ")
pwd = input("Enter password: ")
login_success = (user == username) and (pwd == password)
print("Login Success:", login_success)
# Enter username: student
# Enter password: 1879
# Login Success: True
# Enter username: student
# Enter password: 1234  
# Login Success: False