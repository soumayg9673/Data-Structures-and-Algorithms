import sys

def sumofnaturalno1(n):
    if n == 0:
        return 0
    return n + sumofnaturalno1(n-1)

# tail recursion
def sumofnaturalno2(n, k):
    if n == 1:
        return k
    return sumofnaturalno2(n-1, k+n)
    

def main():
    n = int(input())
    if n < 1:
        sys.exit("Please enter the natural number")
    print(sumofnaturalno1(n))
    print(sumofnaturalno2(n, 1))

if __name__ == "__main__":
    main()