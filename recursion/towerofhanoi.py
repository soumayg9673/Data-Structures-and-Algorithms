import sys

def toh1(n, t1, t2, t3):
    if n == 1:
        print(f"Move 1 from {t1} to {t3}")
        return
    toh1(n-1, t1, t3, t2)
    print(f"Move {n} from {t1} to {t3}")
    toh1(n-1, t2, t1, t3)
    ...

def main():
    n = int(input("No. of discs: "))
    if n < 0:
        sys.exit("Please enter the number above 0")
    toh1(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()