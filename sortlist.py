class SortedList(list):
    def __init__(self):
        super().__init__()
    def append(self, element):
        list.append(self, element)
        list.sort(self)
    def __setitem__(self, index, value):
        list.__setitem__(self, index, value)
        list.sort(self)

if __name__ == "__main__":
    q = SortedList()
    i = input().strip().split()
    for n in i:
        try:
            q.append(float(n))
        except ValueError:
            pass
    print(', '.join((str(x) for x in q)))
    print(', '.join((str(x) for x in q[::-1])))