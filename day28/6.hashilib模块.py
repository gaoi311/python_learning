# 摘要算法的模块
import hashlib
# 能够把 一个 字符串 数据类型的变量
# 转换成一个 定长的 密文的 字符串,字符串里的每一个字符都是一个十六进制数字

# 对于同一个字符串,不管这个字符串有多长,只要是相同的,
# 无论在任何环境下,多少次执行,在任何语言中
# 使用相同的算法\相同的手段得到的结果永远是相同的
# 只要不是相同的字符串,得到的结果一定不同

# 登录的密文验证
# 'alex3714'  # -> '127649364964908724afd'

# 字符串 --> 密文
# 密文 不可逆的 字符串

# 1234567 - > '127649364964908724afd'
# 算法 : 对于同一个字符串,用相同的算法,相同的手段去进行摘要,获得的值总是相同的
# 1234567 - > '127649364964908724afd'


# s1 = 'alex3714'  # aee949757a2e698417463d47acac93df
# s2 = 'alex3714qwghkdblkasjbvkhoufyowhdjlbvjnjxc'  # d2d087c10aeba8276b21f8697ad3e810
# md5是一个算法,32位的字符串,每个字符都是一个十六进制
# md5算法 效率快 算法相对简单
# md5_obj = hashlib.md5()
# md5_obj.update(s1.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res,len(res),type(res))

# 数据库 - 撞库
# 111111 --> 结果
# 666666
# 123456
# alex3714 --> aee949757a2e698417463d47acac93df

# s1 = '123456'
# md5_obj = hashlib.md5()
# md5_obj.update(s1.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res,len(res),type(res))

# 加盐  # alex3714  d3cefe8cdd566977ec41566f1f11abd9
# md5_obj = hashlib.md5('任意的字符串作为盐'.encode('utf-8'))
# md5_obj.update(s1.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res,len(res),type(res))
# ales登录 alex3714|d3cefe8cdd566977ec41566f1f11abd9


# alex|d3cefe8cdd566977ec41566f1f11abd9
# 张三|d3cefe8cdd566977ec41566f1f11abd8  123456
# 鞠莹莹|d3cefe8cdd566977ec41566f1f11abd8 123456

# 恶意用户 注册500个账号
# 张三|123456  '任意的字符串作为盐'.encode('utf-8') d3cefe8cdd566977ec41566f1f11abd8
# 李四|111111
# eee|alex3714

# 动态加盐
# username = input('username : ')
# passwd = input('password : ')
# md5obj = hashlib.md5(username.encode('utf-8'))
# md5obj.update(passwd.encode('utf-8'))
# print(md5obj.hexdigest())
# ee838c58e5bb3c9e687065edd0ec454f


# sha1也是一个算法,40位的字符串,每个字符都是一个十六进制
# 算法相对复杂 计算速度也慢
# md5_obj = hashlib.sha1()
# md5_obj.update(s1.encode('utf-8'))
# res = md5_obj.hexdigest()
# print(res,len(res),type(res))


# 文件的一致性校验
# md5_obj = hashlib.md5()
# with open('5.序列化模块_shelve.py','rb') as f:
#     md5_obj.update(f.read())
#     ret1 = md5_obj.hexdigest()
#
# md5_obj = hashlib.md5()
# with open('5.序列化模块_shelve.py.bak','rb') as f:
#     md5_obj.update(f.read())
#     ret2 = md5_obj.hexdigest()
# print(ret1,ret2)

# 如果这个文件特别大,内存装不下
# 8g 10g
# 按行读  文本 视频 音乐 图片 bytes
# 按字节读 23724873 10240

# md5_obj = hashlib.md5()
# md5_obj.update('hello,alex,sb'.encode('utf-8'))
# print(md5_obj.hexdigest())

# md5_obj = hashlib.md5()
# md5_obj.update('hello,'.encode('utf-8'))
# md5_obj.update('alex,'.encode('utf-8'))
# md5_obj.update('sb'.encode('utf-8'))
# print(md5_obj.hexdigest())

# 大文件的已执行校验

md5_obj = hashlib.md5()
with open('5.序列化模块_shelve.py.bak','rb') as f:
    md5_obj.update(f.read())
    # 循环 循环的读取文件内容
    # 循环的来update
print(md5_obj.hexdigest())

# 写成一个函数
# 参数 : 文件1的路径,文件2的路径,默认参数 = 1024000
# 计算这两个文件的md5值
# 返回它们的一致性结果 T/F


