storage = []
for i in range(4):
    item = str(input("Enter item to add to storage: "))
    storage.append(item)
print("Initial storage:", storage)
print("Customer requests to see the list of items.")
print("Available items:", storage)
item_to_buy = str(input("Enter item asked by the customer: "))
if item_to_buy in storage:
    index = storage.index(item_to_buy)
    delivered_item = storage.pop(index)
    print(f"Owner delivers '{delivered_item}' to customer.")
else:
print(f"Item '{item_to_buy}' not found in storage.")
print("Updated storage:", storage)
