import sys

# good algorithm
def factorial1(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res

# bad algorithm
def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n-1)

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    print(factorial1(n))
    print(factorial2(n))

if __name__ == "__main__":
    main()