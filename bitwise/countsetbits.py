def countsetbits1(n):
    res = 0
    while n > 0:
        if n >> 1 != 0:
            res = res + 1
        n = n >> 1
    return res

def countsetbits2(n):
    res = 0
    while n > 0:
        n = n & (n-1)
        res = res + 1
    return res

def main():
    n = int(input())
    print(countsetbits1(n))
    print(countsetbits2(n))

if __name__ == "__main__":
    main()