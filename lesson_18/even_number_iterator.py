class EvenNumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current = self.current + 1
                return result
            self.current = self.current + 1
        raise StopIteration


N = 10
even_iter = EvenNumberIterator(N)

for number in even_iter:
    print(number)