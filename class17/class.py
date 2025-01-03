a = [ "a", "b", "c" ]
b = a
b[0] = "d"
print(a)   # 顯示 ["d", "b", "c"]



a = 10
b = a
b = 20
print(a)   # 顯示 10



# def doc 用途
def add(a, b):
    """

    加法函式
    :param a: 數字1
    :param b: 數字2
    :return:  a+b

    """
    return a + b



# use help 函式可以查看函式的說明文件
help(add)


# use_doc_屬性也可以查看函式的說明文件
print(add.__doc__)
print(add.__name__)


# eval(input()) - 這個函式可以讓使用者輸入的文字變成程式碼執行
ans = eval(" 5 + 3 ")
print(ans)


# 這樣就可以讓 user 輸入數學運算式，然後計算結果
ans = eval(input("請輸入數學運算式:"))
print(ans)
# 如果輸入:
# 5 + 3
# 顯示8