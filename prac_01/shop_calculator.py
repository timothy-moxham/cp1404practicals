DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    total_price -= DISCOUNT * total_price

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
