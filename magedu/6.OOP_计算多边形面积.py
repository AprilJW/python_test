import math
import json

class Area:
    def __init__(self, *args):
        self.lenght = len(args)
        self.args = args

    def numsides(self):
        if self.lenght == 3:
            return self._triangle(*self.args)
        elif self.lenght == 2:
            return self._quadrangle(*self.args)
        elif self.lenght == 1:
            return self._circle(*self.args)
        else:
            pass

    def _circle(self, r):
        return math.pi * (r**2)

    def _triangle(self, a, b, c):
        p = (a + b + c) /2
        return p / (p * (p - a) * (p - b) * (p - c))**(1/2)

    def _quadrangle(self, a, b):
        return (a * b)


class Triangel(Area):
    pass

print(Triangel(2, 2, 2).numsides())

class Quadrangle(Area):
    pass

print(Quadrangle(2, 2).numsides())

# #给圆增加可序列化功能，方法1，在子类中添加
# class Circle(Area):
#     def __init__(self, r):
#         super().__init__(r)
#         self.r = r
#
#     def to_json(self):
#         r_area_mapping = {}
#         r_area_mapping[self.r] = self.numsides()
#         return json.dumps(r_area_mapping)
#
#     def from_json(self):
#         return json.loads(self.to_json())

# #给圆增加可序列化功能，方法2，多继承
#
# class Json:
#     def to_json(self):
#         r_area_mapping = {}
#         r_area_mapping[self.r] = self.numsides()
#         return json.dumps(r_area_mapping)
#
#     def from_json(self):
#         return json.loads(self.to_json())
#
# class Circle(Area, Json):
#     def __init__(self, r):
#         super().__init__(r)
#         self.r = r



#给圆增加可序列化功能，方法3，装饰器

def to_json(cls):
    def to_json(self):
        r_area_mapping = {}
        r_area_mapping[self.r] = self.numsides()
        return json.dumps(r_area_mapping)
    cls.to_json = to_json
    return cls

def from_json(cls):
    def from_json(self):
        return json.loads(self.to_json())
    cls.from_json = from_json
    return cls

@to_json
@from_json
class Circle(Area):
    def __init__(self, r):
        super().__init__(r)
        self.r = r

print(Circle(2).to_json())
print(Circle(2).from_json())