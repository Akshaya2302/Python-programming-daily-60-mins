price_book = {
    "apple": 0.75,
    "banana": 0.40,
    "orange": 0.60,
    "milk": 2.50
}

shopping_cart = ["apple", "banana", "apple", "orange", "apple", "milk", "banana"]

unique_items = set(shopping_cart)
print(f"Unique items bought: {unique_items}")

total_bill = 0
for item in shopping_cart:
    if item in price_book:
        total_bill += price_book[item]

print(f"Total bill: ${total_bill:.2f}")
