username = input("Enter username: ")
age = int(input("Enter age: "))
category = input("Enter Content Category: ")

followers = 6767

print("\nInstagram Profile")
print("=========================")
print("Username: ", username)
print("Age: ", age)
print("Content Category: ", category)
print("Day 1 followers: ", followers)
followersgained = 50
followers += followersgained
print("Day 2 followers: ", followers)
print("Followers gained: ", followersgained)



if age>40 and category == "fun":
    print("You are old what is fun for you??")