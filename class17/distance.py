class Point:

    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    def distance_to(self, object):
        dx = self.x - object.x
        dy = self.y - object.y
        ditance = ((dx * dx) + (dy + dy)) ** 0.5
        return ditance

    def __str__(self):
        return f'({self.x}, {self.y})'

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# 创建 Point 对象
p1 = Point(x1, y1)
p2 = Point(x2, y2)

print(p1, p2)

distance = p1.distance_to(p2)
formantte_distance = f"{distance:.2f}"
print(f"Distance between p1 and p2: {formantte_distance}")
