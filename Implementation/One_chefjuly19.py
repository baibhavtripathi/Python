for _ in range(int(input())):
    n = int(input())
    coin_list = list(map(int,input().split()))

    avg = sum(coin_list)/n
    min_coin = 0
    for i in range(n):
        if (avg*n - coin_list[i]) / (n-1) == avg:
            if min_coin ==0:
                min_coin = i+1
            elif min_coin > i :
                min_coin = i+1
    
    
    if min_coin == 0:
        print('Impossible')
    else:
        print(min_coin)
