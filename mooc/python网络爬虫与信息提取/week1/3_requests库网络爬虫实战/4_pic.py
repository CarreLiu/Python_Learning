import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/1121/20171121023827320.jpg"
root = "D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python网络爬虫与信息提取\\week1\\3_requests库网络爬虫实战\\"
path = root + url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")