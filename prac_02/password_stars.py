MINIMUM_LENGTH = 5

password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print("Error")
    password = input("Password: ")

print(len(password) * "*")
