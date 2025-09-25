for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 100 + 1, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 1 - 1, -1):
    print(i, end=' ')
print()

# c.
number_of_stars = int(input("How many stars? "))

for i in range(number_of_stars):
    print("*", end='')
print()

# d.
for i in range(1, number_of_stars + 1):
    print(f"{"*" * i}")
print()
