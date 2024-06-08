# shopping cart app using DICTIONARIES

# Predefined items
items = [
    {"name": "Apple", "price": 1.00},
    {"name": "Banana", "price": 0.50},
    {"name": "Orange", "price": 1.50},
    {"name": "Apricot", "price": 3.00},
    {"name": "Grapes", "price": 2.00},
]


# Function to display the cart and it takes cart as an argument and prints the items in the list to the console
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your cart:")
        for item in cart:
            print(f"{item['name']} - ${item['price']}")
    total_price = 0

    # Loop through the cart and calculate the total price of the items in the cart and print it to the console with 2 decimal places using f-string formatting literal
    for item in cart:
        total_price += item["price"]
    print(f"Total price: ${total_price:.2f}")


from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import button_dialog


# User to add predefined items to the cart
def main():
    cart = []
    item_names = [item["name"] for item in items]
    item_completer = WordCompleter(item_names, ignore_case=True)
    while True:
        print("\nShopping Cart App")
        print("1. Add predefined item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = button_dialog(
                title="Select an item",
                text="Choose an item to add to the cart:",
                buttons=[(item["name"], item["name"]) for item in items],
            ).run()
            for item in items:
                if item["name"].lower() == name.lower():
                    cart.append(item)
                    break
            else:
                print("Item not found in predefined items.")
        elif choice == "2":
            name = button_dialog(
                title="Select an item",
                text="Choose an item to remove from the cart:",
                buttons=[(item["name"], item["name"]) for item in cart],
            ).run()
            for item in cart:
                if item["name"].lower() == name.lower():
                    cart.remove(item)
                    break
            else:
                print("Item not found in cart.")
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            display_cart(cart)
            break
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
