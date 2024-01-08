def jp1(n, k):
    if n == 1:
        return 0
    return (jp1(n-1, k) + k)%n
    ...

def main():
    n = int(input("No of persons: "))
    k = int(input("Position: "))
    print(jp1(n, k))

if __name__ == "__main__":
    main()