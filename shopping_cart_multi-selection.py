# shopping_cart_multi-selection.py
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
            print(f"{item['name']} - ${item['price']} x {item['quantity']}")
    total_price = 0
    for item in cart:
        total_price += item["price"] * item["quantity"]
    print(f"Total price: ${total_price:.2f}")


from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import inquirer


# User to add predefined items to the cart
def main():
    cart = []
    while True:
        print("\nShopping Cart App")
        print("1. Add predefined items to cart")
        print("2. Remove items from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            questions = [
                inquirer.Checkbox(
                    "items",
                    message="Choose items to add to the cart:",
                    choices=[f"{item['name']} - ${item['price']}" for item in items],
                ),
            ]
            selected_items = inquirer.prompt(questions)["items"]
            for selected_item in selected_items:
                for item in items:
                    if f"{item['name']} - ${item['price']}" == selected_item:
                        quantity = int(input(f"Enter quantity for {item['name']}: "))
                        cart.append(
                            {
                                "name": item["name"],
                                "price": item["price"],
                                "quantity": quantity,
                            }
                        )
                        break
        elif choice == "2":
            questions = [
                inquirer.Checkbox(
                    "items",
                    message="Choose items to remove from the cart:",
                    choices=[item["name"] for item in cart],
                ),
            ]
            selected_items = inquirer.prompt(questions)["items"]
            for selected_item in selected_items:
                for item in cart.copy():
                    if item["name"].lower() == selected_item.lower():
                        cart.remove(item)
                        break
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
