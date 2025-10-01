"""
CP1404/CP5632 - Practical
Files
"""

# 1
name = input("Name: ")
out_file = open("data.txt", "w")
print(name, file=out_file)
out_file.close()
