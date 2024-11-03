import datetime
import json
from datetime import datetime, date


class Product:
    def __init__(self, name, price, quantity, brand, unique_identifier):
        # use built-in function isinstance() that determines whether object
        # is of type or a subclass of type.
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name

        if not isinstance(price, float):
            raise TypeError("price must be a float value")
        self.price = price

        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer value")
        self.quantity = quantity

        if not isinstance(brand, str):
            raise TypeError("brand must be a string")
        self.brand = brand

        if not (isinstance(unique_identifier, str) and unique_identifier.isdigit() and len(unique_identifier) == 13):
            raise TypeError("unique identifier must be a 13-digit numeric string")
        self.unique_identifier = unique_identifier

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity}, brand={self.brand})"

    def to_json(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Quantity": self.quantity,
            "Unique_identifier": self.unique_identifier,
            "Brand": self.brand
        }


class Clothing(Product):
    def __init__(self, name, price, quantity, brand, unique_identifier, size, material):
        super().__init__(name, price, quantity, brand, unique_identifier)

        if not isinstance(size, str):
            raise TypeError("size must be a string value")
        self.size = size

        if not isinstance(material, str):
            raise TypeError("material must be a string value")
        self.material = material

    def __str__(self):
        return (f"Clothing(name={self.name}, price={self.price}, quantity={self.quantity}, "
                f"brand={self.brand}, size={self.size}, material={self.material})")

    def to_json(self):
        cloth_json = super().to_json()
        cloth_json.update({
            "Size": self.size,
            "Material": self.material
        })

        return cloth_json


class Food(Product):
    def __init__(self, name, price, quantity, brand, unique_identifier, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, brand, unique_identifier)

        if not isinstance(expiry_date, date):
            raise TypeError("expiry date must be in regulate date format")
        self.expiry_date = expiry_date

        if not isinstance(gluten_free, bool):
            raise TypeError("gluten free must be a boolean value")
        self.gluten_free = gluten_free

        if not isinstance(suitable_for_vegans, bool):
            raise TypeError("suitable for vegans must be a boolean value")
        self.suitable_for_vegans = suitable_for_vegans

    def __str__(self):
        return (f"Clothing(name={self.name}, price={self.price}, quantity={self.quantity}, "
                f"brand={self.brand}, expiry_date={self.expiry_date}, gluten_free={self.gluten_free}, "
                f"suitable_for_vegan={self.suitable_for_vegans})")

    def to_json(self):
        food_json = super().to_json()
        food_json.update({
            "Expiry date": self.expiry_date,
            "gluten free": self.gluten_free,
            "Suitable for vegans": self.suitable_for_vegans
        })

        return food_json


class Electronic(Product):
    def __init__(self, name, price, quantity, brand, unique_identifier, power, warranty):
        super().__init__(name, price, quantity, brand, unique_identifier)

        if not isinstance(power, float):
            raise TypeError("power must be a float value")
        self.power = power

        if not isinstance(warranty, int):
            raise TypeError("warranty must be a integer value")
        self.warranty = warranty

    def __str__(self):
        return (f"Clothing(name={self.name}, price={self.price}, quantity={self.quantity}, "
                f"brand={self.brand}, power={self.power}, warranty={self.warranty})")

    def to_json(self):
        electronic_json = super().to_json()
        electronic_json.update({
            "Power": self.power,
            "Warranty": self.warranty
        })

        return electronic_json


class ShoppingCart:
    def __init__(self):
        # imply unique identifier to act as key for the dict
        self.shopping_cart = {}

    # use unique identifiers to determinate each product
    def addProduct(self, product):
        ui = product.unique_identifier
        if ui in self.shopping_cart:
            print(f"The product {product.name} is already in the cart.")
        else:
            self.shopping_cart[ui] = product
            print(f"The product {product.name} has been added to the cart.")
            print(f"The cart contains {len(self.shopping_cart)} products.")
            print()

    def show_product(self):

        #  If no such product is present, no removal should take place
        if not self.shopping_cart:
            print("The shopping cart is empty")
            return False
        else:
            # let the user specify exactly what product to remove
            print("available products:")
            for ui, product in self.shopping_cart.items():
                print(f"UID: {ui} | {product}")
                print()
            return True

    def removeProduct(self, unique_identifier):
        if unique_identifier in self.shopping_cart:
            remove_item = self.shopping_cart.pop(unique_identifier)
            print(f"The product {remove_item.name} has been removed from the cart.")
            print()

    def getContent(self):
        print("This is the total of the expenses:")
        price_count = 0
        if not self.shopping_cart:
            print("The shopping cart is empty.")
        else:
            # sort the products value alphabetically by product name
            for item in sorted(self.shopping_cart.values(), key=lambda x: x.name):
                if isinstance(item.price, (int, float)) and isinstance(item.quantity, int):
                    # with product names, quantities, partial sums per product type and total sum .
                    print(f"- {item.name}: {item.quantity} * £{item.price} = £{item.price * item.quantity}")
                    price_count += item.price * item.quantity
                else:
                    print(f"Error: {item.name} has invalid price or quantity types.")
            print(f"Total = £{price_count}")
            print()

    def changeProductQuantity(self, unique_identifier, quantity):
        if unique_identifier in self.shopping_cart:
            product = self.shopping_cart[unique_identifier]
            product.quantity = quantity
            print(f"The quantity of {product.name} has been updated to {quantity}")

    def print_out_to_json(self):
        if not self.shopping_cart:
            print("The shopping cart is empty.")
        else:
            items_list = []
            for product in self.shopping_cart.values():
                product_data = product.to_json()
                items_list.append(product_data)

            json_data = json.dumps(items_list)
            print("Shopping cart items in json format: ")
            print(json_data)


