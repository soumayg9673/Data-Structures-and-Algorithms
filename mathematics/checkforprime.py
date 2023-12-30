import sys

# naive solution
def checkforprime1(n):
    if n == 1:
        return False
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True

# efficient solution
def checkforprime2(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i = i + 1
    return True

# more efficient solution
def checkforprime3(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n % (i+1) == 0:
            return False
        i = i + 6
    return True

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    print(checkforprime1(n))
    print(checkforprime2(n))
    print(checkforprime3(n))

if __name__ == "__main__":
    main()