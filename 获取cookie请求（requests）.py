import requests
response=requests.get("http://www.baidu.com")
#获取返回的cookiejar对象
cookiejar=response.cookies
#将cookie转换成字典
cookiedict=requests.utils.dict_from_cookiejar(cookiejar)
print(cookiejar)
print(cookiedict)