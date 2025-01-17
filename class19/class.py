# 附加檔案 - 使用 open() 函式
file = open("class19/file_test.py", "a")
file.write("\nprint('Hello Python!')")
file.close()

# 附加檔案 - 使用 with open() as
with open("class19/file_test.py", "a") as file:
    file.write("\nprint('Hello Python!')")

# replace - 取代字串中的特定字串
text = "Hello World!"
new_text = text.replace("World", "Python")
print(new_text)

# strip - 移除字串前後的空白
text = " Hello World! "
new_text = text.strip()
print(new_text)

# split - 依照特定字元分割字串
text = "Hello, World, Python"
words = text.split(",")
print(words)

# zfill - 字串補零
number = "10"
new_number = number.zfill(5)
print(new_number)

# datetime 模組
# datetme 模組提供了處理日期與時間的類別和函式
import datetime

# 取得當前日期和時間 - 使用 datetime.datetime.now() 函式
now = datetime.datetime.now()
print(now)

# 字串轉換為日期 - 使用 datetime.datetime.strptime() 函式
date = datetime.datetime.strptime("9999-01-01", "%Y-%m-%d")
print(date)

# 有哪些格式化字串可以使用？
# (What formatting strings can be used?)
# %Y - 年份（四位數）
# (Year (four digits))
# %m - 月份（兩位數）
# (Month (two digits))
# %d - 日期（兩位數）
# (Day (two digits))
# %H - 小時（24小時制，兩位數）
# (Hour (24-hour clock, two digits))
# %M - 分鐘（兩位數）
# (Minute (two digits))
# %S - 秒（兩位數）
# (Second (two digits))
# 例如：(For example:)
# %A - 星期幾的全名
# (Full name of the day of the week)
# %B - 月份的全名
# (Full name of the month)
# %c - 日期和時間的字串表示
# (String representation of date and time)
# %p - AM 或 PM
# (AM or PM)

#  日期轉換為字串 - 使用 datetime.datetime.strftime() 函式
date = datetime.datetime.now()
date_str = date.strftime("%Y-%m-%d")
print(date_str)


# 計算距離目標日期還有多少天
target_date = datetime.datetime.strftime("2024, 1, 1", "%Y-%m-%d")
now = datetime.datetime.now()
days_left = (target_date - now).days
print(days_left)
