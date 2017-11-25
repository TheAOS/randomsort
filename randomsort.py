import random, itertools

class RSort():
    def __init__(self, o):
        self.iterations = 0
        self.original = o
        self.sorted = None
    def unique_indices(self, a, b):
        i = random.randint(a, b)
        j = random.choice(list(itertools.chain(range(0, i), range(i + 1, b))))
        return (i, j)

    def single_pass(self):
        indices = self.unique_indices(0, len(self.sorted) - 1)
        tmp = self.sorted[indices[0]]
        self.sorted[indices[0]] = self.sorted[indices[1]]
        self.sorted[indices[1]] = tmp

    def is_ordered(self):
        for i in range(len(self.sorted) - 1):
            if(self.sorted[i] > self.sorted[i + 1]):
                return False
        return True

    def sort(self):
        if self.sorted is None:
            self.sorted = self.original[:]
        while not self.is_ordered():
            self.single_pass()
            self.iterations += 1
