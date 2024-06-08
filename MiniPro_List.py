# Simple Python Shopping Cart App using LISTS


# Function to display the cart and it takes cart as an argument and prints the items in the list to the console
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your cart:")
        for item in cart:
            print(item)
    total_price = 0

    # Loop through the cart and calculate the total price of the items in the cart and print it to the console with 2 decimal places using f-string formatting literal
    for item in cart:
        print(f"{item['name']} - ${item['price']}")
        total_price += item["price"]
    print(f"Total price: ${total_price:.2f}")


def main():
    cart = []
    while True:
        print("\nShopping Cart App")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            item = {"name": name, "price": price}
            cart.append(item)
        elif choice == "2":
            name = input("Enter item name: ")
            for item in cart:
                if item["name"] == name:
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
