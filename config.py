#登录账号密码
nickName = "***"
pw = "***"

#某条评论的URL
url = "https://m.weibo.cn/api/comments/show?id=4190294654043937&page="

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'***',
    'Host':'m.weibo.cn',
    #'Referer':'https://m.weibo.cn/status/4190294654043937',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

pageNum = 20
