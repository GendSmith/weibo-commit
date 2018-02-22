
import re
import requests
import json
import time
#import pymongo
from config import *

def get_comment(url):
    wb_data = requests.get(url,headers=headers).text
    data_comment = json.loads(wb_data)
    print(url)
    try:
        datas = data_comment['data']['data']
        for data in datas:
            print('用户名：'+data['user']['screen_name'])
            print('评论：'+  re.compile(r'<[^>]+>',re.S).sub('', str( data['text']) ) )
            print('   ')
    except KeyError:
        print('发生了错误：' + KeyError)
        pass
