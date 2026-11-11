Grocery Inventory Manager

1. Project Description

Grocery Inventory Manager is a Python-based project developed to manage grocery product stock. It helps users add products, update quantities, identify products with low stock and display the available inventory.

2. Problem Statement

Managing grocery stock manually can be difficult. It may become challenging to keep track of product quantities and identify products that need restocking. This project provides a simple solution to manage grocery inventory.

3. Project Objective

The main objective of this project is to develop a user-defined Python package that makes grocery stock management simple and organized.

4. Project Structure

Grocery-Inventory-Manager/
│
├── inventory_pkg/
│   ├── _init_.py
│   └── task.py
│
├── main.py
└── README.md

Description of files:

main.py: Contains the main menu, accepts user input and calls the package functions.
grocery_pkg: Contains the reusable Python functions.
init.py: Makes the package functions accessible for importing.
task.py: Contains the functions used for adding stock, updating stock, generating low-stock reports and displaying inventory.
README.md: Provides information about the project and instructions for running it.

5. Algorithms

Algorithm 1: Add Stock

Step 1-Start the program.
Step 2-Accept the product name from the user.
Step 3-Accept the quantity to be added.
Step 4-Check whether the quantity is valid.
Step 5-If the product already exists, increase its quantity.
Step 6-Otherwise, add the product as a new item.
Step 7-Display the success message.
Step 8-Stop the program.

Algorithm 2: Update Stock

Step 1-Start the program.
Step 2-Accept the product name.
Step 3-Accept the sold quantity.
Step 4-Check whether the product exists.
Step 5-If the product exists, check the available quantity.
Step 6-If sufficient stock is available, reduce the quantity.
Step 7-Otherwise, display an appropriate message.
Step 8-Stop the program.

Algorithm 3: Low Stock Report

Step 1-Start the program.
Step 2-Access the inventory dictionary.
Step 3-Check the quantity of each product.
Step 4-Compare the quantity with the low-stock limit.
Step 5-If the quantity is less than or equal to 5, display the product.
Step 6-Repeat until all products are checked.
Step 7-Stop the program.

Algorithm 4: Display Inventory

Step 1-Start the program.
Step 2-Access the inventory dictionary.
Step 3-Check all available products.
Step 4-Display each product name and its quantity.
Step 5-Stop the program.

Algorithm 5: Main Menu

Step 1-Start the program.
Step 2-Display the menu options.
Step 3-Accept the user's choice.
Step 4-Call the corresponding function.
Step 5-Repeat the menu until the user selects Exit.
Step 6-Stop the program.

6.Code Explanation

The project uses the following Python concepts:

| Python concept   | Purpose in the project                 |
| ---------------- | -------------------------------------- |
| Dictionary       | Stores product names and quantities    |
| Functions        | Perform separate inventory operations  |
| if-else          | Checks conditions and validates inputs |
| elif             | Handles multiple menu choices          |
| for loop         | Checks products in the inventory       |
| while loop       | Repeats the menu until Exit            |
| Package          | Organizes reusable functions           |
| Import statement | Connects the package with main.py      |

7.Conclusion

This project demonstrates the use of user-defined Python packages to solve a real-world grocery inventory management problem. It organizes reusable functions into a separate package and uses them through a main Python program.


