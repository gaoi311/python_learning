import re
from urllib.request import urlopen
# 内置的包 来获取网页的源代码 字符串
# res = urlopen('http://www.cnblogs.com/Eva-J/articles/7228075.html')
# print(res.read().decode('utf-8'))

def getPage(url):
    response = urlopen(url)
    return response.read().decode('utf-8')

def parsePage(s):   # s 网页源码
    ret = com.finditer(s)
    for i in ret:
        ret = {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num")
        }
        yield ret

def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num  # 0
    response_html = getPage(url)   # response_html是这个网页的源码 str
    ret = parsePage(response_html) # 生成器
    print(ret)
    f = open("move_info7", "a", encoding="utf8")
    for obj in ret:
        print(obj)
        data = str(obj)
        f.write(data + "\n")
    f.close()

com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)
count = 0
for i in range(10):
    main(count)  # count = 0
    count += 25