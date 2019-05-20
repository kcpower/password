defined_pw = "a123456"
i = 1 
while i <= 3:
    input_pw = input("請輸入你的密碼:")
    if input_pw == defined_pw:
        print("輸入正確. 歡迎光臨 !")
        break 
    if i == 3:
        print("嘗試次數達到極限. 再見!")  
        break     
    else:
        print("𨍽入錯誤. 再試一次! 還有", 3 - i, "次機會!")
        i = i + 1
    