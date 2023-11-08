class Student:

    def __init__(self, name ,age):
        self.name = name
        self.age = age

stu1 = Student('tom', 20)
stu1.sex = 'male'
#在定义后可以为对象添加属性
print(f'{stu1.name}: {stu1.age}: {stu1.sex}')