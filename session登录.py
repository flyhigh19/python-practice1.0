import requests

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400"}
#创建session登录
sess=requests.session()
#构造登录需要的参数
data={"u":"3490518913","p":"zhang27313"}
#通过传递用户名和密码得到cookie信息
sess.post("https://mail.qq.com/",data=data)
#请求需要的页面
response=sess.get("https://mail.qq.com/cgi-bin/frame_html?sid=aut6qL_VPDG6xhZK&r=91bf2a072587edf3ba4293e6553ea2f8")
print(response.text)