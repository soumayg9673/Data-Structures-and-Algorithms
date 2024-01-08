def ropecutting(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = int(max(ropecutting(n-a,a,b,c),ropecutting(n-b,a,b,c),ropecutting(n-c,a,b,c)))
    if res == -1:
        return -1
    return res + 1

def main():
    n = int(input("Rope lenght: "))
    a = int(input("cut length 1: "))
    b = int(input("cut length 2: "))
    c = int(input("cut length 3: "))
    print(ropecutting(n, a, b, c))

if __name__ == "__main__":
    main()