"""
Smart Grocery Store Management System
-------------------------------------
A simple console application that manages products, stock and sales
for a local grocery store.

Main data structures:
    products -> list of dictionaries (id, name, category, price, stock)
    sales    -> list of dictionaries (product_id, product_name,
                                      quantity_sold, total_amount)
"""

import math

# ----------------------------------------------------------------------
# Data storage (lists of dictionaries)
# ----------------------------------------------------------------------
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120, "stock": 15},
    {"id": 103, "name": "Eggs", "category": "Dairy", "price": 320, "stock": 4},
    {"id": 104, "name": "Rice", "category": "Grains", "price": 450, "stock": 30},
]

sales = []

LOW_STOCK_LIMIT = 5  # stock below this value is reported as "low"


# ----------------------------------------------------------------------
# Input helper functions (validate user input)
# ----------------------------------------------------------------------
def read_text(prompt):
    """Keep asking until the user types a non-empty text."""
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Error: This field cannot be empty.")


def read_int(prompt, minimum):
    """Keep asking until the user types a whole number >= minimum."""
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print("Error: Please enter a valid whole number.")
            continue
        if number < minimum:
            print(f"Error: The value must be at least {minimum}.")
            continue
        return number


def read_price(prompt):
    """Keep asking until the user types a price greater than zero."""
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
        except ValueError:
            print("Error: Please enter a valid price (for example 250 or 99.5).")
            continue
        if not math.isfinite(number) or number <= 0:
            print("Error: Price must be a number greater than 0.")
            continue
        return round(number, 2)


