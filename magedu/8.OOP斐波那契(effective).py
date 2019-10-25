
class Fib:

    def __init__(self):
        self.items = [0, 1]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        yield from self.items
        #return iter(self.items)

    def __getitem__(self, index):
        return self(index)

    def __call__(self, n):
        if n < 0:
            raise IndexError('index out of range')
        # elif self.n < 2:
        #     return self.items[self.n]
        else:
            lenght = len(self)
            for i in range(lenght, n + 1):
                item = self.items[i-1] + self.items[i-2]
                self.items.append(item)
            return self.items[n]


    def __str__(self):
        return str(self.items)

    __repr__ = __str__

f = Fib()
print(f(10))
print(len(f))
print('*******')
print(f[101])
print(len(f))
print(f)

# for i in enumerate(f):
#     print(i)


