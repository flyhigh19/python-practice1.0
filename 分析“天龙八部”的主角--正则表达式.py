import re
with open(r"C:\Users\TH83762\Desktop\天龙八部.txt","rb")as f:
    data=f.read().decode()
print(data)
pat1="乔峰"
pat2="萧峰"
pat3="段誉"
pat4="虚竹"

n1=re.findall(pat1,data)
n2=re.findall(pat2,data)
n3=re.findall(pat3,data)
n4=re.findall(pat4,data)

print("乔峰出现的次数：",len(n1)+len(n2),"段誉出现的次数：",len(n3),"虚竹出现的次数：",len(n4))