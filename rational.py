def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

class RationalNumber:
    def __init__(self, p=0, q=1):
        
        if isinstance(p, str):
            ns = p.split('/')
            try:
                n, d = tuple(ns)
                n = int(n)
                d = int(d)
                if d < 0:
                    n = -n
                    d = -d
                p, q = n, d
            except ValueError:
                p, q = 0, 1
        g = gcd(p, q)
        self._p = p // g
        self._q = q // g
    
    def numerator(self):
        return self._p
    def denominator(self):
        return self._q
    
    def __float__(self):
        return self._p / self._q
    
    def __neg__(self):
        return RationalNumber(-self._p, self._q)
    
    def __lt__(self, other):
        if not isinstance(other, RationalNumber):
            return NotImplemented
        return self._p * other._q < other._p * self._q
    
    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            return NotImplemented
        return RationalNumber(self._p * other._q + self._q * other._p, self._q * other._q)
    
    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            return NotImplemented
        return RationalNumber(self._p * other._p, self._q * other._q)
    
    def __iadd__(self, other):
        if not isinstance(other, RationalNumber):
            return NotImplemented
        self = RationalNumber(self._p * other._q + self._q * other._p, self._q * other._q)
        return self
    
    def __imul__(self, other):
        if not isinstance(other, RationalNumber):
            return NotImplemented
        self = RationalNumber(self._p * other._p, self._q * other._q)
        return self
    
    def __repr__(self):
        return f"RationalNumber({self._p}, {self._q})"
    
    def __str__(self):
        return f"{self._p}/{self._q}"

if __name__ == "__main__":
    a, b = input().strip().split()
    a, b = RationalNumber(a), RationalNumber(b)
    print(float(a), float(b))
    print(-a, -b)
    if a < b: print(a, b)
    else: print(b, a)
    print(a + b, a * b)