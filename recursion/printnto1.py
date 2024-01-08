def printnto1_1(n):
    if n == 0:
        return
    print(n, end=" ")
    printnto1_1(n-1)

def main():
    n = int(input())
    printnto1_1(n)

if __name__ == "__main__":
    main()