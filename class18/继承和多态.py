class Human:
    """人类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')
        
class Student(Human):
    """学生"""
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name} is studying {course_name}')
        
class Teacher(Human):
    """老师"""        
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def teach(self, course_name):
        print(f'{self.name} is teaching {course_name}') 
        
stu1 = Student('tom', 29)
teacher1 = Teacher('frank', 48)

stu1.eat()   
teacher1.sleep()
teacher1.teach('python')