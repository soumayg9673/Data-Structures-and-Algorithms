def print1ton_1(n):
    if n == 0:
        return
    print1ton_1(n-1)
    print(n, end=" ")

# tail recursive
def print1ton_2(n, k):
    if n == 0:
        return
    print(k, end=" ")
    print1ton_2(n-1, k+1)

def main():
    n = int(input())
    print1ton_1(n)
    print()
    print1ton_2(n, 1)

if __name__ == "__main__":
    main()