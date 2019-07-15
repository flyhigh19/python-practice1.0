import re
import urllib.request
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400"}

url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=40"
req=urllib.request.Request(url,headers=header)
data=urllib.request.urlopen(req).read().decode()
# print(data)
pat1=r'"rating":\["(.*?)","\d+"\]'
pat2=r'"title":"(.*?)"'
patter1=re.compile(pat1,re.I)
patter2=re.compile(pat2,re.I)
data1=patter1.findall(data)
data2=patter2.findall(data)
# print(data1)
# print(data2)
for i in range(0,len(data1)):
    print("排名：",i+1," 电影名：",data2[i],"  豆瓣评分",data1[i])