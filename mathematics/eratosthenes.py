import sys
from checkforprime import checkforprime3

def eratosthenes1(n):
    if n < 1:
        return False
    for i in range (2, n+1):
        if checkforprime3(i):
            print(i, end=" ")
    print()

def _eratosthenes(n):
    # creating an array
    isprime = [False,False]
    for i in range(2, n+1):
        if checkforprime3(i):
            isprime.append(True)
        else:
            isprime.append(False)
    return isprime

def eratosthenes2(n):
    isprime = _eratosthenes(n)
    i = 2
    while i*i <= n:
        if isprime[i]:
            j = 2 * i
            while j <= n:
                isprime[j] = False
                j = j + i
        i = i + 1
    i = 2
    while i <= n:
        if isprime[i]:
            print(i, end=" ")
        i = i + 1
    print()

def eratosthenes3(n):
    isprime = _eratosthenes(n)
    i = 2
    while i*i <= n:
        if isprime[i]:
            j = i*i
            while j <= n:
                isprime[j] = False
                j = j + i
        i = i + 1
    i = 2
    while i <= n:
        if isprime[i]:
            print(i, end=" ")
        i = i + 1
    print()

def eratosthenes4(n):
    isprime = _eratosthenes(n)
    i = 2
    while i <= n:
        if isprime[i]:
            print(i, end=" ")
            j = i*i
            while j <= n:
                isprime[j] = False
                j = j + i
        i = i + 1

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    eratosthenes1(n)
    eratosthenes2(n)
    eratosthenes3(n)
    eratosthenes4(n)

if __name__ == "__main__":
    main()