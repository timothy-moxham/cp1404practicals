MINIMUM_LENGTH = 5


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error")
        password = input("Password: ")
    return password


main()
