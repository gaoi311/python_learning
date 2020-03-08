# 正则表达式

# 作业
# exp = '3*5+2-3'
# atom_exp = '3*5'
# res = 15
# exp = exp.replace(str(res),atom_exp)

# 转义符
# print('\n')  # --> \\ \
# \ 是有特殊意义的
# 你看见了这个\ 不应该理解为这是一个'\',它是一个转义符
# 你想把这个转义符变成一个字符串'\',它必须经过转义
# '\\' 等于字符串数据类型的'\'
# '\\n'
# import re
# ret = re.search('\\\\n','\\n')
# print(ret)
# 如果一个字符串形式的'\'取消了它转义符的意思,就表示一个字符串'\'
# 那么就不需要再使用'\\'来表示'\'了
# 我们就在字符串前面加上一个r'',取消这个字符串中所有'\'的转义
# import re
# ret = re.search(r'\\n',r'\n')
# print(ret)

# 在测试的工具中,如果带了\,你又担心它会出现转义的情况
# 不管三七二十一,在测试工具里测好了的代码
# 拿到python中,统一放在字符串r''中就行了

# groups
# import re
# ret = re.search(r'\d+(\.\d)(\d)',r'1.23+2.3+3-4*5')
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.groups())

# split的问题
# import re
# ret3 = re.split('\d(\w)', '***1a***2b***3c**')
# print(ret3)
# ['', 'ashfk0248', '']
# print('aaa'.split('aaa'))

# import re
# ret = re.search('\d','123hhh')
# ret = re.search('\d+','123hhh')
# print(ret)

# import re
# a = re.findall(r'\\d',r'sajasd\d')
# a = re.findall('\\\\d','sajasd\\d')
# \d 转义符+d
# 转义符+d  没有特殊的意义
# 没转义
# '\'就应该是一个普通的'\'字符
# 所以python善良的帮你把你没转义的字符转义
# a1 = re.search(r'\\d',r'sajasd\d')
# print(a)
# print(a1.group())
