import turtle as t

t.color("dark blue")
t.pensize(100)
t.shape("triangle")
# arrow、circle、square、triangle、classic、turtle
t.stamp()  # 蓋章
t.penup()  # 提筆
t.done()


import turtle as t

t.color("dark blue")
t.shape("circle")
t.penup()

for i in range(5, 61, 2):
    t.stamp()
    t.forward(i)
    t.right25
    print(i)

t.done()

print("----------------------------")


import time

print("開始計時")
time.sleep(5)  # 暫停5秒
print("結束計時")

import turtle as t

t.speed(1)
t.penup()

for i in range(12):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(30)

t.right(6)
t.pendown
t.forward(80)
t.penup()
time.sleep(1)
t.backward(80)
t.clear()  # 清除畫面
t.done()

print("----------------------------")


num = int(input("請輸入數字:"))
sum = 0
for i in range(num + 1):
    sum = sum + i

print(f"0到{num}的總和為{sum}")
