# 函式(function) - 就像是一個神奇工具箱，裡面可以放入我們常常使用的指令


# 函式名稱後面一定要加上小括號()，並且記得加上冒號:
def say_hello():
    print("Hello! I'm a Andre!")
    print("Nice to meet you!")


say_hello()  # 呼叫函式


# 函式可以接收資料 (參數) - 參數就像是函式的原料，可以放入不同的值來得到不同的結果
def say_hello_with_name(name):
    print(f"Hello {name}!")
    print("Nice to meet you!")


say_hello_with_name("Andre")


# 函式可以有預設值 - 如果不給參數值，就會使用預設的值
def say_hello_with_default(name="Andre"):
    print(f"Hello {name}!")
    print("Nice to meet you!")


say_hello_with_default()  # 使用預設值
say_hello_with_default("Andre")  # 使用新的值


# 區域變數與全域變數 - imagine 家裡and學校的toy
# 區域變數is you personal toy, only you can play with it
# 全域變數is everyone's toy, everyone can play with it
toy_name = "toy bear"  # 全域變數 , everyone can play with it


def play_with_toy():
    toy_name = "Lego"  # 區域變數 , only you can play with it
    print(f"I'm playing with {toy_name}")


def share_toy():
    global toy_name  # 告訴 Python 我要使用everone's toy
    toy_name = "block"
    print(f"I'm sharing {toy_name}")
