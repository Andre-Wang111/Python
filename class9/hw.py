"""
你製作了一台飲料機！這台飲料機有四個按鈕，每個按鈕都會給出不同的飲料：
蘋果汁 🍎
柳橙汁 🍊
葡萄汁 🍇
系統關閉 🔴
客人會按這些按鈕來選擇他們想要的飲料。
選擇後系統會告訴他們他們選了什麼飲料，但是，如果客人選擇了「系統關閉」，飲料機就會停止工作。
如果客人按錯了按鈕（也就是輸入了不正確的編號），你需要告訴他們「輸入錯誤查無此果汁，請重新輸入」。

範例（在終端機中）：
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:2
您點的商品是柳橙汁
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:3
您點的商品是葡萄汁
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:f
輸入錯誤查無此果汁，請重新輸入
1. 蘋果汁
2. 柳橙汁
3. 葡萄汁
4. 系統關閉
請輸入編號:4
~~系統關閉~~

"""

# 開始飲料機的運行
while True:
    # 顯示選單
    print("\n1. 蘋果汁 🍎")
    print("2. 柳橙汁 🍊")
    print("3. 葡萄汁 🍇")
    print("4. 系統關閉 🔴")

    # 讓使用者選擇
    choice = input("請輸入編號: ")

    # 根據選擇顯示結果或處理錯誤
    if choice == "1":
        print("您點的商品是蘋果汁")
    elif choice == "2":
        print("您點的商品是柳橙汁")
    elif choice == "3":
        print("您點的商品是葡萄汁")
    elif choice == "4":
        print("~~系統關閉~~")
        break  # 結束程式
    else:
        print("輸入錯誤查無此果汁，請重新輸入")


"""
1. while True:
這是一個迴圈，意思是程式會一直重複做某件事，直到你告訴它停止。在這裡，程式會一直讓你選擇飲料，直到你選擇「系統關閉」來停止。

2. print("\n1. 蘋果汁 🍎")
這一行是用來顯示選單的，print() 是顯示文字到螢幕上的方法。"\n" 是為了讓選單前面有一個空行，讓畫面看起來更清楚。

1. 蘋果汁 🍎 表示蘋果汁。
2. 柳橙汁 🍊 表示柳橙汁。
3. 葡萄汁 🍇 表示葡萄汁。
4. 系統關閉 🔴 表示關閉飲料機。
3. choice = input("請輸入編號: ")
這一行會要求你輸入你想選的飲料編號。input() 是讓你輸入文字的方法，程式會把你輸入的內容存到 choice 這個變數裡面。你輸入的是你選擇的編號，比如 1 表示蘋果汁，2 表示柳橙汁等等。

4. 使用 if 和 elif 來判斷：
這些是條件判斷語句，用來檢查你輸入的是什麼，然後決定要做什麼。

if choice == "1":：如果你輸入的是 1，程式就會顯示 "您點的商品是蘋果汁"。
elif choice == "2":：如果你輸入的是 2，程式就會顯示 "您點的商品是柳橙汁"。
elif choice == "3":：如果你輸入的是 3，程式就會顯示 "您點的商品是葡萄汁"。
elif choice == "4":：如果你輸入的是 4，程式會顯示 "系統關閉"，並且程式會停止。
5. else:
如果你輸入的不是 1、2、3 或 4，程式就會顯示 "輸入錯誤查無此果汁，請重新輸入"，提示你輸入錯誤，並讓你重新選擇。

6. break
當你選擇編號 4 來關閉系統時，程式會執行 break，這樣程式就會停止運行，跳出迴圈結束整個程序。

範例：
假設你在使用這台飲料機：

markdown
複製程式碼
1. 蘋果汁 🍎
2. 柳橙汁 🍊
3. 葡萄汁 🍇
4. 系統關閉 🔴
如果你輸入 2，程式會顯示：

複製程式碼
您點的商品是柳橙汁
如果你輸入 f（錯誤的選擇），程式會顯示：

複製程式碼
輸入錯誤查無此果汁，請重新輸入
如果你輸入 4，程式會顯示：

複製程式碼
~~系統關閉~~
這樣就完成了飲料機的選擇過程。程式會根據你選的編號來告訴你你選了什麼飲料，或者讓你重新選擇，直到你關閉系統。

簡單總結：
程式會問你想要喝什麼飲料。
你輸入數字來選擇飲料。
它會告訴你你選了什麼，或者提示你輸入錯誤。
如果你選擇關閉系統，程式就會停止運作。

"""