# test1.py

class A:
    def showmodule(self):
        print(1, self.__module__, self)
        print(2, self.__dict__)
        print(3, self.__class__.__dict__)
        print(4, self.__class__.__name__)


a = A()
a.showmodule()

