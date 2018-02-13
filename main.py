# -*- encoding:utf-8 -*-
from login import login_weibo as Login
from config import nickName
from config import pw
nickName = "15817603318"
pw = "woaiwdc**"

def my_main():
    Login(nickName, pw)
    print("登陆成功！")



if __name__ == '__main__':
    my_main()
