class Sequence:
    def __init__(self):
        self.values = []
    
    def addElement(self, element):
        self.values.append(element)
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Sequence indices must be integers, not " + type(index).__name__)
        return self.values[index]
    
    def __iter__(self):
        return iter(self.values)
    
    def sum(self, upto):
        return sum(self.values[:upto])

class Arithmetic(Sequence):
    def __init__(self, a, delta):
        super().__init__()
        self.a = a
        self.delta = delta
        
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Sequence indices must be integers, not " + type(index).__name__)
        return self.a + self.delta * index
    
    def __iter__(self):
        def _arith():
            q = self.a
            while True:
                yield q
                q += self.delta
        return _arith()
    
    def sum(self, upto):
        return (2 * self.a + (upto - 1)*self.delta) * upto // 2

class Fibonacci(Sequence):
    def __init__(self):
        super().__init__()
        self.addElement(0)
        self.addElement(1)
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Sequence indices must be integers, not " + type(index).__name__)
        while len(self.values) <= index:
            self.addElement(self[-1] + self[-2])
        return self.values[index]
    
    def __iter__(self):
        def _f():
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b
        return _f()
    
    def sum(self, upto):
        while len(self.values) < upto:
            _  = self[len(self.values)]
        return sum(self.values[:upto])

if __name__ == "__main__":
    a = Arithmetic(2, 3)
    f = Fibonacci()
    for i in range(10):
        print(a[i], end=' ')
    print()
    it = iter(f)
    for _ in range(10):
        print(next(it), end=' ')
    print()