# 2.打印坐标
import random
class RandomInt:
    def __init__(self, totalnum, interval):
        self.totalnum = totalnum
        self.interval = interval

    def gene_int(self, lenght=5):
        remains = self.totalnum
        while 1:
            if remains < 0:
                break
            num = lenght if remains > 5 else remains
            for i in range(num):
                yield random.randint(self.interval[0], self.interval[1])
            remains -= lenght


# 2. 打印坐标方法2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

print(type(Point), type(Point.__class__), type(object), type(object.__class__), type(object.__class__.__base__), type(object.__base__))
# zip函数内部尽量不要放引用类型
#print(*[Point(x, y) for x, y in zip(RandomInt(10, (10, 20)).gene_int(), RandomInt(10, (10, 20)).gene_int())], sep='\n')

# 2.打印坐标方法3
from collections import namedtuple

Point = namedtuple('point', ('x', 'y'))

class PointRepr(Point):
    def __init__(self, x, y):
        super(PointRepr, self).__init__()
        # self.x = x
        # self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)


#print(PointRepr(1, 3))
#引用类型？？？
gene1 = RandomInt(10, (10, 20)).gene_int()
gene2 = RandomInt(10, (10, 20)).gene_int()
print([Point(x, y) for x, y in zip(gene1, gene2)])
print([PointRepr(x, y) for x, y in zip(RandomInt(10, (10, 20)).gene_int(), RandomInt(10, (10, 20)).gene_int())])

