def twooddoccuring1(arr, n):
    res = []
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count = count + 1
        if count%2 != 0:
            print(arr[i], end=" ")
    print()

def twooddoccuring2(arr, n):
    x = arr[0]
    for i in range(1, n):
        x = x ^ arr[i]
    k = x & (~(x-1))
    res1, res2 = 0, 0  
    for i in range(n):
        if arr[i] & k != 0:
            res1 = res1 ^ arr[i]
        else:
            res2 = res2 ^ arr[i]
    print(res1, res2)

def main():
    arr = [3,4,3,4,5,4,4,6,7,7]
    twooddoccuring1(arr, len(arr))
    twooddoccuring2(arr, len(arr))

if __name__ == "__main__":
    main()