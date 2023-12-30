# naive solution
def hcf1(a, b):
    res = min(a, b)
    while res > 0:
        if a % res == 0 and b % res == 0:
            break
        res = res - 1
    return res

# euclidean algorithm 1
def hcf2(a, b):
    while a is not b:
        if a > b:
            a = a -b
        else:
            b = b - a
    return a

# euclidean algorithm 2
def hcf3(a, b):
    if b == 0:
        return a
    else:
        return hcf3(b, a%b)


def main():
    a = int(input())
    b = int(input())
    print(hcf1(a, b))
    print(hcf2(a, b))
    print(hcf3(a, b))
    

if __name__ == "__main__":
    main()