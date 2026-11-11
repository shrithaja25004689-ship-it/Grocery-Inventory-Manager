# Smart Grocery Inventory

inventory = {
    "Rice": 20,
    "Sugar": 5,
    "Milk": 15,
    "Biscuits": 3
}


# 1. Add Stock
def add_stock(name, quantity):

    if quantity <= 0:
        print("Invalid quantity")

    elif name in inventory:
        inventory[name] += quantity
        print("Stock added successfully")

    else:
        inventory[name] = quantity
        print("New product added")


# 2. Update Stock
def update_stock(name, quantity):

    if name not in inventory:
        print("Product not found")

    elif quantity <= 0:
        print("Invalid quantity")

    elif quantity > inventory[name]:
        print("Insufficient stock")

    else:
        inventory[name] -= quantity
        print("Stock updated successfully")


# 3. Low Stock Report
def low_stock_report():

    for name, quantity in inventory.items():

        if quantity <= 5:
            print(name, "has low stock")


# 4. Display Inventory
def display_inventory():

    for name, quantity in inventory.items():
        print(name, ":", quantity)
