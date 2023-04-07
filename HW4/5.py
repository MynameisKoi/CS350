def find_seq(n, arr):
    for i in range(1, n+1):
        a = arr.index(i)
        if i == arr[i+a+1]:
            print(arr[a:i+a+2])
        else:
            continue

n = 3
arr1 = [2, 3, 1, 2, 1, 3]
arr2 = [3, 1, 2, 1, 3, 2]
print("Following are sequences in arr1")
find_seq(n, arr1)
print("Following are sequences in arr2")
find_seq(n, arr2)

n = 4
arr3 = [4, 1, 3, 1, 2, 4, 3, 2]
arr4 = [2, 3, 4, 2, 1, 3, 1, 4]
print("Following are sequences in arr3")
find_seq(n, arr3)
print("Following are sequences in arr4")
find_seq(n, arr4)