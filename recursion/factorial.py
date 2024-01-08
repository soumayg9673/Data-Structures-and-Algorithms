def factorial1(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial1(n-1)

# tail recursive
def factorial2(n, k):
    if n == 0 or n == 1:
        return k
    return factorial2(n-1, k*n)

def main():
    n = int(input())
    print(factorial1(n))
    print(factorial2(n, 1))

if __name__ == "__main__":
    main()