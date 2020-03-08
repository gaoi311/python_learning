class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
a = A('alex',83)
aa = A('alex',83)
aa2 = A('alex',83)
aa3 = A('alex',83)
aa4 = A('alex',83)
aa5 = A('alex',83)
aa6 = A('alex',83)
print(a,aa)
print(aa3 == aa == aa4)  # ==这个语法 是完全和__eq__
