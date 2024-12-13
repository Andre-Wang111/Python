# 成績系統
subjects = {}

while True:
    # 顯示目前的成績和功能清單
    print("\n目前的成績:")
    for subject, grade in subjects.items():
        print(f"{subject}: {grade}")

    print("\n功能清單:")
    print("1. 新增科目與成績")
    print("2. 刪除某個科目的成績")
    print("3. 提交所有成績並顯示平均")

    # 輸入選項
    choice = input("請輸入功能選項(1/2/3): ")

    if choice == "1":
        # 新增科目與成績
        subject = input("請輸入科目名稱: ")
        grade = input("請輸入成績: ")
        subjects[subject] = grade
        print(f"已新增: {subject} 的成績為 {grade}")

    elif choice == "2":
        # 刪除某個科目的成績
        subject = input("請輸入要刪除的科目名稱: ")
        if subject in subjects:
            del subjects[subject]
            print(f"已刪除: {subject} 的成績")
        else:
            print(f"科目 {subject} 不存在")

    elif choice == "3":
        # 提交所有成績並顯示平均
        if subjects:
            total = sum(float(grade) for grade in subjects.values())
            average = total / len(subjects)
            print(f"所有成績已提交，平均成績為: {average:.2f}")
        else:
            print("沒有成績可以提交")
        break

    else:
        print("無效的選項，請重新輸入")
