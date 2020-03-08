# isinstance()  判断对象所属类型,包括继承关系
# issubclass()  判断类与类之间的继承关系

# class A:pass
# class B(A):pass
# b = B()
# print(isinstance(b,B)) #o,t
# print(isinstance(b,A)) #o,t
# l = list()
# print(l)  # type(l)
# class mystr(str):pass
# ms = mystr('alex')
# print(ms)
# print(type(ms) is str)  # 不包含继承关系,只管一层
# print(isinstance('alex',str)) # 包含所有的继承关系


# == 值相等        值运算
# is 内存地址相等  身份运算
# is要求更苛刻
    # 不仅要求值相等,还要求内存地址相同

a = 1111
b = 1111
print(a == b)
print(a is b)

# issubclass
# class A:pass
# class B(A):pass
# print(issubclass(B,A))
# print(issubclass(A,B))