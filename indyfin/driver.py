import sys


class RiskStep(object):

    def __init__(self, low, high, lchild=None, rchild=None):
        self.low = low
        self.high = high
        self.lchild = lchild
        self.rchild = rchild


class RiskSurvey(object):

    def __init__(self):
        self.root = self.set_up_tree()

    def play(self, sequence):
        node = self.root
        for step in sequence:
            if step == "R":
                node = node.rchild
            else:
                node = node.lchild
        print(node.low, node.high)

    def set_up_tree(self):
        l1_1 = RiskStep(0.111, 0.996)
        l1_2 = RiskStep(0.122, 0.986)
        root = RiskStep(0.100, 0.999, l1_1, l1_2)
        return root


def run():
    rs = RiskSurvey()
    rs.play(sys.argv[1:])


if __name__ == "__main__":
    run()
