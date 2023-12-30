from countdigits import countDigits2

def palindrom1(x):
    if x < 0:
        return False
    x1 = "".join(reversed(str(x)))
    return x == int(x1)

def palindrom2(x):
    if x < 0:
        return False
    temp = x
    rev = 0
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp = int(temp / 10)
    return rev == x
    

x = int(input())
print(palindrom1(x))
print(palindrom2(x))