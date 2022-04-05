values = {"I":1,
          "V":5,
          "X":10,
          "L":50,
          "C":100,
          "D":500,
          "M":1000,
          "IV":4,
          "IX":9,
          "XL":40,
          "XC":90,
          "CD":400,
          "CM":900}

def dictRev(d):
    ret = {}
    for (key, value) in d.items(): ret[value] = key
    return ret

reverse_values = dictRev(values)

def readRoman(roman):
    i = 0
    l = len(roman)
    res = 0
    while i < l:
        if i == l - 1: res += values[roman[-1]]
        elif roman[i] in "VLDM": res += values[roman[i]]
        else:
            if values[roman[i+1]] > values[roman[i]]:
                res += values[roman[i:i+2]]
                i += 1
            else:
                res += values[roman[i]]
        i += 1
    return res

def writeRoman(number):
    ret = ""
    x = sorted(list(reverse_values.keys()), reverse=True)
    while 0 < number:
        if x[0] <= number:
            ret += reverse_values[x[0]]
            number -= x[0]
        else:
            x = x[1:]
    return ret

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if args[0] == "r":
        print(writeRoman(int(args[1])))
    elif args[0] == "a":
        print(readRoman(args[1]))

