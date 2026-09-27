def student_info(name,roll_no,branch):
    print("Name:",name)
    print("Roll_no:",roll_no)
    print("Branch:",branch)
print("using positional arguments:")
student_info("devi",27,"CSE")
print("using keyword arguments:")
student_info(branch="CSE",name="devi",roll_no=27)
#output:
using positional arguments:
Name: devi
Roll_no: 27
Branch: CSE
using keyword arguments:
Name: devi
Roll_no: 27
Branch: CSE
