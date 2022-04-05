import matplotlib.pyplot as plt

def gfrange(a, b, d):
    res = []
    while a < b:
        res.append(a)
        a += d
    return res

def trigplot(trigfns, a, b, d, save_format):
    x = gfrange(a, b, d)
    y = {fn.__name__ : list(map(fn, x)) for fn in trigfns}
    for (name, ys) in y.items():
        plt.plot(x, ys, label=name)
    plt.xlabel("$x$")
    plt.ylabel("$y$")

    plt.title("Wykresy funkcji")

    plt.legend()
    if save_format != None:
        plt.savefig(f"trigplot.{save_format}", dpi=300)
        print(f"Zapisano plik trigplot.{save_format}.")
    else:
        plt.show()

if __name__ == "__main__":
    fileformat = input("Podaj rozszerzenie (png, jpg, svg, pdf): ").strip()
    from math import sin, tan
    def id(x): x
    if fileformat in ["png", "jpg", "svg", "pdf"]:
        trigplot([id, sin, tan], -.5, .5, .01, fileformat)
    else:
        print(f"Niedozwolone rozszerzenie `{fileformat}`!")
        trigplot([id, sin, tan], -.5, .5, .01, None)
