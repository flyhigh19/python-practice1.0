#requests模块
#使用pip工具下载  pip install requests
import requests

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400"}
wd={"wd":"中国"}
response=requests.get("http://www.baidu.com/s?",params=wd,headers=header).content.decode()
# response=requests.request("get","http://www.baidu.com").content.decode()
# data=response.text    #返回一个字符串形式的数据
# data=response.content  #返回一个二进制形式的数据   .decode重新返回一个字符串数据
print(response)
