import random


class LFSR():
    def __init__(self, polyn):
        self.len, self.polyn = polyn[0], polyn[1:len(polyn)]
        self.state = [random.choice([0, 1]) for _ in range(self.len)]

    def step(self):
        numb = 0
        for _ in self.polyn:
            if self.state[_] == 1:
                numb ^= 1
        self.state.append(numb)
        return self.state.pop(0)

    def gener_sequence(self, length):
        return [self.step() for _ in range(length)]

    def set_state(self, state):
        self.state = state


