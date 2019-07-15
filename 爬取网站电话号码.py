import re
import requests
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400"}
response=requests.get("http://changyongdianhuahaoma.51240.com/",headers=header).text
# print(response.text)
pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
pat11=re.compile(pat1)
pat22=re.compile(pat2)
data1=pat11.findall(response)
data2=pat22.findall(response)
# print(data1)
# print(data2)
resultlist=[];
for i in range(0,len(data1)):
    resultlist.append(data1[i]+data2[i])
    print(resultlist[i])