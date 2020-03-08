# ret=re.compile('-0\.\d+|-[1-9]\d*(\.\d+)?')
# c=ret.search('-1asdada-200')
# print(c.group())
# c1=ret.findall('-1asdada-200')
# print(c1)

import re
# ret = re.findall('-0\.\d+|-[1-9]\d*(\.\d+)?','-1asdada-200')
# print(ret)
# ret = re.findall('www.baidu.com|www.oldboy.com','www.oldboy.com')
# print(ret)
# ret = re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')
# print(ret)

# ret = re.findall('-0\.\d+|-[1-9]\d*(?:\.\d+)?','-1asdada-200')
# print(ret)

# ret = re.split('\d+','alex83egon20taibai40')
# print(ret)
# ret = re.split('(\d+)','alex83egon20taibai40')
# print(ret)

# 分组遇见search
# ret = re.search('\d+(.\d+)(.\d+)(.\d+)?','1.2.3.4-2*(60+(-40.35/5)-(-4*3))')
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))