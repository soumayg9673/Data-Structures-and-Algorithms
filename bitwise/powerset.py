def powerset1(s):
    n = len(s)
    for i in range(1<<n):
        for j in range(n):
            if i&(1<<j) != 0:
                print(s[j], end="")
        print()

def main():
    s = input()
    powerset1(s)

if __name__ == "__main__":
    main()