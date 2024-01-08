def subsetsum1(arr, n, sum):
    if n== 0:
        return 1 if sum == 0 else 0
    return subsetsum1(arr, n-1, sum) + subsetsum1(arr, n-1, sum-arr[n-1])

def main():
    arr = [10,20,15]
    sum = 25
    print(subsetsum1(arr, len(arr), sum))

if __name__ == "__main__":
    main()