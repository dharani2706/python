def require_login(func):
    def wrapper(is_logged_in, *args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login first.")
    return wrapper
def view_profile():
    print("Welcome to your profile!")
    
print("User 1:")
view_profile(True)
print("\nUser 2:")
view_profile(False)
#output:
User 1:
Welcome to your profile!
User 2:
Access denied. Please login first.
