import sys
import products
import store


class TechStore:
    """
       Represents a Best Buy store.

       Encapsulates the functionality related to managing a store in the Best Buy store.
       It provides methods for listing products, checking total quantities, making orders, and more.

       Attributes:
           product_list (list): List of products representing the products available in the store.
    """
    def __init__(self):
        self.product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250)
        ]
        self.best_buy = store.Store(self.product_list)

    def show_list(self):
        """
        Shows the list of products in the store with their price and quantity.
        Updates the quantity when orders are made.
        """
        products_list = self.best_buy.products
        print("______")
        for index, product in enumerate(products_list, start=1):
            print(f"Product #{index}: {product.show()}")
        print("______")

    def total_quantity(self):
        """
        Shows the total quantity available in the store.
        Updates the total quantity when orders are made.
        """
        total_quantity = self.best_buy.get_total_quantity()
        print(f"Total of {int(total_quantity)} items in store")

    def make_order(self):
        """Takes orders until the user enters an empty text."""
        order_list = []

        while True:
            product_num = input("Which product # do you want? ")
            if not product_num:
                break

            try:
                product_num = int(product_num)
                if product_num < 1 or product_num > len(self.best_buy.products):
                    raise ValueError("Invalid product number. Please try again.")
            except ValueError as error:
                print(str(error))
                continue

            quantity = input("What amount do you want? ")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Invalid quantity. Please enter a positive quantity.")
            except ValueError as error:
                print(str(error))
                continue

            product = self.best_buy.products[product_num - 1]
            order_list.append((product, quantity))
            print("Product added to list!")

        try:
            total_price = self.best_buy.order(order_list)
            formatted_price = f"{total_price:.2f}"
            print(f"Order made! Total payment: ${formatted_price}")
        except ValueError as error:
            print(str(error))

    @staticmethod
    def exit_program():
        """Exits the program."""
        sys.exit()

    def start(self):
        """ Displays a menu and allows the user to choose from a list of options."""
        while True:
            print("  Store Menu\n  ------- \n1. List all products in store\n"
                  "2. Show total amount in store\n3. Make an order\n4. Quit")

            functions = {
                1: self.show_list,
                2: self.total_quantity,
                3: self.make_order,
                4: self.exit_program,
            }

            user_choice = int(input("Please choose a number: "))
            if user_choice in functions:
                functions[user_choice]()
                self.start()
            else:
                print("\033[31m" + "Error! Please choose from numbers 1 to 4." + "\033[0m")
                self.start()


if __name__ == "__main__":
    store = TechStore()
    store.start()
