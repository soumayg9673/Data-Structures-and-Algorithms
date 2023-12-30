from hcf import hcf3

# naive solution
def lcm1(a, b):
    res = max(a, b)
    while True:
        if res%a == 0 and res%b == 0:
            return res
        res = res + 1
    return res

# efficient solution
# a * b = hcf(a, b) * lcm(a, b)
def lcm2(a, b):
    return int((a*b)/hcf3(a, b))

def main():
    a = int(input())
    b = int(input())
    print(lcm1(a, b))
    print(lcm2(a, b))
    

if __name__ == "__main__":
    main()
