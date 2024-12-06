# index 找出元素在清單中的位置
L = [1, 3, 2, 4, 5]
print(L.index(3))  # 1

# sort 排序, 預設是由小到大
L = [1, 3, 2, 4, 5]
L.sort()
print(L)

# sort reverse 由小到大
L = [1, 3, 2, 4, 5]
L.sort(reverse=True)
print(L)

# reverse 反轉清單當中的元素, 不是排序
L = [1, 3, 2, 4, 5]
L.reverse()
print(L)

# 字典
# 建立字典
d = {"apple": 20, "banana": 30, "orange": "25"}
print(d)

# 取得字典的值
d = {"apple": 20, "banana": 30, "orange": "25"}
print(d["apple"])
# print(d["pear"])  # KeyError : pear

# len 取得字典的長度
d = {"apple": 20, "banana": 30, "orange": "25"}
print(len(d))

# 檢查key是否存在
d = {"apple": 20, "banana": 30, "orange": "25"}
print("apple" in d)  # True
print("pear" in d)  # False

# 字典走訪
d = {"apple": 20, "banana": 30, "orange": "25"}
for k in d:
    print(k)  # 這樣只會印出key
    print(d[k])  # 這樣只會印出value

for v in d.values():
    print(v)  # 這樣只會印出value

for k, v in d.items():
    print(f"{k}:{v}")  # 這樣會印出key和value
