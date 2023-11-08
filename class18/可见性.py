class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
#__.name/__.age无法在对象直接使用，但是在类内的方法可以使用
    def study(self, course):
        print(f'{self.__name} is studying {course}')

stu1 = Student('tom', 20)

stu1.study('python')
#print(stu1.__name)

print(stu1._Student__name)