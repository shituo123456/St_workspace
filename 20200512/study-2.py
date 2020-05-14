
#1、变量与类型
# 变量类型：数字（整形，浮点），布尔型，字符串，集合（列表，数组，元组，字典），类别（需要我们自己定义）

a = "shishis"
b = True
c = 1.5
e = 3
print(type(b))

class Person:
    pass

d = Person()

# print("=*10")

# list  可以增加 删除 查找
a = [1,2,3,4]
print(a)
print(len(a))
print(a[3])

a[2] = 2
print(a)

a.remove(a[2])
print(a)

a.append(7)
print(a)

a.insert(1,6)
print(a)

a.extend([2,8])
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.clear()
print(a)

a.extend([8])
print(a)

a.extend([8,9,10,4,6,3,2])
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.insert(3,7)
print(a)

a.append(8)
print(a)

print(a.index(7))

a.remove(7)
print(a)

a.remove(a[7])
print(a)


# # 元组tuple,不允许修改
# a = (1,2,3)

a = (1,5,8,3,6)
print(len(a))

print(a[0])

print(a.index(8))
# # set  没有顺序，和索引有关的操作都会报错
a = {1,2,3,8,2,2,3}
print(a)

a.remove(3)
print(a)

a.add(8)
print(a)

# 字典
a = {"name":"zhang3","sex":"男","年龄":"28"}

a["name"] ="li4"
print(a)

print(len(a))

a.pop("年龄")
print(a)

a = [[1,2],[3,4],[5,6],[7,8]]
print(a[0])

print(a[2][1])

print(a[1:])

print(a[:3])

print(a[::2])

print(a[1:4:2])

print(a[::-1])

print(a[-1:1:-1])

b = 8.6
b = int(b)
print(b)

c = [1,1,1,2,2,2]
print(type(c))
print(list(set(c)))




