import numpy as np

class LogicGate():
    def AND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        tmp = np.sum(x*w) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7
        tmp = np.sum(x*w) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def OR(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.2
        tmp = np.sum(x*w) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def XOR(self, x1, x2):
        s1 = self.NAND(x1, x2)
        s2 = self.OR(x1, x2)
        return self.AND(s1, s2)


if __name__ == "__main__":
    pass
