
def f(a=[]):
    a.append(3)
    print(a)
# 多次调用a中的内容追加，因为a是引用类型
# 类中的cars没有被清空，是因为只有在定义时初始化了一次

# 3.车辆信息
class CarInformation:
    cars = {}  # 只有在定义时被初始化了一次，
    # 在创建实例对象时没有被重新定义cars不会被清空，调用类时cars也不会被清空
    print(cars)
    def __init__(self, mark, color, price, speed):
        self._mark = mark
        self.price = price
        self.color = color
        self.speed = speed
        self.__configs = 'iidie999002'

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value

    @property
    def configs(self):
        return self.__configs

    @configs.setter
    def configs(self, values):
        self.__configs = values

    @classmethod
    def addCar(cls, objcar):
        onecar = objcar.__dict__
        onecar_info = {objcar.mark: onecar}
        __class__.cars.update(onecar_info)

    @classmethod
    def showCars(cls):
        print(__class__.cars)

CarInformation.addCar(CarInformation('特斯拉', '白色', '100万', '350km/h'))
CarInformation.showCars()

CarInformation.addCar(CarInformation('保时捷', '白色', '200万', '370km/h'))
CarInformation.showCars()

c = CarInformation(1, 2, '3', '4')
print('*****')
print(c.configs)
c.configs = '77899i'
print(c.configs)

print(c.mark)
c.mark = '77899i'
print(c.mark)


# 方法2
class Car:
    def __init__(self, mark, color, speed, price):
        self.mark = mark
        self.color = color
        self.speed = speed
        self.price = price

    def __repr__(self):
        return "name: {} speed:{}".format(self.mark, self.price)


class CarInfoMgr:  #  单一实例， 单一模式
    def __init__(self):
        self.info = []

    def addcar(self, car:Car):
        self.info.append(car)

    def getallcars(self):
        return self.info

# 全局唯一管理对象
mgr = CarInfoMgr()

c = Car('特斯拉', '白色', '100万', '350km/h')
mgr.addcar(c)

c = Car('保时捷', '白色', '200万', '370km/h')
mgr.addcar(c)

print(mgr.getallcars())
