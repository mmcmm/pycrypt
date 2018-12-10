
class Method1:

    def __init__(self, p: int, n: int, polynom):
        self.p = p
        self.n = n
        self.polynom = polynom
        self.fieldC = []
        self.fieldF = []

    def generateField(self):
        # add first element
        elem = [0] * self.n
        self.fieldC.append(elem)

        # add initial elements
        for i in range(self.n-1, 0, -1):
            elem = [0] * self.n
            elem[i-1] = 1
            self.fieldC.append(elem)

        # calculate polynom coef
        elem = [0] * self.n
        for i in range(1, len(self.polynom)):
            c = self.polynom[i]
            if c == 0:  # no point moving it
                continue
            c = -c
            while (c < 0):
                c += self.p
            elem[i-1] = c
        self.fieldC.append(elem)

    def printField(self):
        for i in range(len(self.fieldC)):
            print(self.fieldC[i])


def main():
    # TODO:
    # print('p: ')
    # p = input('> ')

    # print('n: ')
    # n = input('> ')

    # print('Polynom Coefficients: ')  # t^3 + 2t +1 -> 1,0,2,1
    # polynom = [int(n) for n in input('> ').split(',')]

    m = Method1(int(3), int(3), [1, 0, 2, 1])

    m.generateField()
    m.printField()


if __name__ == '__main__':
    main()
