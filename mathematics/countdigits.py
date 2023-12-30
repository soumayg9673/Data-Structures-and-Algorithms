def countDigits1(x):
    res = 0
    while x > 0:
        x = x/10
        res = res + 1
    return res

def countDigits2(x):
    return len(str(x))

def main():
    x = int(input())
    print(countDigits1(x))
    print(countDigits2(x))

if __name__ == "__main__":
    main()