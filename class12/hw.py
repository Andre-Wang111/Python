order = []  # 初始化菜單

while True:
    print("請選擇功能: 1. 新增餐點  2. 刪除餐點  3. 提交菜單")
    choice = input("請輸入功能代號 (1/2/3): ")

    if choice == "1":
        # 新增餐點
        item = input("請輸入餐點名稱: ")
        order.append(item)
        print(f"目前order={order}")

    elif choice == "2":
        # 刪除餐點
        item = input("請輸入餐點名稱: ")
        order = [i for i in order if i != item]  # 刪除所有相同名稱的餐點
        print(f"目前order={order}")

    elif choice == "3":
        # 提交菜單
        print("菜單提交如下:")
        unique_items = set(order)
        for item in unique_items:
            print(f"{item}: {order.count(item)}")
        break  # 結束程式

    else:
        print("無效的選項，請重新輸入。")


"""
程式邏輯與運作
order = []

初始化一個空列表，作為菜單的存放空間。
while True:

進入無限迴圈，用來持續處理用戶的輸入，直到用戶選擇提交菜單。
功能選擇 (choice)

提供三種功能讓用戶選擇：
1 新增餐點。
2 刪除餐點。
3 提交菜單並退出程式。
功能細節
新增餐點 (功能代號 1)
item = input("請輸入餐點名稱: ")
接收用戶輸入的餐點名稱。
order.append(item)
將輸入的餐點名稱新增到 order 列表中。
print(f"目前order={order}")
顯示目前的菜單內容。
刪除餐點 (功能代號 2)
item = input("請輸入餐點名稱: ")
接收用戶輸入的餐點名稱。
order = [i for i in order if i != item]
使用列表生成式，過濾掉與輸入名稱相符的所有餐點（即刪除所有同名項目）。
print(f"目前order={order}")
顯示刪除後的菜單內容。
提交菜單 (功能代號 3)
unique_items = set(order)
將菜單轉換為集合，去除重複項目，取得菜單中所有唯一餐點名稱。
統計餐點數量
for item in unique_items:
遍歷每個唯一的餐點。
order.count(item)
計算該餐點在列表中出現的次數。
print(f"{item}: {order.count(item)}")
逐一列出餐點名稱及其數量。
break
退出迴圈，結束程式執行。
無效選項
else:
當用戶輸入的功能代號不在 1/2/3 之間時，顯示錯誤訊息，提醒重新輸入。
執行範例
輸入 1
輸入餐點名稱：漢堡
輸出：目前order=['漢堡']
輸入 1
輸入餐點名稱：薯條
輸出：目前order=['漢堡', '薯條']
輸入 2
輸入餐點名稱：漢堡
輸出：目前order=['薯條']
輸入 3
提交菜單：
makefile
複製程式碼
菜單提交如下:
薯條: 1
改進建議
新增退出功能：

在功能選單中加入選項 4，允許用戶退出程式而不提交菜單。
elif choice == "4":
    print("已退出程式。")
    break
刪除單一項目功能：

若需要刪除單個餐點，可以改用 order.remove(item)，而不是一次移除所有同名項目。
提升易用性：

提供更清晰的提示訊息，讓用戶輸入前更容易理解操作。
"""
