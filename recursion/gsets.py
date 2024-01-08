def gsets1(s, s1, i):
    if len(s) == i:
        print(s1)
        return
    gsets1(s, s1, i+1)
    gsets1(s, s1+s[i], i+1)

def main():
    s = input()
    gsets1(s,"", 0)

if __name__ == "__main__":
    main()