import random as r  # this is a  隨機模組

# random.randrange 設定範圍的方式跟 range 一樣, 特性也一樣不包含 the last number
# random.randrange 的公能是隨機取得一個數字, range 是取得一組數字
print(r.randrange(10))  # 隨機取得一個數字, 取得的數字在 0 到 9 之間
print(r.randrange(1, 10))  # 隨機取得一個數字, 取得的數字在 1 到 9 之間
print(r.randrange(1, 10, 2))  # 隨機取得一個數字, 在 1、3、5、7、9 之間


# random.randint 設定範圍的方式必須要有開始和結束, but特性包含 the last number
# 不能跳數字抽籤
print(r.randint(1, 10))  # 隨機取得一個數字,在 1 到 10 之間


# 猜數字遊戲
import random as r

target_number = r.randint(1, 100)

print("請輸入一個1到100之間的數字")

while True:
    guess = int(input("請輸入你的猜測數字："))

    if guess < target_number:
        print("再大一點！")
    elif guess > target_number:
        print("再小一點！")
    else:
        print("恭喜猜中！")
        break


# list 清單
# list 可以存入很多資料, 每筆資料用 ',' 隔開
# list 可以存入不同的資料類型
# list 最外層用 '[]' 包起來
L = [
    1,
    2,
    3,
    4,
    5,
]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "Hello", ["World", 6]]  # 數字、字串、list
print(L)

# list 取值
# list 取值方式跟字串一樣, 用 ' [] ' 取值
# list 取值方式跟字串一樣, 也可以用 ' [] ' 取值
# list 當中資料的編號(index)都是從 0 開始

L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# list 取值方式跟字串一樣, 也可以用 ' [ : ] ' 取值
# 設定範圍的方式跟 range 一樣, 特性也一樣不包含 the last number
print(L[1:4:2])  # 取出第二到第四個值, 間隔為 2
print(L[0:3])  # 取出第一到第三個值
print(L[:3])  # 取出第一個到第三個值
print(L[3:])  # 取出第四個到最後一個值
print(L[:])  # 取出所有值
