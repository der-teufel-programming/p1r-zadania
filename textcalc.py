class CalcError(Exception):
    pass


map_operators = {"+": lambda x, y: x + y,
                 "-": lambda x, y: x - y,
                 "*": lambda x, y: x * y,
                 "/": lambda x, y: x / y,
                 "%": lambda x, y: x % y,
                 "^": lambda x, y: pow(x, y)}

def textcalc(text):
    values = text.split(" ")
    if len(values) != 3: raise CalcError("Równanie powinno zawierać tylko dwie spacje.")
    try:
        v1 = float(values[0])
    except ValueError:
        raise CalcError(f"\"{values[0]}\" nie jest liczbą.")
    try:
        v2 = float(values[2])
    except ValueError:
        raise CalcError(f"\"{values[2]}\" nie jest liczbą.")
    op = values[1]
    if op not in map_operators:
        raise CalcError("Nieznany operator.")
    if op == "/" and v2 == 0:
        raise CalcError("Dzielenie przez zero.")
    return map_operators[op](v1, v2)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    out_file = open(args[1], "w")
    with open(args[0], "r") as in_file:
        for line in in_file:
            try:
                result = textcalc(line.strip())
                print(f"{line.strip()} = {result}", file=out_file)
            except CalcError as e:
                print(f"Błąd! {e}", file=out_file)
    out_file.close()
