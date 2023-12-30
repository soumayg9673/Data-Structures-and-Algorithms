from checkforprime import checkforprime3
import sys

# naive solution
def primefactors1(n):
    if n <= 1:
        return
    for i in range(2, n):
        if checkforprime3(i):
            x = i
            while n%x == 0:
                print(i, end=", ")
                x = x * i
    print()

# efficient solution
def primefactors2(n):
    if n <= 1:
        return
    i = 2
    while i*i <= n:
        while n%i == 0:
                print(int(i), end=", ")
                n = n / i
        i = i + 1
    if n > 1:
        print(int(n), end=", ")
    print()

# more efficient solution
def primefactors3(n):
    if n <= 1:
        return
    while n % 2 == 0:
        print(2, end=", ")
        n = n / 2
    while n % 3 == 0:
        print(3, end=", ")
        n = n / 3
    i = 5
    while i*i <= n:
        while n%i == 0:
            print(i, end=", ")
            n = n/i
        while n%(i+1) == 0:
            print(i+2, end=", ")
            n = n/(i+2)
        i = i + 6
    if n > 3:
        print(n)

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    primefactors1(n)
    primefactors2(n)
    primefactors3(n)

if __name__ == "__main__":
    main()