# 準備的食物清單
food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "pizza": 2}

# 輸出結果
print("執行結果：")
for item, quantity in food_list.items():
    if item == "果汁":
        print(f"{item}：{quantity}杯")
    else:
        print(f"{item}：{quantity}份")


print("----------------------------------------------------------------")


food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 15}
for k, v in food_list.items():
    if k == "果汁":
        print(f"{k}: {v}杯")
    else:
        print(f"{k}: {v}份")
