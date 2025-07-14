product_info = ("Keyboard", 1500, 2)

# Unpack
product, price, quantity = product_info
total = price * quantity
print(f"Product: {product}, Price: {price}, Quantity: {quantity}, Total: {total}")

product_list = list(product_info)
product_list[2] = 3

updated_tuple = tuple(product_list)
print("Updated tuple:", updated_tuple)