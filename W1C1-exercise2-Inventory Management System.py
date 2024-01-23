# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {"shoes": 10, "clothes": 100, "accessories": 5}
# inventory-dictionary, "shoes","clothes","accessories"-item, 10,100,5-quantity of the item

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
    if item in inventory:
        inventory [item]+= quantity
        #inventory [item] = inventory [item] + quantity
        print(f"{quantity} {item} had been added.")
    else:
        inventory[item] = quantity
        print(f"Item {item} is not found. Add with quantity {quantity} {item}(s).")        

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
     # 2. Print each item's name and its quantity.
    for item, quantity in inventory. items():
        print(f"{item},{quantity}")
    #loop for the keys
    #for key(or k)
    

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    if item in inventory:
        inventory [item] = quantity
        print(f"quantity of {item} updated to {inventory[item]}")
    else:
        print(f"{item} is not found.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input ("search for the item:")
            new_quantity = int(input ("The number of item to add:"))
            add_item(item, new_quantity)

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            item = input ("Enter new item name:")
            quantity = int(input ("Enter new quantity:"))
            update_item (item,quantity)

        elif choice == "4":
            print ("Exit from the system")
            break

        else:
            print ("Invaild input, please try again.")

            # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()