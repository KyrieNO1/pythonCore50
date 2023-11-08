class Student:

    def __init__(self, name ,age):
        self.name = name
        self.age = age

stu1 = Student('tom', 20)
stu1.sex = 'male'
print(f'{stu1.name}: {stu1.age}: {stu1.sex}')