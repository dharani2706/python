#Y.DHARANI
#CHALLENGE PROGRAM
import keyword
def is_valid_identifier(name):
    if keyword.iskeyword(name):
        return false
    if not(name[0].isalpha() or name[0] == '_'):
        return false
    for char in name:
        if not(char.isalnum() or char == '_'):
            return false
    return true
name = input("Enter a name to check if it is a valid identifier: ")
if is_valid_identifier(name):
    print("Valid identifier")
else:
    print("Invalid identifier")