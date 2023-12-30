import sys

def computingpower1(x, n):
    return int(pow(x, n))

def computingpower2(x, n):
    res = 1
    for _ in range (n):
        res = res * x
    return res

def computingpower3(x, n):
    if n == 0:
        return 1
    temp = computingpower3(x, int(n/2))
    temp = temp * temp
    if n%2 == 0:
        return temp
    else:
        return temp*x

def main():
    x = int(input())
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    print(computingpower1(x, n))
    print(computingpower2(x, n))
    print(computingpower3(x, n))

if __name__ == "__main__":
    main()