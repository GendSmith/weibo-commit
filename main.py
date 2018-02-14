# -*- encoding:utf-8 -*-
from login import login_weibo as Login
from spider import spider_weibo as Spider
from config import nickName
from config import pw
from config import url

def my_main():
    Login(nickName, pw)
    print("登陆成功！")
    Spider(url)
    print("爬虫成功")



if __name__ == '__main__':
    my_main()
