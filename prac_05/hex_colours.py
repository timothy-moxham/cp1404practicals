"""
CP1404/CP5632 Practical
Program to look up hexadecimal colour codes from colour names
"""

NAME_TO_CODE = {"Brick Red": "#cb4154", "Celtic Blue": "#246bce", "Charcoal": "#36454f", "Chocolate": "#d2691e",
                "Chestnut": "#954535", "Cobalt": "#0047ab", "Daffodil": "#ffff31", "Eggplant": "#614051",
                "Emerald": "#50c878", "Fawn": "#e5aa70"}

colour_name = input("Colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name}'s hexadecimal colour code is {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Colour name: ").title()
