from urllib import request
import urllib
import re
#构建请求头
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400"}

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
key = input("请输入您要翻译的文字和网址：")
# key="中国"
#post请求需要提交的数据
formdata={
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15525407503951",
    "sign":"a47617b4c441b015d562abc5fea3f35d",
    "ts":"1552540750395",
    "bv":"4fd81d9d0040d9e81745dcc31af68bcb",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME",
    "typoResult":"false"
}
data=urllib.parse.urlencode(formdata).encode(encoding='utf-8')
req=request.Request(url,data=data,headers=header)
resp=request.urlopen(req).read().decode()
print(resp)  #json格式的数据
pat=r'"tgt":"(.*?)"}]]'         #r取消转义  .*?任意字符 "tgt":"和"}]中间的字符提取出来
result=re.findall(pat,resp)
print("翻译结果为："+result[0])


