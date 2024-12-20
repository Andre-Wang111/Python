score_dict = {}
while True:
    for subject, score in score_dict.items():
        print(f"{subject}: {score}")
    print("新增科目成績:")
    print("刪除科目成績:")
    print("提交所有科目成績並顯示平均分數:")
    choice = input("請輸入功能編號: ")
    print("====================================================================")

    if choice == "1":
        subject = input("請輸入想新增的科目: ")
        if subject in score_dict:
            print("科目已存在，請重新輸入")
        else:
            while True:
                try:
                    score = int(input("請輸入成績: "))
                    score_dict[subject] = score
                    break
                except:
                    print("輸入錯誤,請重新輸入")
    elif choice == "2":
        subject = input("請輸入要刪除的科目: ")
        if subject in score_dict:
            score_dict.pop(subject)
            print("科目已刪除")

    elif choice == "3":
        if len(score_dict) == 0:
            print("目前沒有科目成績")
        else:
            for subject, score in score_dict.items():
                print(f"{subject}: {score}")
            print(f"平均分數為:{sum(score_dict.values()) / len(score_dict)}")
        break

    else:
        print("查無此功能,請重新輸入")

    print("====================================================================")
