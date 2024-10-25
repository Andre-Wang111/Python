# 99乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}*{i}={j*i}")


# while迴圈
# 這是條件式迴圈，當條件成立時，會執行迴圈內的程式
i = 1
while i < 10:
    # 當i小於10時，執行迴圈內的程式
    print(i)
    i = i + 1

# 算數指定運算子
# +=、-=、*=、**=、/=、//=、%=

# x = x + 1  等於x += 1
# x = x - 1  等於x -= 1
# x = x * 1  等於x *= 1
# x = x ** 1 等於x **= 1
# x = x / 1  等於x /= 1
# x = x // 1 等於x //= 1
# x = x % 1  等於x %= 1
i = 1
while i < 10:
    print(i)
    i += 1

print("----------------------------")


password = "123":
user_input = " "
while user_input != password:
    user_input = input("請輸入密碼:")
print("密碼正確")
