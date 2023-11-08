class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course):
        print(f'{self.__name} is studying {course}')

stu1 = Student('tom', 20)

stu1.study('python')
#print(stu1.__name)
print(stu1._Student__name)