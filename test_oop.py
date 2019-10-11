#-*-coding: UTF-8 -*-
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age=age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(23)
print(s.age)

s2 = Student()
#print(s2.name)

Student.set_age = set_age
s2 = Student()
s2.set_age(29)
print(s2.age)

class Student(object):
    __slots__ = ('name', 'age', 'score')

s = Student()
s.name = 'Michael'
s.age = '23'
print(s.name)
print(s.age)

s2 = Student()
s2.age = '30'
s2.name = 'Tom'
print(s2.age)
print(s2.name)

class Student1(Student):
    pass
s3 = Student1()
s3.age=45

s.score=222
print(s.score)

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 and 100')

        self._score = score

s =Student()
s.set_score(90)
print(s.get_score())

#s.set_score('900')

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 and 100')
        self._score=score

s = Student()
s.score=90
print(s.score)
#s.score=200
print(s.score)

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width*self._height

s = Screen()
s.width=10
s.height=20
print(s.width, s.height)
print(s.resolution)

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object name = %s' % self.name

    __repr__ = __str__
print(Student('Michael'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100:
            #mei bao cuo
            raise StopIteration()
        return self.a

    def __getitem__(self):
        return self.a

f = Fib()
# 报错
#print(f[:10])
# print(f[0])
# print(f[1])


# for i in Fib():
#     print(i)
