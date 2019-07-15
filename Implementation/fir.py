for _ in range(int(input())):
    dictstr = input()
    patt = input()
    out_str = ''
    from collections import defaultdict
    out_dict=defaultdict(int)
    for i in dictstr:
        if i not in out_dict.keys():
            out_dict[i]=1
        else:
            out_dict[i]= out_dict.get(i,0)+1
    #print(out_dict)
    for i in out_dict.keys():
        if i in patt:
            print(i*patt.count(i),end='')
    print()
