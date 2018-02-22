# -*- encoding:utf-8 -*-
from spider import *
from config import *

def my_main():
    for i in range(1,pageNum):
        real_url = url + str(i)
        get_comment(real_url)
        #time.sleep(2)


if __name__ == '__main__':
    my_main()
