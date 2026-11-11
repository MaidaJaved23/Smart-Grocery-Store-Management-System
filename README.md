<div align="center">

<img src="assets/banner.svg" alt="Smart Grocery Store Management System" width="100%">

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-none-brightgreen)
![Interface](https://img.shields.io/badge/Interface-Console%20Menu-0f766e)
![Tests](https://img.shields.io/badge/Tests-25%20checks%20passing-success)
![Data](https://img.shields.io/badge/Data-Lists%20%26%20Dictionaries-orange)

**A simple, easy-to-read console application that helps a local grocery store manage products, stock, sales and reports.**

</div>

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Features at a Glance](#-features-at-a-glance)
3. [Quick Start](#-quick-start)
4. [Application Menu](#-application-menu)
5. [Task-by-Task Description](#-task-by-task-description)
6. [Data Structures](#-data-structures)
7. [ER Diagram & Data Hierarchy](#-er-diagram--data-hierarchy)
8. [Code Explanation & Function Hierarchy](#-code-explanation--function-hierarchy)
9. [Input Validation Rules](#-input-validation-rules)
10. [Sample Run](#-sample-run)
11. [Testing](#-testing)
12. [Requirements Checklist](#-requirements-checklist)
13. [Project Structure](#-project-structure)

---

## 🛒 Overview

The store owner needs to keep records of **products, prices, available stock and sales**.
This program does exactly that using plain Python — **lists of dictionaries** for storage, **loops** to process records, **conditionals** to choose operations, and **custom functions** to keep the code organised.

It runs from a menu and keeps running until the user chooses **Exit**.

> 💡 **Design goal:** the simplest and easiest logic possible. No classes, no files, no external libraries — only the basics taught in an introductory Python course.

---

## ✨ Features at a Glance

| # | Feature | What it does |
|---|---------|--------------|
| 1 | ➕ **Add New Product** | Reads product details, blocks duplicate IDs, stores a dictionary with `.append()` |
| 2 | 📋 **View All Products** | Prints a neat table of ID, name, category, price and stock |
| 3 | 🔍 **Search Product** | Finds products by **ID** or **name** (case-insensitive, partial names work) |
| 4 | 📦 **Update Stock** | Add stock to a product *or* set an exact quantity, then shows the result |
| 5 | 💰 **Process Sale** | Checks product + stock, calculates total, deducts stock, prints a summary |
| 6 | 🧾 **View Sales Records** | Lists every completed sale |
| 7 | 📊 **Store Report** | Totals, revenue, low-stock items, highest and lowest priced products |
| 8 | 🚪 **Exit** | Ends the program politely |

---

## 🚀 Quick Start

**Requirements:** Python 3.8 or newer. No extra packages.

```bash
# 1. Unzip the project and open the folder
cd smart_grocery_store

# 2. Run the program
python grocery_store.py          # on some systems: python3 grocery_store.py
```

The store starts with four sample products (Milk, Bread, Eggs, Rice) so every option can be tried immediately.

---

## 🧭 Application Menu

```text
====================================
SMART GROCERY STORE SYSTEM
====================================

1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice:
```

Any choice other than `1`–`8` shows an error message and the menu appears again.

---

## 📝 Task-by-Task Description

### 1️⃣ Product Management
Products live in a list called `products`. Each product is a dictionary with the keys `id`, `name`, `category`, `price`, `stock`.

### 2️⃣ Add New Products — `add_product()`
1. Asks for the **Product ID** first and checks the list with `find_product_by_id()`.
2. If the ID already exists → *"A product with this ID already exists"* and nothing is added.
3. Otherwise asks for name, category, price and stock, builds a dictionary and adds it with `products.append(...)`.

### 3️⃣ Display All Products — `view_all_products()`
Loops through `products` and prints one aligned row per product (name, category, price, stock). Shows *"No products available"* if the list is empty.

### 4️⃣ Search Products — `search_product()`
- Type a **number** → matches the product ID.
- Type **text** → matches product names (upper/lower case ignored, part of a name is enough, e.g. `mil` finds *Milk*).
- Prints the **complete details** of every match, or *"Product not found"* if there is none.

### 5️⃣ Update Product Stock — `update_stock()`
Asks for a Product ID, then offers:
- **1. Add stock** → new stock = old stock + quantity entered
- **2. Set new stock quantity** → stock becomes the quantity entered (0 is allowed)

The updated stock is displayed afterwards.

### 6️⃣ Process a Customer Sale — `process_sale()`
| Step | Check / Action |
|------|----------------|
| 1 | Ask for Product ID → **does the product exist?** If not, the sale is cancelled |
| 2 | Ask for quantity (must be 1 or more) |
| 3 | **Is there enough stock?** If `quantity > stock` the sale is **refused** (stock stays unchanged) |
| 4 | Calculate `total = price × quantity` |
| 5 | Deduct the quantity from the stock |
| 6 | Save the sale in the `sales` list and print a **purchase summary** |

### 7️⃣ Store Sales Records — `view_sales_records()`
Every successful sale is saved as a dictionary in the separate `sales` list. Option 6 prints them all in a table.

### 8️⃣ Generate Store Report — `generate_report()`
Displays:
- Total number of products
- Total available stock (sum of all stock)
- Total sales transactions
- Total revenue generated
- Products with stock **below 5** units
- Product(s) with the **highest** price
- Product(s) with the **lowest** price

> If two products share the highest (or lowest) price, **both** are shown.

---

## 🗃️ Data Structures

**`products`** – list of dictionaries

```python
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
]
```

**`sales`** – separate list of dictionaries

```python
sales = [
    {"product_id": 101, "product_name": "Milk", "quantity_sold": 4, "total_amount": 1000.0},
]
```

---

## 🧬 ER Diagram & Data Hierarchy

The program has two entities. **PRODUCT** is stored in the `products` list and **SALE** is stored in the `sales` list. One product can appear in many sales (**1 : N**), connected by the product ID.

<div align="center">
<img src="assets/er-diagram.svg" alt="Entity-Relationship diagram" width="100%">
</div>

The same diagram in text form (GitHub renders it automatically):

```mermaid
erDiagram
    PRODUCT ||--o{ SALE : "is sold in"
    PRODUCT {
        int id PK "unique"
        string name
        string category
        float price
        int stock
    }
    SALE {
        int product_id FK
        string product_name
        int quantity_sold
        float total_amount
    }
```

**Data hierarchy (tree view)**

```text
GROCERY STORE (running program)
├── products  (list)
│   └── PRODUCT (dictionary)
│       ├── id        → int,   unique, ≥ 1
│       ├── name      → str,   not empty
│       ├── category  → str,   not empty
│       ├── price     → float, > 0
│       └── stock     → int,   ≥ 0
└── sales  (list)
    └── SALE (dictionary)
        ├── product_id     → int  (links to PRODUCT.id)
        ├── product_name   → str
        ├── quantity_sold  → int, ≥ 1
        └── total_amount   → float (price × quantity)
```

---

## 🧠 Code Explanation & Function Hierarchy

`main()` shows the menu in a `while True` loop and uses `if / elif / else` to call the correct function. Choice `8` uses `break` to leave the loop.

<div align="center">
<img src="assets/hierarchy.svg" alt="Function hierarchy" width="100%">
</div>

| Function | Purpose |
|----------|---------|
| `read_text(prompt)` | Repeats until the user types non-empty text |
| `read_int(prompt, minimum)` | Repeats until the user types a whole number ≥ `minimum` |
| `read_price(prompt)` | Repeats until the user types a valid price greater than 0 |
| `find_product_by_id(product_id)` | Loops through `products`; returns the matching dictionary or `None` |
| `print_product_details(product)` | Prints all five fields of one product |
| `print_products_with_price(label, price)` | Prints every product with a given price (used for highest / lowest) |
| `add_product()` … `generate_report()` | One function per menu option (1–7) |
| `show_menu()` / `main()` | Display the menu and run the program loop |

**Key idea:** dictionaries are accessed by key (`product["stock"]`), and because a product dictionary is shared, changing `product["stock"]` inside a function updates the real list — no copying needed.

---

## 🛡️ Input Validation Rules

| Input | Rule | If invalid |
|-------|------|-----------|
| Menu choice | `1`–`8` | Error message, menu shown again |
| Product ID | Whole number ≥ 1, not already used (when adding) | Asks again / rejects duplicate |
| Name, Category | Not empty | Asks again |
| Price | Number > 0 (`nan`/`inf` rejected) | Asks again |
| Stock (new product / set) | Whole number ≥ 0 | Asks again |
| Quantity to add / sell | Whole number ≥ 1 | Asks again |
| Sale quantity | Must not exceed available stock | Sale cancelled with a clear message |
| `Ctrl + C` / end of input | — | Program closes politely (no crash) |

---

## 🖥️ Sample Run

Selling 4 Milk, then trying to sell more Eggs than available, then opening the report:

```text
--- Process Customer Sale ---
Enter Product ID: 101
Enter purchase quantity: 4

--- Purchase Summary ---
Product        : Milk (ID 101)
Unit Price     : 250.00
Quantity       : 4
Total Price    : 1000.00
Remaining Stock: 16

--- Process Customer Sale ---
Enter Product ID: 103
Enter purchase quantity: 10
Error: Insufficient stock. Only 4 unit(s) of Eggs available. Sale cancelled.

====================================
          STORE REPORT
====================================
Total number of products : 4
Total available stock    : 65
Total sales transactions : 1
Total revenue generated  : 1000.00

Products with stock below 5 units:
  - Eggs (ID 103): 4 left

Highest priced product: Rice (ID 104) - 450.00
Lowest priced product : Bread (ID 102) - 120.00
```

---

## ✅ Testing

An automated test file with **25 checks** is included. It feeds inputs to the program and verifies the results, including:

- valid and invalid input for every field, duplicate IDs
- search by ID / full name / partial name / not found
- add stock, set stock, invalid stock choice, unknown ID
- sale success, unknown product, insufficient stock, selling exactly all stock, out-of-stock item
- report with and without sales, tied prices, completely empty store
- invalid menu choices and clean exit

Run it with:

```bash
python tests/test_grocery_store.py
```

Expected last line: `ALL 25 CHECKS PASSED`

---

## 📌 Requirements Checklist

| Requirement | Where it is met |
|-------------|-----------------|
| Python application | `grocery_store.py` |
| Lists and dictionaries as primary data structures | `products` and `sales` |
| At least two custom functions | 15 functions |
| Loops to process records | `for` loops in view, search, report; `while` loops in menu and input helpers |
| Dictionary keys and values | e.g. `product["price"]`, `sale["total_amount"]` |
| Conditional statements | `if / elif / else` in `main()`, sale checks, stock update |
| Meaningful names | `process_sale`, `find_product_by_id`, `total_revenue`, … |
| Proper indentation and formatting | 4-space indentation, one blank line / two between functions |
| Input validation | Helper functions `read_text`, `read_int`, `read_price` |
| Comments on important parts | Docstrings and inline comments |
| `.append()` for new products and sales | `add_product()`, `process_sale()` |
| Menu runs until Exit | `while True` loop in `main()` |

---

## 📁 Project Structure

```text
smart_grocery_store/
├── grocery_store.py            # the application (run this file)
├── README.md                   # this document
├── assets/
│   ├── banner.svg              # animated banner
│   ├── er-diagram.svg          # ER diagram (high-resolution vector)
│   └── hierarchy.svg           # function hierarchy (high-resolution vector)
└── tests/
    └── test_grocery_store.py   # 25 automated checks
```

<div align="center">

**Made with Python 🐍 — simple logic, clear code.**

</div>
