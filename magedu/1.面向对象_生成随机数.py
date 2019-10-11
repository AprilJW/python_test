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

r1 = RandomInt(6, [1, 10])
print(type(r1.gene_int()))
print(list(r1.gene_int()))

# 方法2
class RandomGen:
    def __init__(self, start=1, stop=100, count=10):
        self.start = start
        self.stop = stop
        self.__count = count
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.start, self.stop) for i in range(self.__count)]

    def generate(self):
        return next(self._gen)

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

r = RandomGen()
print(r.generate())
r.count = 3
print(r.generate())

# 方法3
class RandomGen:
    def __init__(self, start=1, stop=100, count=10):
        self.start = start
        self.stop = stop
        self.__count = count
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield random.randint(self.start, self.stop)

    def generate(self, count=0):
        count = self.count if count <= 0 else count
        return [next(self._gen) for i in range(count)]

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

r = RandomGen()
print(r.generate())
r.count = 3
print(r.generate())


#方法4
class RandomGen:
    @classmethod # 当工具使用，所以用类方法
    def generate(cls, start=1, stop=100, count=7):
        return [random.randint(start, stop) for i in range(count)]

print(RandomGen.generate())