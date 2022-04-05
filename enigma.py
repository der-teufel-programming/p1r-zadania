def encode(m, key):
    return [ch ^ key for ch in m]

def decode(s, key):
    return [ch ^ key for ch in s]

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) < 4:
        print(f"{sys.argv[0]} wymaga 4 argumentów. Otrzymano: {len(args)}.")
        exit()
    try:
        key = int(args[0])
        assert 0 <= key and key <= 255
    except ValueError:
        print(f"Klucz musi być liczbą. \"{args[0]}\" nie jest liczbą.")
    except AssertionError:
        print("Klucz musi być liczbą z przedziału 0-255.")
    if args[1] == "/e":
        # encode
        out_file = open(args[3], "w")
        try:
            with open(args[2], "rb") as in_file:
                for b in in_file:
                    print(*encode(b, key), file=out_file)
        except FileNotFoundError:
            print(f"Nie można otworzyć pliku wejściowego \"{args[2]}\".")
        out_file.close()
    elif args[1] == "/d":
        # decode
        out_file = open(args[3], "w")
        try:
            with open(args[2], "r") as in_file:
                secret = map(int, in_file.read().split())
                message = bytes(decode(secret, key)).decode("ASCII")
                print(message, file=out_file, end='')
        except FileNotFoundError:
            print(f"Nie można otworzyć pliku wejściowego \"{args[2]}\".")
        out_file.close()
    else:
        print(f"Błędna opcja \"{args[1]}\".")
