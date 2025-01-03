"""
成績系統改寫作業 Score System Rewrite Assignment
--------------------------------------------

任務說明 (Task Description)：
請把成績系統的每個功能變成一個獨立的功能包，就像把工具分門別類放好一樣！
Please turn each feature of the score system into separate functions, just like organizing tools into different boxes!

需要製作的功能包 (Functions to Create)：
1. 新增功能 (Add Function):
   - def add: 幫我們加入新科目和分數
   - For adding new subject and score

2. 刪除功能 (Delete Function):
   - def delete: 可以刪掉不要的科目和分數
   - For removing subject and score

3. 離開功能 (Exit Function):
   - def exit: 結束程式並算出平均分數
   - For ending program and calculating average

完成方式 (How to Complete)：
- 要像積木一樣，把每個功能都組裝好
- Build each function like blocks
- 保持原本的操作方式不變
- Keep the same way of using the program
"""

def add():
    global score_dict
    subject = input("請輸入想新增的科目:")
    if subject in score_dict:
        print("此科目已經新增過囉!")
    else:
        while True:
            try:
                score = int(input("請輸入分數:"))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")


def delete():
    global score_dict
    subject = input("請輸入想刪除的科目:")
    if subject in score_dict:
        score_dict.pop(subject)
        print("刪除成功!")
    else:
        print("此科目尚未新增!")


def exit():
    global score_dict
    if len(score_dict) == 0:
        print("目前沒有登記成績喔!")
    else:
        for subject, score in score_dict.items():
            print(f"{subject}:{score}")
        print(f"總平均為:{sum(score_dict.values())/len(score_dict)}")


def edit():
    global score_dict
    subject = input("請輸入想修改的科目:")
    if subject in score_dict:
        while True:
            try:
                score = int(input("請輸入新的分數:"))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")
    else:
        print("此科目尚未新增!")


score_dict = {}
functions = [add, delete, edit, exit]

while True:
    for subject, score in score_dict.items():
        print(f"{subject}:{score}")
    for i in range(len(functions)):  # function=指令名稱
        print(f"{i + 1}. {functions[i].__name__}")  # 顯示指令名稱當作選項
    try:
        choice = int(input("請輸入功能編號:"))
        print("==========================")

        if 1 <= choice < len(functions):
            functions[choice - 1]()  # add() or delete()
        elif choice == len(functions):
            functions[choice - 1]()  # exit()
            break
        else:
            print("無效的選擇，請重新輸入")

    except:
        print("輸入錯誤，請輸入數字")

    print("==========================")


