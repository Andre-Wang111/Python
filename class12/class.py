# list 型態轉換
print(range(10))  # 產生一個range但看不到裡面的數字
print(list(range(10)))  # 將list 轉換成 range
print(list("hello"))  # 將字串轉換成list

# split
s = "hello world"
L = s.split(" ")  # 將字串以空白分割
print(L)
calender = ("2024", "1", "1")
L = calender.split(" / ")  # 將字串以 / 分割
print(L)

# join
L = ["hello", "world"]
s = " ".join(L)  # 將list以空白合併
print(s)

# append
L = ["hello", "world"]
L.append("python")  # 將 python 加到 list 當中
print(L)

# remove
L = ["hello", "world", "python"]
L.remove("world")  # 移除 world
print(L)

# pop
L = ["hello", "world", "python"]
s = L.pop(1)  # 移除索引1的元素
print(s)

# count
L = ["hello", "world", "python", "hello"]
print(L.count("hello"))  # hello 出現的次數
