def palindrome1(s, k):
    if k == int(len(s)/2):
        return s[k] == s[int(len(s)/2)]
    return s[k] == s[len(s)-1-k] and palindrome1(s, k+1)

def palindrome2(s, start, end):
    if start >= end:
        return True
    return s[start] == s[end] and palindrome2(s, start+1, end-1)

def main():
    s = input()
    print(palindrome1(s, 0))
    print(palindrome2(s, 0, len(s)-1))

if __name__ == "__main__":
    main()