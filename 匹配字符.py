import re
#原子：正则表达式中实现匹配的基本单位
#元字符：正则表达式中具有特殊意义的的字符

#以普通字符作为原子（匹配一个普通字符）
# a="湖南湖北广东广西湖北"
# pat="湖北"
# # data=re.search(pat,a)
# data=re.findall(pat,a)
# print("湖北出现的次数为：",len(data))

#匹配通用字符
# \w 任意字母/数字/下划线
# \W 和小写w相反
# \d 十进制数字
# \D 除了十进制数之外的数
# \s 空白字符
# \S 非空白字符

# b="185731448470"
# pat2="1\d\d\d\d\d\d\d\d\d\d"
# print(re.search(pat2,b))

# c="@@2%_f eahu_ingei@aon*feofnaeuhai"
# pat3=r"\W\w\w\s"
# print(re.search(pat3,c))

#匹配数字，中文，英文
# 数字[0-9]
# 英文[a-z][A-Z]
# 中文[\u4e00-\u9fa5]
# d="^^&^&%$%#%张三1848boy44jfijfna15inigjfia"
# pat1=r"[\u4e00-\u9fa5][\u4e00-\u9fa5]"
# pat2=r"[a-z][a-z][a-z]"
# pat3=r"[0-9][0-9]"
# result=re.search(pat1,d)
# result2=re.search(pat2,d)
# result3=re.search(pat3,d)
# print(result,result2,result3)