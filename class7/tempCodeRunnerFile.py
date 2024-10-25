# 設定正確的密碼
correct_password = "your_password"  # 請在這裡替換為你的密碼

while True:
    # 請用戶輸入密碼
    user_input = input("請輸入密碼：")

    # 檢查密碼是否正確
    if user_input == correct_password:
        print("歡迎！你已成功進入系統。")
        break  # 退出循環
    else:
        print("密碼錯誤，請重新輸入。")
