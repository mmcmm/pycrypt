
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

        

    def printField(self):
        for i in range(len(self.fieldC)):
            print(self.fieldC[i])


def main():
    print('p: ')
    p = input('> ')

    print('n: ')
    n = input('> ')

    print('Polynom Coefficients: ')
    polynom = input('> ').split(',')

    m = Method1(int(p), int(n), polynom)

    m.generateField()
    m.printField()


if __name__ == '__main__':
    main()
