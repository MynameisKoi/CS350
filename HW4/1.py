import numpy as np

class Node:
    def __init__(self, data, idx):
        self.data=data
        self.idx=idx

elm0=Node("head",1)
elm1=Node("S",2)
elm2=Node("t",3)
elm3=Node("i",4)
elm4=Node("n",5)
elm5=Node("g",None)
ls=np.array([elm0,elm1,elm2,elm3,elm4,elm5])
# print(ls[2].data)

def insertElem(ls, idx, data):
    elm=Node(data,idx)
    ls=np.insert(ls,idx,elm)
    return ls

# insert element and print out ls
ls = insertElem(ls, 3, 'r')
for i in ls:
    print(i.data, end="->")
print("None")

# check the data of the new added element
print("ls[3].data = ", ls[3].data)

