"""
编写Python脚本，分析xx.log文件，按域名统计访问次数

xx.log文件内容如下：
https://www.sogo.com/ale.html
https://www.qq.com/3asd.html
https://www.sogo.com/teoans.html
https://www.bilibili.com/2
https://www.sogo.com/asd_sa.html
https://y.qq.com/
https://www.bilibili.com/1
https://dig.chouti.com/
https://www.bilibili.com/imd.html
https://www.bilibili.com/

脚本输出：
4 www.bilibili.com
3 www.sogo.com
1 www.qq.com
1 y.qq.com
1 dig.chouti.com
"""

import re
from collections import Counter

with open("xx.log") as f:
    data = f.read()

ym_list = re.findall(r'https://(.*?)/.*?', data)
ym_dict = dict(Counter(ym_list))
# 排序
print(ym_dict.items())

ret = sorted(ym_dict.items(), key=lambda x: x[1], reverse=True)
print(ret)
for i in ret:
    print(i[1], i[0])

# ----------------------------------------------
# import re
# dic = {}
# with open('xx.log') as f:
#     for i in f:
#         r = re.search('\w+.(\w+).com', i).group()
#         if r in dic:
#             dic[r].append(r)
#         else:
#             dic[r] = [r]
# for k, v in dic.items():
#     print('%s有%s个' % (k, len(v)))
#
#
# {
#     "www.sogo.com": ["www.sogo.com", "www.sogo.com"],
#     "www.bilibili.com": []
# }







