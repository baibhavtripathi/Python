highest_num, second_highest_num = 0, 0
for ele in map(int, input().split()):
    if ele > highest_num:
        second_highest_num = highest_num
        highest_num = ele
    else: second_highest_num = max(second_highest_num, ele)
print(second_highest_num)