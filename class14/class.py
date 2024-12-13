# 新增/修改字典的內容
d = {"apple": 20, "banana": 30, "orange": 25}
d["apple"] = 10
print(d)
d["pear"] = 15
print(d)

# 刪除字典的內容
d = {"apple": 20, "banana": 30, "orange": 25}
d.pop("apple")  # 刪除字典中的 apple
# 如果要刪除的key不存在, 會出現 KeyError 錯誤, 所以可以加上第二個參數, 當 key 不存在時, 不會有任何變化
popitem = d.pop("pear", "不存在這筆資料")  # nothing have changed
print(d)
print(popitem)
