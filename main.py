"7"
class GoodIfrit:
    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = goodness

    def change_goodness(self, value):
        self.goodness = max(0, self.goodness + value)

    def __add__(self, number):
        return GoodIfrit(self.height + number, self.name, self.goodness)

    def __call__(self, arg):
        return arg * self.goodness // self.height

    def __str__(self):
        return f'Good Ifrit {self.name}, {self.height}, {self.goodness}'

    def __lt__(self, other):
        if self.goodness != other.goodness:
            return self.goodness < other.goodness
        elif self.height != other.height:
            return self.height < other.height
        else:
            return self.name < other.name

    def __gt__(self, other):
        if self.goodness != other.goodness:
            return self.goodness > other.goodness
        elif self.height != other.height:
            return self.height > other.height
        else:
            return self.name > other.name

