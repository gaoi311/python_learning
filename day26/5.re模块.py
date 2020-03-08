import re

# 字符串
# 匹配
# findall  *****
# ret = re.findall('\d+','19874ashfk01248')
# print(ret)  # 参数 返回值类型:列表 返回值个数:1 返回值内容:所有匹配上的项
# ret1 = re.findall('\s+','19874ashfk01248')
# print(ret1)
# search   *****
# ret2 = re.search('\d+','@$19874ashfk01248')
# print(ret2) #  返回值类型: 正则匹配结果的对象  返回值个数:1 如果匹配上了就返回对象
# if ret2:print(ret2.group()) # 返回的对象通过group来获取匹配到的第一个结果
# ret3 = re.search('\s+','19874ashfk01248')
# print(ret3) #  返回值类型: None   如果没有匹配上就是None
# match  **
# ret4 = re.match('\d+','19874ashfk01248')
# print(ret4)
# ret5 = re.match('\d+','%^19874ashfk01248')
# print(ret5)


# 替换 replace
# sub ***
# print('replace789,24utdeedeeeeshf'.replace('e','H',3))
# ret = re.sub('\d+','H','replace789nbc2xcz392zx')
# print(ret)
# ret = re.sub('\d+','H','replace789nbc2xcz392zx,48495',1)
# print(ret)
# subn ***
# ret = re.subn('\d+','H','replace789nbc2xcz392zx')
# print(ret)

# 切割
# split ***
# print('alex|83|'.split('|'))
# ret = re.split('\d+','alex83egon20taibai40')
# print(ret)

# 进阶方法 - 爬虫\自动化开发
# compile ***** 时间效率
# re.findall('-0\.\d+|-[1-9]+(\.\d+)?','alex83egon20taibai40')  --> python解释器能理解的代码 --> 执行代码
# ret = re.compile('-0\.\d+|-[1-9]\d+(\.\d+)?')
# res = ret.search('alex83egon-20taibai-40')
# print(res.group())
# 节省时间 : 只有在多次使用某一个相同的正则表达式的时候,这个compile才会帮助我们提高程序的效率

# finditer ***** 空间效率
# print(re.findall('\d','sjkhkdy982ufejwsh02yu93jfpwcmc'))
# ret = re.finditer('\d','sjkhkdy982ufejwsh02yu93jfpwcmc')
# for r in ret:
#     print(r.group())

