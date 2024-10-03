import random
import time
right_password = str(input("输入你的6位银行卡密码:")) 
start = time.time()
index = len(right_password)
if index == 6:
    for i in right_password:
        if ord(i) >= 48 and ord(i) <= 57:
            while True:
                a = random.randint(0,9)
                b = random.randint(0,9)
                c = random.randint(0,9)
                d = random.randint(0,9)
                e = random.randint(0,9)
                f = random.randint(0,9)
                result = f"{a}{b}{c}{d}{e}{f}"
                if result == str(right_password):
                    print(f"Password is {result}")
                    print(f"密码破译用时（秒）: {time.time() - start}")
                    break
            break    
        else:
            print("输入错误，请重新输入！")
            break
else:
    print("输入错误，请重新输入！")
    