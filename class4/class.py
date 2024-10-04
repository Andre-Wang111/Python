# 比較運算子
print(1 == 1)  # True,1等於1
print(1 != 1)  # False,1不等於1
print(1 > 1)  # True,1大於1
print(1 < 1)  # False,1小於1
print(1 >= 1)  # True,1大於等於1
print(1 <= 1)  # False,1小於等於1

# 邏輯運算子
print(True and True)  # True, True和True
print(True and False)  # False, True和False
print(False and True)  # False, False和True
print(True or True)  # True, True或True
print(True or False)  # True, True或False
print(False or False)  # False, False或False
print(not True)  # False, not True
print(not False)  # True, not False

# if
pwd = input("請輸入密碼:")
if pwd == "123":  # 如果密碼是123
    print("密碼正確")  # 印出密碼正確

# if else
pwd = input("請輸入密碼:")
if pwd == "123":  # 如果密碼是123
    print("密碼正確")  # 印出密碼正確
else:  # 如果密碼不是123
    print("密碼錯誤")  # 印出密碼錯誤

# if elif else
pwd = input("請輸入密碼:")
if pwd == "123":
    print("welcome Andre")
elif pwd == "456":  # 如果密碼是456
    print("welcome Alan")  # 印出歡迎Alan
else:
    print("密碼錯誤")

# if elif else 是連續的判斷，只要有一個條件成立，後面的判斷就不會執行
# if 一定要有，elif可以有多個但是選用，else只能有一個但是選用

score = int(input("請輸入成績:"))
if score >= 101:
    print("輸入錯誤!")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
