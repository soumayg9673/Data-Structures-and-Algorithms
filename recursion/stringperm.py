def swapchar(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    return str(s)

def stringperm1(s, i):
    if i == (len(s)-1):
        print(s, end=" ")
        return
    for j in range(i, len(s)):
        swapchar(list(s), i, j)
        stringperm1(s, i+1)
        swapchar(list(s), j ,i)


def main():
    s = input("Enter string: ")
    stringperm1(s, 0)
    

if __name__ == "__main__":
    main()