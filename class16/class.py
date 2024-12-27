# 區域變數與全域變數 - imagine 家裡and學校的toy
# 區域變數is you personal toy, only you can play with it
# 全域變數is everyone's toy, everyone can play with it
toy_name = "toy bear"  # 全域變數 , everyone can play with it


def play_with_toy():
    toy_name = "Lego"  # 區域變數 , only you can play with it
    print(f"I'm playing with {toy_name}")


def share_toy():
    global toy_name  # 告訴 Python 我要使用everone's toy
    toy_name = "block"
    print(f"I'm sharing {toy_name}")


# let's see how the toy changes :
print(f" at the start, toy is {toy_name}")  # 顯示 : toy bear
play_with_toy()
print(f" at the end, toy is still {toy_name}")  # 顯示 : toy bear(nothing changed)

# \n 是換行符號

print("\n now let's change everyone's toy:")
print("The classroom toy is: {toy_name}")
share_toy()
print("Now the classroom toy has changed to: {toy_name}")


# 函式可以回傳資料
# return 是回傳的keyword , 代表這個函式處理完後要交回甚麼結果
def calculate_sum(num1, num2=0):
    total = num1 + num2
    return total


result = calculate_sum(5, 3)
print(f"Sum of 5+3 is {result}")
result = calculate_sum(10)
print(f"Sum of 10+0 is {result}")


# 函式參數預設值的順序 - 有預設值的參數一定要放在沒有預設值的參數後面


# This is correct:
def order_lunch(main_dish, side_dish="salad"):
    print(f"Main dish is : {main_dish}")
    print(f"Side dish is : {side_dish}")


# This is wrong:
"""
def wrong_order(dessert = "ice cream", meal ):
    print(f"Meal is : {meal}")
    print(f"Dessert is : {dessert}")
"""
