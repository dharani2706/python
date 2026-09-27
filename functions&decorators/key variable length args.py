def build_profile(**details):
    print("\nPROFILE CARD")
    for key, value in details.items():
        print(key.capitalize(), ":", value)
        print(" ")
# First profile
build_profile(
    name="Rahul",
    age=20,
    city="Hyderabad",
    hobby="Cricket"
)
# Second profile
build_profile(
    name="Anita",
    age=21,
    city="Chennai",
    hobby="Reading",
    course="B.Tech CSE"
)
#output:
PROFILE CARD
Name : Rahul
Age : 20
City : Hyderabad
Hobby : Cricket
PROFILE CARD
Name : Anita
Age : 21
City : Chennai
Hobby : Reading
Course : B.Tech CSE
 
