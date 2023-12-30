import sys

# naive solution
def divisorsnumber1(n):
    if n < 1:
        return
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end=" ")
    print()

# efficient solution
def divisorsnumber2(n):
    i = 1
    while i*i <= n:
        if n % i == 0:
            print(i, end=" ")
            if i is not int(n/i):
                print(int(n/i), end=" ")
        i = i + 1
    print()

# more efficient solution
def divisorsnumber3(n):
    i = 1
    while i*i <= n:
        if n%i == 0:
            print(i, end=" ")
        i = i + 1
    while i >= 1:
        if i is not int(n/i) and n%i == 0:
            print(int(n/i), end=" ")
        i = i - 1
        

def main():
    n = int(input())
    if n < 0:
        sys.exit("Please enter non-negative number.")
    divisorsnumber1(n)
    divisorsnumber2(n)
    divisorsnumber3(n)

if __name__ == "__main__":
    main()