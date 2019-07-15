#html-->xml
text='''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">张三</a></li>
        <li class="item-1"><a href="link2.html">李四</a></li>
        <li class="item-inactive"><a href="link3.html">王五</a></li>
        <li class="item-1"><a href="link4.html">赵六</a></li>
        <li class="item-0"><a href="link5.html">小七</a>
    </ul>
</div>
'''
from lxml import etree
#将字符串解析成特殊的HTMl对象
html=etree.HTML(text)
# print(type(html))
#将HTML转成字符串
result=etree.tostring(html,encoding="utf-8").decode()
print(result)