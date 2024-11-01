"""
Let's create a checkout register program!
1. Each time you enter (input) the price of an item, the program will add it to the total amount.
2. The program will show the new total every time you add a new item.
3. When you enter 0, the program will stop adding and end the checkout.

for example (in terminal):
---
Please enter the item price: 10
Current total is 10 dollars.

Please enter the item price: 23
Current total is 33 dollars.

Please enter the item price: 55
Current total is 88 dollars.

Please enter the item price: 100
Current total is 188 dollars.

Please enter the item price: 0
---
"""

price = int(input("Please enter the item price: "))
sum = 0
while price != 0:
    sum += price
    print(f"Current total is {sum} dollars.")
    price = int(input("Please enter the item price: "))


print("-------------------------------------------")

# 質數判斷
num = int(input("請輸入數字:"))
is_Prime = True
for i in range(2, num):
    if num % i == 0:
        is_Prime = False

if is_Prime and num > 1:
    print(f"{num}是質數")
else:
    print(f"{num}不是質數")
