import configparser
# file类型
# f = open('setting')

# 有一种固定格式的配置文件
# 有一个对应的模块去帮你做这个文件的字符串处理

# settings.py 配置

# import configparser
#
# config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
#
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
#
# with open('example.ini', 'w') as f:
#    config.write(f)


import configparser

config = configparser.ConfigParser()
# print(config.sections())        #  []
config.read('example.ini')
# print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True
# print(config['bitbucket.org']["user"])  # hg
# print(config['DEFAULT']['Compression']) #yes
# print(config['topsecret.server.com']['ForwardX11'])  #no
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# print(config.get('bitbucket.org','compression')) # yes get方法Section下的key对应的value
