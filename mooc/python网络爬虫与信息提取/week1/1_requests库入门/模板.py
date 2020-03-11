import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

url = "http://www.baidu.com"
urll = "https://item.jd.com/100000287145.html"
print(getHTMLText(urll))