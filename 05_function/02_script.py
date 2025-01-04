def add_to_cart(items, cart=None):
    if cart is None:
        cart = []
    if isinstance(items, list):
        cart.extend(items)  # Add multiple items if a list is provided
    else:
        cart.append(items)  # Add a single item
    return cart

# Adding a single item
cart1 = add_to_cart("basuri")
print(cart1)

# Adding another single item
cart2 = add_to_cart("murali")
print(cart2)

# Adding multiple items
cart3 = add_to_cart(["murali", "basuri"])
print(cart3)
