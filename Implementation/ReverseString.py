arr = ["h", "e" ,"l" ,"l" ,"o"]
arr_length = len(arr)
for i in range(arr_length//2):
    arr[i], arr[arr_length - 1 - i] = arr[arr_length - 1 - i], arr[i]

print(arr)