import re
#原子表 定义一组平等的原子[3578]
# b="185731448470"
# pat2="1[3578]\d\d\d\d\d\d\d\d\d\d"
# print(re.search(pat2,b))

# c="fkoeagjaojgpythoniofjaifjiagnhvia"
# pat=r"py[abcdet]hon"
# print(re.search(pat,c))

#常用元字符....具有特殊含义的字符
# .匹配任意字符 （\n除外）
# ^匹配字符串开始位置   ^136
# $匹配字符串结束的位置    666$
# *重复0次1次多次前面的原子  \d*
# ?重复0次或一次前面的原子   \d?
# +重复一次或多次前面的原子  \d+

d="135252515681371213161515125485469"
pat1="..."
pat2="^135\d\d\d\d\d\d\d\d"
pat3=".*5469$"
pat4="8*"
pat5="8?"
pat6="81+"
print(re.search(pat6,d))
