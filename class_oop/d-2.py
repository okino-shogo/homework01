import math


class Rectangle:
    def __init__(self, height, width):
        # 属性OK
        self.height = height
        self.width = width

    # 面積  {:.2f}で小数点二桁まで表示できる
    def area(self):
        return f"{self.height * self.width:.2f}"

    # 対角線
    def diagonal(self):
        return f"{(math.sqrt(self.height ** 2 + self.width ** 2)):.2f}"


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
