class LogicGate():
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta
    def AND(self, x1, x2):
        tmp = x1 * self.w1 + x2 * self.w2
        if tmp <= self.theta:
            return 0
        elif tmp > self.theta:
            return 1

    def NAND(self, x1, x2):
        tmp = x1 * (-1 * self.w1) + x2 * (-1 * self.w2)
        if tmp <= (-1 * self.theta):
            return 0
        else:
            return 1

    def OR(self, x1, x2):
        tmp = x1 * (self.w1) + x2 * (self.w2)
        if tmp <= (0.2):
            return 0
        else:
            return 1

if __name__ == "__main__":
    l = LogicGate(0.5, 0.5, 0.7)
    print(l.AND(0, 0))

    print(l.NAND(0, 0))
