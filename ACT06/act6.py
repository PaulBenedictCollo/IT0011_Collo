class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "ID: " + self.item_id + ", Name: " + self.name + ", Description: " + self.description + ", Price: $" + format(self.price, ".2f")


class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self):
        try:
            item_id = input("Enter item ID: ")
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            
            name = input("Enter item name: ")
            description = input("Enter item Description: ")
            price = float(input("Enter item Price: "))
            if price < 0:
                raise ValueError("No negative prices.")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully.")
        except ValueError as e:
            print("Error: " + str(e))

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item.__str__())

    def update_item(self):
        try:
            item_id = input("Enter item ID to update: ")
            if item_id not in self.items:
                raise ValueError("Item ID not found.")

            name = input("Enter new name: ")
            description = input("Enter new description: ")
            price = float(input("Enter new price: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item updated successfully.")
        except ValueError as e:
            print("Error: " + str(e))

    def delete_item(self):
        try:
            item_id = input("Enter item ID to delete: ")
            if item_id not in self.items:
                raise ValueError("Item ID not found.")
            
            del self.items[item_id]
            print("Item deleted successfully.")
        except ValueError as e:
            print("Error: " + str(e))


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_item()
        elif choice == "2":
            manager.view_items()
        elif choice == "3":
            manager.update_item()
        elif choice == "4":
            manager.delete_item()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
