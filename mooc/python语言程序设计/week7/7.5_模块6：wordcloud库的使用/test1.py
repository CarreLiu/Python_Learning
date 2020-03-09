#test1.py
import wordcloud
txt = "life is short, you need python"
w = wordcloud.WordCloud()
w.generate(txt)
w.to_file("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\7.5_模块6：wordcloud库的使用\\pywcloud.png")