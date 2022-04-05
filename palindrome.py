import sys

def isPalindrome(text):
    text = list(filter(lambda x: x.isalpha(), text.lower()))
    return text == text[::-1]

if __name__ == "__main__":
    args = sys.argv[1:]
    res = []
    for arg in args:
        if arg not in ["/a", "/all", "-a", "--all"]:
            res.append((arg, isPalindrome(arg)))
    if ("/a" in args) or ("/all" in args) or ("-a" in args) or ("--all" in args):
        for r in res:
            if r[1]: print(f"`{r[0]}` jest palindromem")
            else: print(f"`{r[0]}` nie jest palindromem")
    else:
        for r in res:
            if r[1]: print(r[0])
