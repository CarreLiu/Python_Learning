#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\7.6_实例12：政府工作报告词云\\新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\7.6_实例12：政府工作报告词云\\grwordcloud.png")