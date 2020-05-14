a = 7
b = 4

print(a/b)  #除以
print(a//b)  #取整数部分
print(a%b)  #取余数

print(a**0.5)

print(3==1)
print(5>2)
print(3<=2)
print(8>=5)

a = 8
a +=3
print(a)

a**=2
print(a)

a**=3
print(a)

print(3<4 and 7>5)

# 字符串

a = "hello"
b = "world"

c = a +" "+ b
print(c)

d = a + "\n" + b
print(d)

d = a + "\n" + b
print(d)

d = a + "\n" + b
print(d)

print('hello\nworld')

print(r"hello\nworld")

print(a.index("llo"))
print(a.find("llo"))

print(a[1:])

print("{} {}!".format(a,b))
print("{} {}!".format(a,b))
print("{} {}!".format(a,b))

print(f"{a} {b}!")
print(f"{a} {b}!")
print(f"{a} {b}!")

# 控制语句
# 1、条件判断语句

a = True

if a:
    print("当前a = True")
else:
    print("当前a = False")

a = True

if a:
    print("当前a = True")
else:
    print("当前a = False")

b = 2

if b==0:
    print("当前b = 0")
elif b==1:
    print("当前b = 1")
else:
    print("当前b = 2")

# 2、循环控制语句

for i in range(10):
    print(i,end=" ")

for i in range(10):
    print(i )

a_list = [5, 6, 7, 9]
for a in a_list:
    print(a)

for i, a in enumerate(a_list):
    print(i,":",a)

for i, a in enumerate(a_list):
    print(i,":",a)

for i, a in enumerate(a_list):
    print(i,":",a)

b_dict = {"name":"zhang3", "sex":"男", "age":"28"}

for key, value in b_dict.items():
    print(key,":",value)

for f, g in b_dict.items():
    print(f,":",g)

# 循环中断命令
# continue：本次循环终止，继续下轮循环
# break：跳出循环，整个循环都不执行

for i in range(10):
    if i ==6:
        continue  #不打印6
    print(i)

for i in range(10):
    if i == 3:
        continue
    print(i, end=" ")
print("\n================")
for i in range(10):
    if i== 7:
        break
    print(i, end=" ")

# 列表推导式
print("\n==============")

d_list = [1,2,3,4,5]

f_list = [x * 2 for x in d_list]
print(f_list)

# 函数

def add(a, b):
    c = a + b
    return c

d = add(5, 8)
print(d)

# 模块
# import numpy as np

if __name__ == "__main__":
    d = add(5, 8)
    print(d)

# 符号重载

class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age

zhang3 = person("张三", 32)
li4 = person("李四", 45)
print(zhang3 + li4)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age

hih = Person("张",50)
jfk = Person("的",60)
print(hih + jfk)

# 矩阵 Matix

class Matix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        a_row = len(self.data)
        a_col = len(self.data[0])

        b_row = len(other.data)
        b_col = len(other.data[0])

        if a_row != b_row and a_col != b_col:
            return "形状不同， 不能相加"

        for row in range(a_row):
            for col in range(a_col):
                self.data[row][col] += other.data[row][col]

        return self

    def __str__(self):
        return str(self.data)

if __name__ == "__main__":

    a = Matix([[2,3],[4,5]])
    b = Matix([[5,6],[8,9]])
    print(a + b)