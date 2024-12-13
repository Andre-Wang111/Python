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


"""
### 解釋選中的程式碼段落
這段程式碼是**功能 3**，負責提交所有成績並計算平均分。如果你是一名六年級學生，以下是詳細的解釋：

---

### 1. **`elif choice == "3":`**
   - 程式檢查使用者輸入的選項是否為「3」。
   - 如果是「3」，表示使用者選擇了「提交所有成績並顯示平均分」。

---

### 2. **`if subjects:`**
   - 程式檢查 `subjects` 字典是否有任何資料。
   - **為什麼要檢查？**  
     - 如果 `subjects` 是空的，代表還沒有任何成績，所以不能計算平均分。

---

### 3. **計算總分與平均分**
   - **`total = sum(float(grade) for grade in subjects.values())`**
     - 這段程式碼的作用是計算所有成績的總和：
       - **`subjects.values()`**：取得字典中的所有成績（例如：`[90, 80, 85]`）。
       - **`float(grade)`**：把每個成績轉換成浮點數（因為成績可能是字串，轉換後可以進行數學運算）。
       - **`sum()`**：將所有成績加總。
     - 例如：
       ```python
       subjects = {"數學": 90, "英文": 85, "科學": 80}
       total = sum(float(grade) for grade in subjects.values())
       # total = 90 + 85 + 80 = 255
       ```

   - **`average = total / len(subjects)`**
     - 計算平均分：
       - **`len(subjects)`**：計算字典中科目的數量（例如：3個科目）。
       - **`total / len(subjects)`**：用總分除以科目數量，得到平均分。
     - 例如：
       ```python
       average = 255 / 3  # 平均分是 85.0
       ```

---

### 4. **顯示結果**
   - **`print(f"所有成績已提交，平均成績為: {average:.2f}")`**
     - 這行程式碼會印出平均分，並格式化成兩位小數：
       ```python
       "所有成績已提交，平均成績為: 85.00"
       ```

---

### 5. **處理沒有成績的情況**
   - **`else:`**
     - 如果 `subjects` 是空的（沒有任何成績），程式會執行這段程式碼：
       ```python
       print("沒有成績可以提交")
       ```
       讓使用者知道沒有成績可供提交。

---

### 6. **結束程式**
   - **`break`**
     - 不管是否成功提交成績，只要執行了功能 3，程式就會跳出迴圈並結束。

---

### 用簡單的例子解釋
假設你新增了三個科目和成績：
```python
subjects = {"數學": "90", "英文": "85", "科學": "80"}
```

- 當你選擇功能 3 時：
  - 程式計算：
    ```python
    total = 90 + 85 + 80 = 255
    average = 255 / 3 = 85.0
    ```
  - 顯示結果：
    ```
    所有成績已提交，平均成績為: 85.00
    ```
  - 然後程式結束。

如果字典是空的（`subjects = {}`），程式會提示：
```
沒有成績可以提交
```

---

如果還有問題或需要進一步說明，隨時告訴我！😊
"""
