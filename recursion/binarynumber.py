def binary1(n):
    if n == 0:
        return
    binary1(int(n/2))
    print(n%2, end="")

def main():
    n = int(input())
    binary1(n)

if __name__ == "__main__":
    main()