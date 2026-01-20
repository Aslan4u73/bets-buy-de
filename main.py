import products
import store


def print_menu():
    print("\nStore Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    active_products = store_obj.get_all_products()
    for i, product in enumerate(active_products, start=1):
        print(
            f"{i}. {product.name}, Price: ${product.price:.0f}, "
            f"Quantity: {product.quantity}"
        )
    return active_products


def make_order(store_obj):
    active_products = store_obj.get_all_products()

    print("------")
    for i, product in enumerate(active_products, start=1):
        print(
            f"{i}. {product.name}, Price: ${product.price:.0f}, "
            f"Quantity: {product.quantity}"
        )
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_number = input("Which product # do you want? ").strip()
        if product_number == "":
            break

        amount_text = input("What amount do you want? ").strip()

        try:
            index = int(product_number) - 1
            amount = int(amount_text)

            if index < 0 or index >= len(active_products) or amount <= 0:
                raise ValueError

            shopping_list.append((active_products[index], amount))
            print("Product added to list!")
        except ValueError:
            print("Error adding product!")

    if not shopping_list:
        print("********")
        return

    try:
        total_price = store_obj.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price:.0f}")
    except ValueError:
        print("********")
        print("Error adding product!")


def start(store_obj):
    while True:
        print_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store_obj)

        elif choice == "2":
            print(f"Total of {store_obj.get_total_quantity()} items in store")

        elif choice == "3":
            make_order(store_obj)

        elif choice == "4":
            break

        else:
            print("Invalid choice, please try again.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
