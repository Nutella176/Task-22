# Create menu list
# Create a dictionary containing stock levels
# Create a dictionary containing the price of each menu item
menu = ["muffin", "carrot cake", "espresso", "cappuccino"]
stock = {"muffin": 10, "carrot cake": 10, "espresso": 10, "cappuccino": 10}
price = {"muffin": 3, "carrot cake": 3, "espresso": 2, "cappuccino": 2}

# Clculate stock worth by multiplying the stock levels with the item price
multiply = {key: stock[key] * price[key] for key in stock}

# Print the sum
print(sum(multiply.values()))
