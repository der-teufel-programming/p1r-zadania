class Rest:
    def __init__(self, value=0):
        self.value = value % 17
    
    def __add__(self, other):
        if not isinstance(other, (Rest, int)):
            return NotImplemented
        if isinstance(other, Rest):
            return Rest(self.value + other.value)
        return Rest(self.value + other)
    def __mul__(self, other):
        if not isinstance(other, (Rest, int)):
            return NotImplemented
        if isinstance(other, Rest):
            return Rest(self.value * other.value)
        return Rest(self.value * other)
    def __iadd__(self, other):
        if not isinstance(other, (Rest, int)):
            return NotImplemented
        if isinstance(other, Rest):
            self.value = (self.value + other.value) % 17
        else:
            self.value = (self.value + other) % 17
        return self
    def __imul__(self, other):
        if not isinstance(other, (Rest, int)):
            return NotImplemented
        if isinstance(other, Rest):
            self.value = (self.value * other.value) % 17
        else:
            self.value = (self.value * other) % 17
        return self
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"Rest({self.value})"

if __name__ == "__main__":
        a, b = input().strip().split()
        try:
            a, b = Rest(int(a)), Rest(int(b))
            print(f"Suma modulo 17:    {a + b}")
            print(f"Iloczyn modulo 17: {a * b}")
        except ValueError as e:
            print("Błąd:", e)