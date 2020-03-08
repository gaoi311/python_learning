import random
# 随机 : 在某个范围内取到每一个值的概率是相同的
# 随机小数
# print(random.random())  # 0-1之内的随机小数
# print(random.uniform(1,5)) # 任意范围之内的随机小数

# 随机整数 *****
# print(random.randint(1,2)) # [1,2] 包含2在内的范围内随机取整数
# print(random.randrange(1,2)) # [1,2)不包含2在内的范围内随机取整数
# print(random.randrange(1,10,2)) # [1,10)不包含10在内的范围内随机取奇数

# 随机抽取
# 随机抽取一个值
# lst = [1,2,3,'aaa',('wahaha','qqxing')]
# ret = random.choice(l)
# print(ret)
# 随机抽取多个值
# ret = random.sample(lst,2)
# print(ret)

# 打乱顺序  在原列表的基础上做乱序
# lst = [1,2,3,'aaa',('wahaha','qqxing')]
# random.shuffle(lst)
# print(lst)

# 抽奖 \ 彩票 \发红包 \验证码 \洗牌

# 生成随机验证码
# 4位数字的
import random
# 0-9
# 基础版本
# code = ''
# for i in range(4):
#     num = random.randint(0,9)
#     code += str(num)
# print(code)

# 函数版本
# def rand_code(n=4):
#     code = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         code += str(num)
#     return code
#
# print(rand_code())
# print(rand_code(6))

# 6位 数字+字母
# print(chr(97))
# print(chr(122))
# import random

# 基础版
# code = ''
# for i in range(6):
#     rand_num = str(random.randint(0,9))
#     rand_alph = chr(random.randint(97,122))
#     rand_alph_upper = chr(random.randint(65,90))
#     atom_code = random.choice([rand_num,rand_alph,rand_alph_upper])
#     code += atom_code
# print(code)

# 函数版
# def rand_code(n=6):
#     code = ''
#     for i in range(n):
#         rand_num = str(random.randint(0,9))
#         rand_alph = chr(random.randint(97,122))
#         rand_alph_upper = chr(random.randint(65,90))
#         atom_code = random.choice([rand_num,rand_alph,rand_alph_upper])
#         code += atom_code
#     return code
#
# ret = rand_code()
# print(ret)

# 数字/数字+字母
# def rand_code(n=6 , alph_flag = True):
#     code = ''
#     for i in range(n):
#         rand_num = str(random.randint(0,9))
#         if alph_flag:
#             rand_alph = chr(random.randint(97,122))
#             rand_alph_upper = chr(random.randint(65,90))
#             rand_num = random.choice([rand_num,rand_alph,rand_alph_upper])
#         code += rand_num
#     return code
#
# ret = rand_code(n = 4)
# print(ret)

# ***** 永远不要创建一个和你知道的模块同名的文件名

#函数 : 发红包 : 200块钱 , 10个

