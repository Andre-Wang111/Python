# list len
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得list的長度, 也就是List當中有幾筆資料
# 務必不要跟index混淆, index是資料的編號, len是資料的數量
#  len 可以搭配 for 迴圈使用來取得list當中的所有資料
for i in range(len(L)):  # 這邊的 i 是 index
    print(L[i])

for i in L:  # 這邊的 i 是資料
    print(i)

# 要使用哪種方式讀取 List 當中的資料, 要看使用的情境當中會不會需要 index


print("---------------------------------------------------------------")


juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "Coca Cola", "系統關閉"]

while True:
    for i in range(len(juices_list)):
        print(f"{ i + 1 }. {juices_list [i]}")
    try:
        select = int(input("請輸入編號:"))
    except:
        print("請輸入數字")
        continue
    if juices_list[select - 1] == "系統關閉":
        print("系統關閉")
        break
    elif select > 4:
        print("查無果汁")
        continue
    else:
        print(f"你點的商品是 {juices_list[select - 1]}")


print("---------------------------------------------------------------")


# 更新List當中的資料
L = [1, 2, 3, 4, 5]
L[0] = 100  # 更新第一筆資料
print(L)

# List 跟字串很像的地方
# 合併清單資料
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)

# 重複清單資料
L = [1, 2, 3]
L = L * 3
print(L)
