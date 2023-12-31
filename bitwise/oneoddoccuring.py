def oneoddoccuring1(arr, n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count = count + 1
        if count%2 != 0:
            return arr[i]

def oneoddoccuring2(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = res ^ arr[i]
    return res

def main():
    arr = [7,3,7,7,7]
    print(oneoddoccuring1(arr, len(arr)))
    print(oneoddoccuring2(arr, len(arr)))

if __name__ == "__main__":
    main()