import re
#匹配固定数字
#{n}前面的原子出现了n次
#{n,}至少出现了n次
#{n,m}出现次数介于n-m之间
a="23a4f65415148a"
pat1=r"\d{8,10}"
print(re.search(pat1,a))