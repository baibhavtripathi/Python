# arr = [-1,-3,-5,-6,-5,-7]
arr = [23,45,77,44,45,23]


max_score = -101
second_max_score = -101
for score in arr:
    if score > max_score:
        second_max_score = max_score
        max_score = score
    elif score != max_score and score > second_max_score:
        second_max_score = score
print(second_max_score)

# second_max_score = sorted(arr)[-1]
# for score in sorted(arr)[::-1]:
#     if score < second_max_score:
#         second_max_score = score
#         break
# print(second_max_score)


