import re
#conpile函数 ----正则表达式转换成内部格式，提高运行效率
# str="Python666java"
# pat1=r"\d+"
# pat2=re.compile(r"python",re.I)   #模式修正符（忽略大小写）****
# print(pat2.search(str))

# match函数---匹配开头位置  都是一次匹配
# search函数----匹配任意位置
# str="javapythonhtmljspython"
# pat1=re.compile(r"(p)ython",re.I)
# print(pat1.search(str).group())  #group 分组


#findall函数    列表中
#finditer()函数   迭代器  可以用for循环遍历出来
str="hello----hello-----hello-----hello----hello"
pat1=re.compile(r"hello")
# print(re.findall(pat1,str))
# list1=[];
# data=re.finditer(pat1,str)
# for i in data:
#     print(i.group())
#     list1.append(i.group())
# print(list1)

#split()函数   分隔
#sub()函数    替换
# str="张三,,,,李四,,,,,王五"
# pat1=re.compile(r",+")
# result=pat1.split(str)
#
# strr="hello123hello456!!"
# pat2=re.compile(r"\d+")
# result2=pat2.sub("666",strr)
# print(result2)