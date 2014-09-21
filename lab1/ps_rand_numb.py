import random


class BuiitInGener():
    def gener_bit(self):
        return random.choice(['0', '1'])

    def gener_byte(self):
        tmp = str(bin(random.randint(0, 255)))[2:]
        tmp = tmp if len(tmp) == 8 else '0'*(8 - len(tmp)) + tmp
        return tmp


class LemerGenerator():
    def __init__(self):
        self.a, self.m, self.c, self.x = 2 ** 16 + 1, 2 ** 32, 119, ''
        self.reset_init_value()

    def reset_init_value(self):
        self.x = str(bin(random.randint(1, self.m)))[2:]
        self.check_x()

    def gener_first_byte(self):
        self.x = str(bin((self.a * int(self.x, 2) + self.c) % self.m))[2:]
        self.check_x()
        return self.x[24:]

    def gener_last_byte(self):
        self.x = str(bin((self.a * int(self.x, 2) + self.c) % self.m))[2:]
        self.check_x()
        return self.x[:8]

    def check_x(self):
        self.x = self.x if len(self.x) == 32 else '0'*(32 - len(self.x)) + self.x


if __name__ == "__main__":
    temp = BuiitInGener()
    temp2 = LemerGenerator()
    print(temp2.gener_last_byte())
    print(temp2.gener_first_byte())
    print(temp2.gener_first_byte())
    # print(temp.gener_bit())
    # print(temp.gener_byte())
