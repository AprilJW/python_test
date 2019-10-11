# 5. 模拟购物车购物
class Color:
    YELLOW = 0
    RED = 1
    BLUE = 2
    WHITE = 3

class Item:
    def __init__(self, name, price, **kwargs): #kwargs用来收集一些无关紧要的关键字参数
        self.name = name
        self.price = price
        self.__spec = kwargs

    def __repr__(self):
        return str(self.__dict__)

class Cart:  #增删改查

    def __init__(self):
        self.items = []

    def addItem(self, item: Item):
        self.items.append(item)
        return self       #添加完购物车后，又返回实例自身，可以实现链式编程

    def settleAccounts(self):
        self.showArticle()
        self.saveArticle()
        self.clearShoppingCart()


    def showArticle(self):
        print('商品清单 ：')
        #[print(item) for item in self.items]
        #print('商品总价 ：{}'.format(sum((items['price'] for items in self.items))))
        #print(self.items)
        print(self.items)

    def saveArticle(self):
        with open('articlefile.txt', 'a', encoding='utf8') as f:
            print('商品清单 ：', file=f)
            [print(article, file=f) for article in self.items]
            #print('商品总价 ：{}'.format(sum((items['price'] for items in self.items))), file=f)

    def clearShoppingCart(self):
        self.items.clear()

    def logout(self, consumption):
        print('您本次消费 {} 元'.format(consumption))
        print('欢迎下次再来')

    def login(self):
        with open('articlefile.txt', 'r', encoding='utf8') as f:
            print('历史购物清单：')
            print(f.read())
        print('账户余额：{}'.format(self._bankCart()))

    def _bankCart(self, bankcart=100):
        #print(bankcart)
        return bankcart

mycart = Cart()
earphone = Item('耳机', 2000, color=Color.RED, type='noise reduce')
computer = Item('MacPro', 20000, color=Color.WHITE, memory='1T')
mycart.addItem(earphone).addItem(computer)
# print(mycart.showArticle())

mycart.showArticle()