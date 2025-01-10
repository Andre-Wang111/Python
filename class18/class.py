# 檔案讀寫
# 判斷檔案是否存在 - 使用 os.path.exists() 函式

import os

# 相對路徑代表相對於目前的工作目錄的路徑
# 絕對路徑代表完整的路徑
if os.path.exists("class17/hw.py"):
    print("檔案存在")
else:
    print("檔案不存在")


# open() 開啟模式
# r - 讀取模式，檔案必須存在
# w - 寫入模式，檔案不存在會自動建立
# a - 附加模式，檔案不存在會自動建立
# r+ - 讀取與寫入模式，檔案必須存在
# w+ - 讀取與寫入模式，檔案不存在會自動建立
# a+ - 讀取與附加模式，檔案不存在會自動建立


# 讀取檔案 - 使用 open() 函式
with open("class18/file_test.py", "r") as file:
    print(file.read())


# 寫入檔案 - 使用 open() 函式
file = open("class18/file_test.py", "w")
file.write("print('Hello World!')")
file.close()


# 寫入檔案 - 使用 with open() as 函式
