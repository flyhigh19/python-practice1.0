from urllib import request
import urllib

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400",

    "Cookie":"BAIDUID=3DD6BB8DD8BBD2ACB30FD534DC4160B7:FG=1; BIDUPSID=3DD6BB8DD8BBD2ACB30FD534DC4160B7;\
PSTM=1540186448; MCITY=-158%3A; BDUSS=04ME9YckFzfm83a0hnfk1Zb1pDZFEwZjdWZW5yYXFwbGV2Qjl3M0NMR2x3eWxj\
QVFBQUFBJCQAAAAAAAAAAAEAAACJUSilAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAKU2AlylNgJcMU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; bdindexid=afaai2sohd6scstpfsmka\
53n00; H_PS_PSSID=1430_21091_28558_28607_28584_28640_26350_28603_28627_20719; BDRCVFR[feWj1Vr5u3D]=I67\
x6TjHwwYf0; PSINO=7; delPer=0; ZD_ENTRY=baidu; PHPSESSID=aibb0vae2u9salg184sqc1dak6; Hm_lvt_4010fd5075\
fcfe46a16ec4cb65e02f04=1552543819; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1552543819"
    }

url="http://i.baidu.com/"

req=request.Request(url,headers=header)
resp=request.urlopen(req).read().decode()
print(resp)  #json格式的数据
