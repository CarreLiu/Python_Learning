#CrawJDPrice
import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url, hd):
    try:
        r = requests.request('POST', url, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        pprice = []
        pname = []
        soup = BeautifulSoup(html, 'html.parser')
        for p in soup.find_all('div', class_='p-price'):
            if p.i.string is not None:
                pprice.append(eval(p.i.string))
        for p in soup.find_all('div', class_='p-name'):
            if p.em.text is not None:   #使用p.em.string获取不出来，不知道为什么
                pname.append(p.em.text)
        for i in range(len(pprice)):
            ilt.append([pprice[i], pname[i]])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    hd = {'user-agent':'Mozilla/5.0'}
    goods = "书包"
    depth = 4
    start_url = "https://search.jd.com/Search?keyword=" + goods
    infoList = []
    for i in range(1,depth,2):
        try:
            url = start_url + "&enc=utf-8&page=" + str(i)
            html = getHTMLText(url, hd)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
main()
