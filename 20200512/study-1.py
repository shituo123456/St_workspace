class Person:
    pass

p = Person()

class Cat:
    pass

c = Cat()

class Person:
    def say(self, content):
        print(content)

zhang3 = Person()
zhang3.say("你好")

li4 = Person()
li4.say("你好")

class Person:
    def get(self,obj):
        return obj

zhang3 = Person()
print(zhang3.get("5元"))

# 构造函数   功能：对象创建的时候会自动执行

class Person:

    def __init__(self):
        print("我爱小黄")

p = Person()

class Person:

    def __init__(self):
        print("我爱宝宝")

p = Person()

class Person:

    def __init__(self):
        print("我爱宝宝")

p = Person()

# call行为    功能：调用的时候直接使用（）调用

class Person:

    def __call__(self):
        print("调用call行为")

zhang3 = Person()
zhang3()

class Person:
    def __call__(self):
        print("调用啊")

li4 = Person()
li4()

# 属性：1.类之间有共同的属性 2.属性可以被读取和修改

class Person:
    def __init__(self, name):
        self.name = name
        self.height = 1.74
        self.sex = "男"

    def show(self):
        print(self.name)
        print(self.height)
        print(self.sex)

p = Person("石拓")
p.show()

p.name = "小黄"
print(p.name)

class Person:
    def __init__(self, name):
        self.name = name
        self.height = 1.75
        self.sex = "男"

    # def show(self):
        print(self.name)
        print(self.height)
        print(self.sex)

p = Person("石拓")
# p.show()

p.height = 1.74
print(p.height)


# 继承 1、类是可以继承的   2、继承的类也可以继承父类的行为和属性

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

cat1 = Cat("小黄")
cat1.show()

class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

class cat(Animal):
    def __init__(self, name):
        super().__init__(name)

c = cat("小黄2")
c.show()

class Aniaml:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)

class cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)

class cat(Animal):
    def __init__(self, name):
        super().__init__(name)

c = cat("小黄3")
c.show()

class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)

class dog(Animal):
    def __init__(self, name):
        super().__init__(name)

d = dog("xiaoahung 4")
d.show()

# 组合  1、类之间存在组合关系；2、可以把对象定义为属性的方式来组合类之间的关系

class Eye:
    def __init__(self, color):
        self.color = color

class Person:
    def __init__(self, eye):
        self.eye = eye

    def show(self):
        print(self.eye.color)

eye = Eye("黑色")
p = Person(eye)
p.show()

class Eye:
    def __init__(self, color):
        self.color = color

class Person:
    def __init__(self, eye):
        self.eye = eye

    def show(self):
        print(self.eye)

eye = Eye("黑色2")
p = Person(eye)
p.show()