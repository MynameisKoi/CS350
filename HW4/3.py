def partition(array):
    array.sort()
    for i in range(len(array)):
        if sum(array[i:]) == sum(array[:i]):
            print("ls1 = ", array[i:])
            print("ls2 = ", array[:i])
            return True
    print("Impossible to partition into 2 subsets with equal sum!")

ls = [1, 3, 2, 1, 2, 1]
print("Original list: ", ls)
partition(ls)

ls = [1,2,3,4,5,6,7,8,9,10]
print("Original list: ", ls)
partition(ls)

ls = [1,2,3,4,5,6,7,8,9,11]
print("Original list: ", ls)
partition(ls)