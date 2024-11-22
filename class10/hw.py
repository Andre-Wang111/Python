import random as r

start = 0
end = 100
m = r.randrange(1, 101)
num = 0
while num != m:
    num = int(input(f"請輸入一個{start}到{end}之間的數字："))
    if num < m:
        print("再大一點！")
        if num > start:
            start = num
    elif num > m:
        print("再小一點！")
        if num < end:
            end = num

print(f"恭喜你猜到了！答案是{m}")
