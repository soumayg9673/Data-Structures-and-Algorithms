def checkkthbit1(n, k):
    if k < 1:
        return
    elif (n>>(k-1))&1 != 0:
        print("Yes")
    else:
        print("No")

def main():
    n = int(input())
    k = int(input())
    checkkthbit1(n, k)


if __name__ == "__main__":
    main()