#数据获取和数据清洗一体html()
#数据获取与数据清洗分开 parse()
from lxml import etree
import requests
# #获取本地HTML文档
html=etree.parse(r"C:\Users\TH83762\Desktop\文件夹\爬虫\第2页.html")
# result=etree.tostring(html,encoding="utf-8").decode()
# print(result)

#获取某一类标签
# result=html.xpath("//span")   #获取所有span标签
# result=html.xpath("//a")
# print(result[0].text)     #获取span里面的值

#获取指定属性的标签
# result1=html.xpath("//li[@class='item-88']")
#获取li标签下的a标签
# result2=html.xpath("//li/a[@href='link2.html']")
# print(result2[0].text)

# 获取标签属性
# result1=html.xpath("//li/@class")
result1=html.xpath("//li/a//@href")
for i in result1:
    requests.get(i)
print(result1)
