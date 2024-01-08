import sys

def sumofdigits1(n):
    if n == 0:
        return 0
    return n%10 + sumofdigits1(int(n/10))

# tail recursion
def sumofdigits2(n, k):
    if n == 0:
        return k
    return sumofdigits2(int(n/10), k+(n%10))

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter a whole number")
    print(sumofdigits1(n))
    print(sumofdigits2(n, 0))

if __name__ == "__main__":
    main()