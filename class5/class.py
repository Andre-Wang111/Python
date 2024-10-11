數字 = int(input("請輸入數字:"))
if 數字 % 2 == 0:
    print("數字是偶數")
else:
    print("數字是奇數")


# 匯入模組
# import turtle  # 匯入模組turtle
import turtle as t  # 匯入模組turtle並取名為t

# from turtle import * #匯入模組turtle的所有指令
# from turtle import done # 匯入模組turtle的指令done

# done()
# turtle.done()

t.speed(1)  # 設定速度為1
t.forward(100)  # 前進100步
t.left(90)  # 向左轉90度
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


# 發現turtle一開始面向右邊
t.done()  # 讓視窗不要關閉


# for example
# for的組成有三個部份
# for 迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈裡面
# 迴圈變數每回合都會從範圍裡面取出一個值
for i in range(6):  # range 可以產生一組數字, 0~5
    print(i)

for i in range(1, 6):  # range = 1~5
    print(i)

for i in range(1, 6, 2):  # range = 1,3,5
    print(i)


import turtle as t

t.penup()
