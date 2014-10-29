import random


class Generator():
    def genseq(self, numb=1):
        arr = []
        for i in range(numb):
            arr.append(self.getnext())
        return arr

    def getnext(self):
        pass


class BuiitInGener(Generator):
    def getnext(self):
        return random.randint(0, 255)


class LemerGenFirstBits(Generator):
    def __init__(self):
        self.a, self.m, self.c = 2 ** 16 + 1, 2 ** 32, 119
        self.x = random.randint(1, self.m - 1)

    def getnext(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x % 2 ** 8


class LemerGenLastBits(Generator):
    def __init__(self):
        self.a, self.m, self.c = 2 ** 16 + 1, 2 ** 32, 119
        self.x = random.randint(1, self.m - 1)

    def getnext(self):
        self.x = (self.a * self.x + self.c) % self.m
        return (self.x >> 24) & 0xff


class L20Generator(Generator):
    def __init__(self):
        self.pol = [0, 11, 15, 17]
        self.state = [random.choice([0, 1]) for _ in range(20)]

    def getnext(self):
        res = ''
        for __ in range(8):
            tmp = 0
            for _ in self.pol:
                if self.state[_] == 1:
                    tmp ^= 1
            self.state.append(tmp)
            res += str(self.state.pop(0))
        return int(res, 2)


class L89Generator(Generator):
    def __init__(self):
        self.pol = [0, 51]
        self.state = [random.choice([0, 1]) for _ in range(89)]

    def getnext(self):
        res = ''
        for __ in range(8):
            tmp = 0
            for _ in self.pol:
                if self.state[_] == 1:
                    tmp ^= 1
            self.state.append(tmp)
            res += str(self.state.pop(0))
        return int(res, 2)


class LFSR():
    def __init__(self, polyn):
        self.polyn = polyn
        self.state = [random.choice([0, 1]) for _ in range(len(polyn))]

    def step(self):
        numb = 0
        for _ in range(len(self.polyn)):
            if self.polyn[_] & self.state[_] == 1:
                numb ^= 1
        self.state.append(numb)
        return self.state.pop(0)


class GeffeGen(Generator):
    def __init__(self):
        l1 = LFSR([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        l2 = LFSR([1, 1, 0, 1, 1, 0, 0, 0, 0])
        l3 = LFSR([1, 0, 0, 1, 0, 0, 0, 0, 0, 0])
        self.l1, self.l2, self.l3 = l1, l2, l3

    def getnext(self):
        res = ''
        for _ in range(8):
            x, y, s = self.l1.step(), self.l2.step(), self.l3.step()
            res += str(s & x ^ (1 ^ s) & y)
        return int(res, 2)


class Librarian(Generator):
    def getnext(self):
        f = open('txt1')
        f.seek(random.randint(1, 300000))
        return ord(f.read(1)) % 2 ** 8


class BBS(Generator):
    def __init__(self):
        self.numb = 0x5ABA02CC8F5C8E71DD2FE0F870C2CDDB77B4EC7 * 0x72AC531AC3A02B881DDF
        self.r = random.randint(2, self.numb-1)

    def getnext(self):
        self.r = (self.r ** 2) % self.numb
        return self.r % 256