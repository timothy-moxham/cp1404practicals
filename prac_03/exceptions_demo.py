"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a function receives an incorrect data type.
E.g., passing a string or float to the int() function here will raise a ValueError.

2. When will a ZeroDivisionError occur?
When attempting to divide a numerator by a denominator of 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by using an error checking loop to ensure that the denominator is not equal to 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
