class Fib:

    def __init__(self, n):
        self.n = n
        self.calculate_n()

    def calculate_n(self):
        if self.n <= 0:
            return
        elif self.n < 3:
            return 1
        else:
            return self.calculate_fib()

    def calculate_fib(self):
        k1 = 1
        k2 = 1
        k = 2
        while k < self.n:
            k1, k2 = k2, k1 + k2
            k += 1
        return k2

    def iteritems(self):
        k1 = 1
        k2 = 1
        k = 1
        while k <= self.n:
            yield k1
            k1, k2 = k2, k1 + k2
            k += 1

    def __iter__(self):
        return self.iteritems()

    def __call__(self):
        return 'result: {}'.format(self.calculate_n())

    def __len__(self):
        count = 0
        for i in iter(self):
            count += 1
        return count

    def getvaluefromindex(self):
        itemlist = []
        for i in iter(self):
            itemlist.append(i)
        return itemlist

    def __index__(self):
        itemlist = []
        for i in iter(self):
            itemlist.append(i)
        return itemlist




f = Fib(101)
print(f())

# for i in iter(f):
#     print(i)

print(len(f))
print(f.getvaluefromindex()[100])