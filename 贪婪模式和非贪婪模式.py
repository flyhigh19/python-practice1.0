#贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
#非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配
#python里面默认是贪婪的
import re
str='aa<div>test1</div>bb<div>test2</div>'
pat1=r"<div>.*?</div>"  #非贪婪模式
pat2=r"<div>.*</div>"   #贪婪模式
print(re.findall(pat1,str))