# ----------------------------------------------------------------------
# Product helper functions
# ----------------------------------------------------------------------
def find_product_by_id(product_id):
    """Return the product dictionary with this ID, or None if not found."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def print_product_details(product):
    """Print every detail of one product."""
    print(f"  Product ID : {product['id']}")
    print(f"  Name       : {product['name']}")
    print(f"  Category   : {product['category']}")
    print(f"  Price      : {product['price']:.2f}")
    print(f"  Stock      : {product['stock']}")


# ----------------------------------------------------------------------
# Menu option functions
# ----------------------------------------------------------------------
def add_product():
    """Option 1: add a new product (duplicate IDs are not allowed)."""
    print("\n--- Add New Product ---")
    product_id = read_int("Enter Product ID: ", 1)

    # Prevent duplicate product IDs
    if find_product_by_id(product_id) is not None:
        print("Error: A product with this ID already exists. Product not added.")
        return

    name = read_text("Enter Product Name: ")
    category = read_text("Enter Category: ")
    price = read_price("Enter Price: ")
    stock = read_int("Enter Available Stock: ", 0)

    # Store the product as a dictionary and append it to the list
    new_product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
    }
    products.append(new_product)
    print(f"Success: '{name}' was added to the store.")


def view_all_products():
    """Option 2: display all products in a table."""
    print("\n--- All Products ---")
    if len(products) == 0:
        print("No products available.")
        return

    print(f"{'ID':<8}{'Name':<22}{'Category':<16}{'Price':>10}{'Stock':>8}")
    print("-" * 64)
    for product in products:
        print(
            f"{product['id']:<8}{product['name']:<22}{product['category']:<16}"
            f"{product['price']:>10.2f}{product['stock']:>8}"
        )


def search_product():
    """Option 3: search by product ID or by (part of) the product name."""
    print("\n--- Search Product ---")
    text = read_text("Enter Product ID or Name: ")

    # Treat the text as an ID only if it is a plain number
    is_number = text.isascii() and text.isdigit()
    found_count = 0

    for product in products:
        id_matches = is_number and product["id"] == int(text)
        name_matches = text.lower() in product["name"].lower()
        if id_matches or name_matches:
            found_count += 1
            print(f"\nProduct found ({found_count}):")
            print_product_details(product)

    if found_count == 0:
        print("Product not found. No product matches that ID or name.")


def update_stock():
    """Option 4: add stock to a product or set its stock quantity."""
    print("\n--- Update Product Stock ---")
    product_id = read_int("Enter Product ID: ", 1)
    product = find_product_by_id(product_id)

    if product is None:
        print("Error: Product not found.")
        return

    print(f"Current stock of {product['name']}: {product['stock']}")
    print("1. Add stock")
    print("2. Set new stock quantity")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        extra = read_int("Enter quantity to add: ", 1)
        product["stock"] = product["stock"] + extra
    elif choice == "2":
        product["stock"] = read_int("Enter new stock quantity: ", 0)
    else:
        print("Error: Invalid choice. Stock was not changed.")
        return

    print("Stock updated successfully.")
    print(f"Updated stock of {product['name']}: {product['stock']}")


def process_sale():
    """Option 5: sell a product to a customer and record the sale."""
    print("\n--- Process Customer Sale ---")
    product_id = read_int("Enter Product ID: ", 1)
    product = find_product_by_id(product_id)

    if product is None:
        print("Error: Product not found. Sale cancelled.")
        return

    quantity = read_int("Enter purchase quantity: ", 1)

    # Do not allow a sale if there is not enough stock
    if quantity > product["stock"]:
        print(f"Error: Insufficient stock. Only {product['stock']} unit(s) of "
              f"{product['name']} available. Sale cancelled.")
        return

    total = round(product["price"] * quantity, 2)
    product["stock"] = product["stock"] - quantity

    # Store the completed sale in the sales list
    sale_record = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total,
    }
    sales.append(sale_record)

    print("\n--- Purchase Summary ---")
    print(f"Product        : {product['name']} (ID {product['id']})")
    print(f"Unit Price     : {product['price']:.2f}")
    print(f"Quantity       : {quantity}")
    print(f"Total Price    : {total:.2f}")
    print(f"Remaining Stock: {product['stock']}")


def view_sales_records():
    """Option 6: display all completed sales."""
    print("\n--- Sales Records ---")
    if len(sales) == 0:
        print("No sales have been recorded yet.")
        return

    print(f"{'No.':<6}{'Product ID':<12}{'Product Name':<22}{'Qty':>6}{'Total Amount':>16}")
    print("-" * 62)
    number = 1
    for sale in sales:
        print(
            f"{number:<6}{sale['product_id']:<12}{sale['product_name']:<22}"
            f"{sale['quantity_sold']:>6}{sale['total_amount']:>16.2f}"
        )
        number += 1


def print_products_with_price(label, price):
    """Print every product whose price equals the given price."""
    for product in products:
        if product["price"] == price:
            print(f"{label}: {product['name']} (ID {product['id']}) - {product['price']:.2f}")


def generate_report():
    """Option 7: display the final store report."""
    print("\n====================================")
    print("          STORE REPORT")
    print("====================================")

    total_products = len(products)
    total_stock = 0
    for product in products:
        total_stock = total_stock + product["stock"]

    total_revenue = 0
    for sale in sales:
        total_revenue = total_revenue + sale["total_amount"]

    print(f"Total number of products : {total_products}")
    print(f"Total available stock    : {total_stock}")
    print(f"Total sales transactions : {len(sales)}")
    print(f"Total revenue generated  : {total_revenue:.2f}")

    # Products with stock below the limit
    print(f"\nProducts with stock below {LOW_STOCK_LIMIT} units:")
    low_count = 0
    for product in products:
        if product["stock"] < LOW_STOCK_LIMIT:
            print(f"  - {product['name']} (ID {product['id']}): {product['stock']} left")
            low_count += 1
    if low_count == 0:
        print("  None")

    # Highest and lowest priced products
    print()
    if total_products == 0:
        print("Highest priced product: N/A (no products)")
        print("Lowest priced product : N/A (no products)")
        return

    highest = products[0]["price"]
    lowest = products[0]["price"]
    for product in products:
        if product["price"] > highest:
            highest = product["price"]
        if product["price"] < lowest:
            lowest = product["price"]

    print_products_with_price("Highest priced product", highest)
    print_products_with_price("Lowest priced product ", lowest)


# ----------------------------------------------------------------------
# Main program
# ----------------------------------------------------------------------
def show_menu():
    """Print the main menu."""
    print("\n====================================")
    print("SMART GROCERY STORE SYSTEM")
    print("====================================\n")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit\n")


def main():
    """Show the menu again and again until the user chooses Exit."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            process_sale()
        elif choice == "6":
            view_sales_records()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("\nThank you for using the Smart Grocery Store System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
