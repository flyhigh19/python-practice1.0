import urllib
import urllib.request
import time
#根据url发送请求 获取服务器响应文件
def loadPage(url,filename):
    print("正在下载 "+filename)
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    request = urllib.request.Request(url, headers=header)  #使用360浏览器进行url请求
    return urllib.request.urlopen(request).read()   #获取HTML页面内容
#将HTML内容写入本地
def writePage(html,filename):
    print("正在保存 " + filename)
    #文件写入
    with open(filename,"wb")as f:
        f.write(html)
    print("保存成功")
    print("-----------------------")
#处理每个界面的url
def tiebaSpider(url,beginPage,endPage):
    for(page)in range(beginPage,endPage+1):
        pn=(page-1)*50
        filename="//飞奔的嗨少/Users/TH83762/Desktop/文件夹/爬虫/第"+str(page)+"页.html"  #每次请求后的保存的文件名
        fullurl=url+"&pn="+str(pn)     #每次请求完整的url
        #print fullurl
        html=loadPage(fullurl,filename)  #采用爬虫爬取网页
        #print(html)
        writePage(html,filename)    #把爬取到的网页信息写入本地

if __name__ == '__main__':
    kw=input("请输入需要爬取的贴吧关键字：")
    beginPage=int(input("请输入起始页："))
    endPage = int(input("请输入结束页："))
    url="http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    fullurl=url+key
    tiebaSpider(fullurl,beginPage,endPage)

time.sleep(6)