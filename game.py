class Apple:
    states = {0: "Отсутствует", 1: "Цветок", 2: "Недозрелое", 3: "Созревшее"}

    def __init__(self, _index):
        self.state = 0
        self._index = _index

    def grow(self):
        currentState = self.state
        if currentState + 1 > Apple.states.__len__():
            print("Яблоко уже созрело")
        else:
            self.state = currentState + 1

    def is_ripe(self):
        return self.state == Apple.states.__len__()


class AppleTree:

    def __init__(self, coutOfApples):
        self.apples = self.__private_genetateAppleList(coutOfApples)

    def __private_genetateAppleList(self, coutOfApples):
        list = []
        for x in range(0, coutOfApples):
            list.append(Apple(x))
        return list

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        for apple in self.apples:
            if not apple.is_ripe():
                return False
        return True

    def give_away_all(self):
        list = self.apples
        self.apples = []
        return list


class Gardener:

    def __init__(self, name, listAppleTree, baskets):
        self.name = name
        self.listAppleTree = listAppleTree
        self.baskets = baskets

    def work(self):
        for tree in self.listAppleTree:
            tree.grow_all()

    def harvest(self):
        for tree in self.listAppleTree:
            if tree.all_are_ripe():
                for apple in tree:
                    self.__private_getBasketNext().set_apple(apple)
            else:
                print("уражай еше не созрел")

    def __private_getBasketNext(self):
        for basket in self.baskets:
            if not basket.is_full():
                return basket

    def knowledge_base(self):
        return "some rules\n" + "garden:" + self.toString()

    def toString(self):
        return "name: " + self.name + "\n count of tree " + len(self.listAppleTree)


class Basket:
    def __init__(self, s):
        self.s = s
        self.list = []

    def set_apple(self, apple):
        if not self.is_full():
            self.list.append(apple)
        else:
            print("i am full")

    def is_full(self):
        return self.list.__len__() == self.s


if __name__ == '__main__':
    a = [AppleTree(10), AppleTree(20), AppleTree(30), AppleTree(40), AppleTree(50)]
    b = [Basket(20), Basket(20), Basket(20), Basket(20), Basket(30), Basket(20)]
    g = Gardener("Sanya", a, b)
   # g.knowledge_base()
    g.work()
    #g.harvest()
    g.work()
    g.work()
    g.work()
    g.harvest()
