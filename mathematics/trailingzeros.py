from factorial import factorial1
import sys

# bad algorithm - due to overflow
def trailingzeros1(n):
    fact = factorial1(n)
    res = 0
    while fact % 10 == 0:
        res = res + 1
        fact = fact /10
    return res

# good algorithm
def trailingzeros2(n):
    res = 0
    i = 5
    while i <= n:
        res = res + int(n/i)
        i = i * 5
    return res

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    #print(trailingzeros1(n))
    print(trailingzeros2(n))

if __name__ == "__main__":
    main()