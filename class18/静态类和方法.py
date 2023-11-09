from math import pow

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边能否构成三角形"""
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        s = self.perimeter()/2
        return pow((s * (s - self.a) * (s - self.b) * (s - self.c)), 0.5)

abc = Triangle(37, 57, 78)

"""使用静态方法检验abc是否为三角形"""
validity = abc.is_valid(3, 5, 8)
print(validity)

print(f'三角形的周长是{abc.perimeter()}, 面积是{abc.area():.2f}')