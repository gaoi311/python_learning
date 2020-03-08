import re
# ret=re.findall(r"\d+(?:\.\d+)?","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)

# ret=re.findall(r"\d+(?:\.\d+)|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret.remove('')
# print(ret)

import re
# ret = re.findall('>(\w+)<',r'<a>wahaha<\a>')
# print(ret)

# ret = re.search(r'<(\w+)>(\w+)</(\w+)>',r'<a>wahaha</b>')
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))

# 分组命名
# ret = re.search("<(?P<name>\w+)>\w+</(?P=name)>","<h1>hello</h1>")
# print(ret.group('name'))  #结果 ：h1
# # print(ret.group())  #结果 ：<h1>hello</h1>
#
# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# print(ret.group(1))
# # print(ret.group())  #结果 ：<h1>hello</h1>

# ret = re.search(r'<(?P<tag>\w+)>(?P<c>\w+)</(\w+)>',r'<a>wahaha</b>')
# print(ret.group())
# print(ret.group('tag'))
# print(ret.group('c'))

# 正则指引
# python语言为基础 来讲解正则表达式
