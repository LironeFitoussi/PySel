# Initialize the cart with 0 items
items_in_cart = 0

def add_items(number):
    """Function to add items to the cart."""
    global items_in_cart
    items_in_cart += number
    print(f"Added {number} items to the cart. Total now: {items_in_cart}")

# Add 2 items to the cart
add_items(2)

# QA check: Verify that the cart contains exactly 2 items
if items_in_cart != 2:
    raise Exception(f"QA Check Failed: Expected 2 items in the cart, found {items_in_cart}")
else:
    print("QA Check Passed: 2 items in the cart.")

# Add 1 more item to the cart
add_items(1)

# Use an assertion to check the number of items in the cart is now 3
assert items_in_cart == 3, f"Assertion Failed: Expected 3 items in the cart, found {items_in_cart}"
print("Assertion Passed: 3 items in the cart.")
