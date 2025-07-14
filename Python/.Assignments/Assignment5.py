# 1. Combine names
first = "Hiral"
last = "Shewale"
full_name = first + " " + last
print("Full Name:", full_name)

# 2. Formatted price string
item = "Laptop"
price = 799.99
print(f"The price of {item} is ${price}")

# 3. Uppercase conversion
s = "hello world"
print(s.upper())

# 4. Join list into sentence
words = ['Python', 'is', 'awesome']
print(" ".join(words))

# 5. Today's date in DD-MM-YYYY
from datetime import datetime
today = datetime.now()
print("Today's Date:", today.strftime("%d-%m-%Y"))