def shoppingActions():
    cart = ShoppingCart()
    print('The program has started.')
    print('Insert your next command (H for help):')

    terminated = False
    while not terminated:
        user_input = input("Type your next command: ").strip().upper()

        # allows the user to add a product to the cart.
        if user_input == 'A':
            print("Adding a new product:")

            product_type = input("Insert its type (Clothing/Food/Electronic): ").strip().title()
            if product_type not in ['Clothing', 'Food', 'Electronic']:
                print("Enter the valid input type (Clothing/Food/Electronic).")
                continue

            name = input("Insert its name: ").strip().title()
            price = float(input("Insert its price (£): ").strip())
            quantity = int(input("Insert its quantity: ").strip())
            brand = input("Insert its brand: ").strip()
            unique_identifier = input("Insert its EAN code (13 digits): ").strip()

            if product_type == 'Clothing':
                size = input("Insert its size: ").strip().upper()
                material = input("Insert its material: ").strip().title()

                product = Clothing(name, price, quantity, brand, unique_identifier, size, material)

            elif product_type == 'Food':
                expiry_date = input("Insert its expiry date (YYYY-MM-DD): ").strip()
                try:
                    expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format, please enter date in YYYY-MM-DD format")
                    print()
                    continue

                gluten_free = input("Is gluten free (True or False): ").strip().title()
                if gluten_free in ['True', 'False']:
                    gluten_free = (gluten_free == 'True')

                suitable_for_vegans = input("Is suitable for vegans (True or False): ").strip().title()
                if suitable_for_vegans in ['True', 'False']:
                    suitable_for_vegans = (suitable_for_vegans == 'True')

                product = Food(name, price, quantity, brand, unique_identifier, expiry_date, gluten_free,
                               suitable_for_vegans)

            elif product_type == 'Electronic':
                power = float(input("Insert its power (Watt): ").strip())
                warranty = int(input("Insert its warranty (months): ").strip())

                product = Electronic(name, price, quantity, brand, unique_identifier, power, warranty)

            else:
                print("Invalid product type, please type again.")
                continue

            cart.addProduct(product)

        # allows the user to remove an existing product from the shopping chart.
        elif user_input == 'R':
            product_exist = cart.show_product()

            # execute the code if shopping cart is not empty
            if product_exist:
                unique_identifier = input("Enter the EAN code of the product to remove: ")
                cart.removeProduct(unique_identifier)

        # prints out a formatted text summary of the cart, with an easy-to-read list
        elif user_input == 'S':
            cart.getContent()

        # the user can directly change the quantity of a product already present in the cart.
        elif user_input == 'Q':
            # let the user specify a product without ambiguity
            product_exist = cart.show_product()

            if product_exist:
                unique_identifier = input("Enter an EAN code of product to change the product: ")
                quantity = int(input("Enter the number of quantity: "))
                cart.changeProductQuantity(unique_identifier, quantity)

        # generates a summary of the cart as a JSON-formatted data dump, printed to the console.
        # This output is an array of JSON representations of each product.
        elif user_input == 'E':
            cart.print_out_to_json()

        # the script terminates (exiting the while loop)
        elif user_input == 'T':
            print('Goodbye.')
            terminated = True

        # a request for help from the user. The commands that the program recognises are printed
        # out to the console
        elif user_input == 'H':
            print("The program supports the following commands:")
            print("  [A] - Add a new product to the cart")
            print("  [R] - Remove a product from the cart")
            print("  [S] - Print a summary of the cart")
            print("  [Q] - Change the quantity of a product")
            print("  [E] - Export a JSON version of the cart")
            print("  [T] - Terminate the program")
            print("  [H] - List the supported commands")

        else:
            print("Invalid input, please re-enter again.")


# main execution
shoppingActions()
