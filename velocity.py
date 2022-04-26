class Velocity:
    def __init__(self, v=0):
        self.v = v
    def gamma(self):
        if self.v == 1:
            return float("Inf")
        return 1.0 / pow(1 - self.v**2, 0.5)
    def __add__(self, other):
        if not isinstance(other, Velocity):
            return NotImplemented
        return Velocity((self.v + other.v) / (1.0 + self.v * other.v))
    def __iadd__(self, other):
        if not isinstance(other, Velocity):
            return NotImplemented
        self.v = ((self.v + other.v) / (1.0 + self.v * other.v))
    def __str__(self):
        return f"{self.v}"
    def __repr__(self):
        return f"Velocity({self.v})"

if __name__ == "__main__":
    v1, v2 = input().strip().split()
    try:
        v1 = Velocity(float(v1))
        v2 = Velocity(float(v2))
        v3 = v1 + v2
        print("beta =", v3)
        print("gamma =", v3.gamma())
    except ValueError as e:
        print("Błąd:", e)