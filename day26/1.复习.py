# 正则表达式
# 作用 : 一种匹配字符串的规则
# 应用 : 登录注册的表单验证
        #爬虫 自动化开发 日志分析

# 元字符
    # [] [^]  个性化的定制,
        # [1-9]下面这一组无法描述的一般用上面字符组的形式
        # [\d\s]一个特殊元字符无法描述一个字符内出现的内容了
    # \d \D \w \W \s \S \t \n
    # .  匹配除了换行符之外的所有字符 爬虫容易用,表单不容易用
    # ^ $
    # | ()
# 量词
    # *  0-n
    # +  1-n
    # ?  0-1
    #{n},{n,},{n,m}
# 其他知识 :
    # 贪婪匹配 - 回溯算法
    # 量词? - 惰性匹配

# 1、匹配任意长度的正整数   [1-9]\d*
# 2、匹配小数  -?\d+\.\d+
# 3、匹配整数或者小数
    # -?\d+\.?\d*    有缺陷 1. 2.这样的内容都能被匹配上
    # -?\d+\.?\d+    有缺陷 1 2 这样的一位数都匹配不上了
    # -?\d+(\.\d+)?  准确的
# 4、匹配负数  -0\.\d+|-[1-9]\d+(\.\d+)?
# 5、匹配qq号 [1-9]\d{4,11}
# 6、匹配长度为11位的电话号码 1[3-9]\d{9}
# 7、长度为8-10位的用户密码 ： 包含数字字母下划线和?@
    # [\w@?]{8,10}
# 8、匹配验证码：4位数字字母组成的
    # [\da-zA-Z]{4}

# 9、从类似
# <a>wahaha<\a>
# <b>banana<\b>
# <h1>qqxing<h1>
# <script>salkdjgh<\script>
# 这样的字符串中，
# 1）匹配出wahaha，banana，qqxing内容。 >\w+<
# 2）匹配出a,b,h1这样的内容 <\w+>

# 10、1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 从上面算式中匹配出最内层的小括号
# (-40/5)(9-2*5/3+7/3*99/4*2998+10*568/14)(-4*3)(16-3*2)
    # \([\d\.+\-*/]+\)
    # \([^()]+\)
