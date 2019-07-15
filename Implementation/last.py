M = 1000000007
def fibo(n):
    if n<2:
        return n
    x=0
    y=1
    m=n-1
    res=0
    while(m>=1):
        res = (x+y)%M
        x = y
        y = res
        m-=1
    return res

def notfib(n):
    if n<3:
        return 0
    a=0
    b=1
    m=1
    res=0
    while m<n:
        res = (a+b+fibo(n-3))%M
        a = b
        b=res
        m+=1
    return res
if __name__ == "__main__":
    n = int(input())
    print(fibo(n+1),notfib(n))
