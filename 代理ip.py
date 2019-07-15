import requests
#设置IP地址
proxylist={
    "http":"http://144.48.109.161:8080",
    "https":"https://144.48.109.161:8080",
}
response=requests.get("http://www.baidu.com/",proxies=proxylist)
print(response.content.decode())