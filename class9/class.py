#  for else
# 如果for迴圈正常結束，則執行else區塊

import time


for i in range(5):
    print(i)
else:
    print("迴圈正常結束")

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("迴圈正常結束")


# 使用者輸入秒數
seconds = int(input("Please enter the number of seconds: "))

# 倒數計時
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)  # 每秒休息 1 秒

# 當倒數結束時顯示訊息
print("Time's up!")


# loop continue
for i in range(5):
    if i == 3:
        continue
    print(i)

i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

    # 輸入想要跳繩的次數
num_of_jumps = int(input("Please enter the number of times you want to jump rope: "))

# 開始計算跳繩次數
for i in range(1, num_of_jumps + 1):
    # 如果次數是 10 的倍數，則休息
    if i % 10 == 0:
        print("Take a break")
        continue
    # 其他次數則顯示跳繩次數
    if i == 1:
        print(f"Jump {i} time")
    else:
        print(f"Jump {i} times")


# loop break
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(j)
    if i == 3:
        break
    print(i)

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
