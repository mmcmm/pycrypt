from string import ascii_uppercase


class Method1:

    def __init__(self, p: int, n: int, polynom):
        self.p = p
        self.n = n
        self.polynom = polynom
        self.fieldC = []
        self.fieldF = []
        self.q = p**n
        self.alphabet = self.makeAlphabet()

    def generateField(self):
        # add first element
        elem = [0] * self.n
        self.fieldC.append(elem)

        # add initial elements
        for i in range(self.n-1, 0, -1):
            elem = [0] * self.n
            elem[i-1] = 1
            self.fieldC.append(elem)

        # calculate next element from polynom
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

        # self.multiply([0, 1, 2], [0, 1, 0])
        # calculate next elements
        for i in range(len(self.fieldC), self.q):
            nextElem = self.multiply(self.fieldC[i-1], self.fieldC[1])
            self.fieldC.append(nextElem)

        # generate F values
        self.calculateFValues()

    def multiply(self, p1, p2):
        # multiply
        coeffs = [0] * (len(p2)+len(p1)-1)
        for i1, coef1 in enumerate(p1):
            for i2, coef2 in enumerate(p2):
                coeffs[i1 + i2] += coef1 * coef2

        # replace higher ranked term with previous
        diff = len(coeffs) - self.n
        for i in range(diff):
            r = len(coeffs) - i - 1  # rank
            if coeffs[i] != 0:
                for _ in range(coeffs[i]):  # add it as needed
                    for j in range(0 + diff, len(coeffs)):
                        coeffs[j] += self.fieldC[r][j-diff]
                coeffs[i] = 0

        # mod p coefficients
        result = []
        for i in range(len(coeffs)-1, len(coeffs)-self.n-1, -1):
            result.append(coeffs[i] % self.p)
        result.reverse()

        return result

    def add(self, p1, p2):
        result = []
        for i in range(len(p1)):
            result.append((p1[i] + p2[i]) % self.p)
        return result

    def calculateFValues(self):
        for _, coeff in enumerate(self.fieldC):
            value = 0
            for j, c in enumerate(coeff):
                value += c * (self.p**(self.n-j-1))
            self.fieldF.append(value)

    def crypt(self, word, decrypt=None):
          #  fill matrix
        m = [[]] * 11  # a, b, c ... j
        for i in range(len(m)):
            m[i] = [0] * max(2, len(word))

        # starting values, coef index
        a1 = 16
        a2 = 6
        b1 = 13
        b2 = 10

        # a1, b1
        m[4][0] = self.fieldC[a1]
        m[5][0] = a1
        m[6][0] = self.fieldC[b1]
        m[7][0] = b1

        # a2, b2
        m[4][1] = self.fieldC[a2]
        m[5][1] = a2
        m[6][1] = self.fieldC[b2]
        m[7][1] = b2

        # add letters and values
        i = 0
        for c in word:
            alphabelPos = ascii_uppercase.index(c)+1
            elemIdx = self.findFieldElem(alphabelPos)
            m[0][i] = c
            m[1][i] = alphabelPos
            m[2][i] = self.fieldC[elemIdx]
            m[3][i] = elemIdx
            i = i + 1

        # fill a and b rows
        for i in range(2, len(word)):
            m[4][i] = self.add(m[4][i-1], m[4][i-2])  # a + a prev
            m[5][i] = self.findFieldElemPos(m[4][i])  # a t pos

            b = (m[7][i-1] + m[7][i-2]) % (self.q-1)
            m[6][i] = self.fieldC[b]  # b * b prev
            m[7][i] = self.findFieldElemPos(m[6][i])  # b t pos

        # fil in final rows, y = a x + b
        for i in range(len(word)):
            elem = (m[5][i] + m[3][i]) % (self.q-1)  # a * x, add exp
            m[8][i] = self.add(self.fieldC[elem], m[6][i])  # a * x + b
            m[9][i] = self.findFieldFVal(m[8][i])
            m[10][i] = self.alphabet[m[9][i]]  # letters

        print()
        for row in m:
            print(row)

    def findFieldFVal(self, coeff):
        i = 0
        for e in self.fieldC:
            if e == coeff:
                return self.fieldF[i]
            i = i + 1

    def findFieldElem(self, position):
        for i in self.fieldF:
            if self.fieldF[i] == position:
                return i

    def findFieldElemPos(self, elem):
        i = 0
        for e in self.fieldC:
            if e == elem:
                return i
            i = i + 1

    def makeAlphabet(self):
        alphabet = [" "]
        for c in ascii_uppercase:
            alphabet.append(c)
        return alphabet

    def printField(self):
        for i in range(len(self.fieldC)):
            print("t^" + str(i) + " = (" + ', '.join(str(x) for x in self.fieldC[i])
                  + ")      f(" + str(i) + ") = " + str(self.fieldF[i]))


def main():
    # TODO:
    # print('p: ')
    # p = input('> ')

    # print('n: ')
    # n = input('> ')

    # print('Polynom Coefficients: ')  # t^3 + 2t +1 -> 1,0,2,1
    # polynom = [int(n) for n in input('> ').split(',')]

    # print('Word: ')
    # word = input('> ')

    m = Method1(int(3), int(3), [1, 0, 2, 1])

    m.generateField()
    m.printField()
    m.crypt("SECRET")


if __name__ == '__main__':
    main()
