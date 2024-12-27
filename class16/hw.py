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

print("---------------------------------------------------------------------------- "
   

score_dict = {}


def show_score():
    for d, score in score_dict.items():
        print(f"{d}: {score}")
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均(會刪除所有成績)")


def add_score():
    subject = input("請輸入新增的科目: ")
    if subject in score_dict:
        print("此科目已經新增過了!")
    else:
        while True:
            try:
                score = int(input("請輸入分數: "))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")


def delete_score():
    subject = input("請輸入想刪除的科目: ")
    if subject in score_dict:
        score_dict.pop(subject)
        print("刪除成功!")
    else:
        print("此科目尚未新增!")


def show_average():
    if len(score_dict) == 0:
        print("目前沒有登記成績!")
    else:
        for subject, score in score_dict.items():
            print(f"{subject}: {score}")
        print(f"總平均為{sum(score_dict.values()) / len(score_dict)}")


while True:
    show_score()
    choice = input("請選擇功能編號: ")
    print("=================================")
    if choice == "1":
        add_score()
    elif choice == "2":
        delete_score()
    elif choice == "3":
        show_average()
        break
    else:
        print("查無此功能，請重新輸入")
