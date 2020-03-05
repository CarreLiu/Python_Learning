#ex5.py
username = "Kate"
password = "666666"
for i in range(3):
    u = input()
    p = input()
    if username == u and password == p:
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")