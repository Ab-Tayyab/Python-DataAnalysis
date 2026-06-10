import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "files", "inventory_management_system.json")

os.makedirs(os.path.dirname(file_name), exist_ok=True)

def load_file():
    try:
        with open(file_name,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {} 

def save_file():
    with open(file_name,'w') as file:
        json.dump(inventory,file,indent=4)

inventory = load_file()
if not inventory:
    inventory = {
        "fruits":{
            "apple":1,
            "mango":4,
            "banana":3,
        },
        "cloth":{
            "men":1,
            "women":3,
            "kids":1,
        }
    }

out_of_stock_products=set()

# find category 

def get_category():
    category_name = input("Enter category name: ").strip().lower()
    if category_name not in inventory:
        print("Category not found!")
        return None
    return inventory[category_name]


# show inventory 
def show_inventory():
    # all categories
    choice = input("Enter choice: 1 for show whole inventory, 2 for specific category: ").strip()
    if choice =="1": 
        print("\nInventory")
        for category,products in inventory.items():
            print(f"{category}")
            for product,quantity in products.items():
                print(f"{product}: {quantity}")
    elif choice == "2":
        category = get_category()
        if category:
            print(f"Product: Quantity")
            for product,quantity in category.items():
                print(f"{product}: {quantity}")

    else:
        print("Invalid choice!")



# add category and product 

def add_inventory():
    category_name = input("Enter category name: ").strip().lower()
    product_name = input("Enter product name: ").strip().lower()
    try:
        product_quantity = int(input("Enter product quantity in numbers: "))
    except ValueError:
        print("Value must be integer")
        return
    
    if product_quantity<0 or product_quantity==0:
        print("Product quantity should be greater 0!")


    if category_name not in inventory:
        inventory[category_name]={}
        print("New category created successfully!")

    inventory[category_name][product_name] = product_quantity

    if product_name in out_of_stock_products:
        out_of_stock_products.remove(product_name)

    print("Product added successfully!")


# purchase product 

def purchase_product():
    product_name = input(
        "Enter product name: "
    ).strip().lower()

    for category, products in inventory.items():

        if product_name in products:

            products[product_name] -= 1

            print("Product purchased successfully!")

            if products[product_name] == 0:

                out_of_stock_products.add(product_name)

                del products[product_name]

                print(
                    f"{product_name} is now out of stock and removed."
                )

                if not products:
                    empty_category = category

                    del inventory[empty_category]

                    print(
                        f"Category '{empty_category}' removed because it became empty."
                    )

            return

    print("Product not found!")




# show out of stock product 

def show_outOfStock_product():
    if not out_of_stock_products:
        print("No Product is out of stock")
        return
    print("Out of stock products")
    for index,product in enumerate(
        sorted(out_of_stock_products),
        start=1):
        print(f"{index}. {product}")
        

#Menu
def menu():
        print("""
===========================
Inventory Management System
===========================
1. Show Inventory
2. Add Inventory
3. Purchase Product             
4. Show outOfStock Product              
0. Exit
===========================
""")
        
while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid value!")
        continue
    match choice:
        case 1:
            show_inventory()
        case 2:
            add_inventory()
        case 3:
            purchase_product()

        case 4:
            show_outOfStock_product()
        case 0:
            save_file()
            print("👋 Good Bye!")
            break
        case _:
            print("Invalid choice")

