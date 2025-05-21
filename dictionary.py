items = {
    "Apple": {"quantity": 5, "price":1.00 },
    "Book": {"quantity": 3, "price": 0.50},
    "Cloth": {"quantity": 2, "price": 2.00},
    "Fridge":{"quantity":1,
     "price":50.00},
}

for item, details in items.items():
    print(f"Item: {item}")
    print(f"Quantity: {details['quantity']}")
    print(f"Price: ${details['price']:.2f}")
    print(f"Total: ${details['quantity'] * details['price']:.2f}")
    print()
