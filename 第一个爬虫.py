import urllib.request
import urllib
import re
import random
#from urllib import request

#url=r"http://www.baidu.com/"
wd={"wd":"北京"}
url="http://www.baidu.com/s?"    #url 编码
#构造url 编码*********
wdcode=urllib.parse.urlencode(wd)
url=url+wdcode
# print(url)
#伪装PC机QQ浏览器/Android 华为Mate 10 Pro/vivo/火狐/360进行访问  注意分行时使用\(反斜线)进行上下连接
agent1="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400"
agent2="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00)\
AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
agent3="Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0\
Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools"
agent4="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0"
agent5="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
list1=[agent1,agent2,agent3,agent4,agent5]
agent=random.choice(list1)
#print(agent)**********      添加多个请求头通过随机数组短时间内多次进行访问而减少触发对应服务器的反爬机制
header={
"User-Agent":agent}    #字典(键值对)
#********创建自定义请求对象 除了URL之外的信息封装进去（cookie...）（可以通过伪装浏览器（参数：user-agent）进行访问）用来对抗服务器的反爬虫机制1（判断用户是否通过浏览器访问）
req=urllib.request.Request(url,headers=header)
#使用代理IP地址来访问http服务器
# proxylist=[
#     {"http":"189.194.48.154:33880"},
#     {"http":"111.90.179.182:8080"},
#     {"http":"144.48.109.161:8080"},
#     {"http":"103.255.30.34:3128"},
#     {"http":"170.38.16.175:80"}
# ]
# proxy=random.choice(proxylist)
# print(proxy)
#构建代理处理器对象
# proxyHandler=urllib.request.ProxyHandler(proxy)
#发送请求 获取响应信息读取  这里requset自动创建请求对象************
reponse=urllib.request.urlopen(url).read().decode()
#构建http处理器对象（专门处理http请求对象）
http_hander=urllib.request.HTTPHandler()
#urlopen是一个特殊的opener(不支持代理/cookie)  创建自定义opener对象调用open（）发送请求/（why use opener.open()）反爬虫机制2 代理：当使用同一台电脑进行多次访问时，对方服务器会记录你的IP地址
opener=urllib.request.build_opener(http_hander)
# opener=urllib.request.build_opener(proxyHandler)
# reponse=opener.open(req).read().decode()      #发送请求 获取响应
#将自定义的opener设置为全局变量，这样用urlopener发送的请求也会使用自定义的opener
urllib.request.install_opener(opener)
reponse=urllib.request.urlopen(req).read().decode() #解码--->编码（encode）爬取网页之后进行中文处理
#print(type(reponse))    #显示请求到的数据的类型（bytes 二进制/str 字符串）
#print(len(reponse))     #显示整个HTML的长度
#print(reponse)          #显示响应的HTML网页数据
pat=r"<title>(.*?)</title>"   #通过正则表达式进行简单的数据清洗（获取标题）
data=re.findall(pat,reponse)
print(data[0])      #findall有多个list列表信息
