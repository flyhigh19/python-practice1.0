import requests
import re
import time

# 网易云音乐陈奕迅
# https://music.163.com/artist?id=2116
# 好听轻音乐第一页
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# 好听轻音乐第二页
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# 好听轻音乐第三页
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
# 歌曲信息列表的url
# http://www.htqyy.com/play/33
# 歌曲的资源所在的url
# http://f2.htqyy.com/play7/33/mp3/3
page=int(input("请输入您要爬取的好听轻音乐页数："))
songID=[]
songName=[]
for i in range(0,page):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    #获取音乐榜单的网页信息获取对应歌曲的id和name
    html=requests.get(url)
    strr=html.text
    #</span><span class="title"><a href="/play/62" target="play" title="月光下的凤尾竹" sid="62">月光下的凤尾竹</a></span>
    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'
    idlist=re.findall(pat2,strr)
    titlelist=re.findall(pat1,strr)
    songID.extend(idlist)       #将两个列表合成一个列表
    songName.extend(titlelist)
for i in range(0,len(songID)):
    songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/3"
    songname=songName[i]
    data=requests.get(songurl).content
    print("正在下载第",i+1,"首歌：",songName[i])
    with open("C:\\Users\\TH83762\\Desktop\\文件夹\\爬虫\\爬虫爬取的轻音乐music\\{}.mp3".format(songname),"wb")as f:
        f.write(data)
    time.sleep(0.5)
