from bs4 import BeautifulSoup
import requests
import time
from multiprocessing import Process

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/61.0'
}

def get_url(url):
    res = requests.get(url)
    li = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        re = soup.find('div',class_='beautiful_pictures_show').find_all('li')
        for i in re:
            s = i.find('img').get('src')
            li.append(s)
    return li


def get_img(url):
    # url = 'http://pic.xiao4j.com/upload/meinv/2018_0816/144048869.jpg_270_410.jpg'
    # s = url.split('/')[-1].split('_')[0]
    # print(s)
    r = requests.get(url)
    if r.status_code == 200:
        print()
        with open(url.split('/')[-1].split('_')[0],'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    url = 'http://www.xiao4j.com/beauty/index.html'
    img_url = get_url(url)
    start = time.time()
    p_l = []
    for i in img_url:
        # get_img(i)
        p = Process(target=get_img,args=(i,))
        p.start()
        p_l.append(p)

    [i.join() for i in p_l]
    print(time.time() - start)