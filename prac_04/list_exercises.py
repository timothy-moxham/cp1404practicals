"""
CP1404/CP5632 Practical
Program to calculate the information of 5 numbers prompted from a user.
"""

numbers = [int(input("Number: ")) for number in range(5)]
print(numbers)

print(f"The first number is {numbers[0]}\n"
      f"The last number is {numbers[-1]}\n"
      f"The smallest number is {min(numbers)}\n"
      f"The largest number is {max(numbers)}\n"
      f"The average of the numbers is {sum(numbers) / len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")
