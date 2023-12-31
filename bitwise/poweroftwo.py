from countsetbits import countsetbits2

def poweroftwo1(n):
    if n%2 != 0:
        return False 
    res = countsetbits2(n)
    return res == 1

def poweroftwo2(n):
    return (n and (n & (n-1) == 0))

def main():
    n = int(input())
    print(poweroftwo1(n))
    print(poweroftwo2(n))

if __name__ == "__main__":
    main()