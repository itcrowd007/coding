x = int(input())
y = int(input())
z = int(input())
n = int(input())
#Чужой вариант
print ([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i + j + k != n ])
#мой вариант не понял задание
from itertools import groupby
array3=([[i,j,k] for i in [0,x,y,z] if i <=x for j in [0,x,y,z] if j <=y for k in [0,x,y,z] if k <= z and i + j + k != n ])
newarray=[]
for item in array3:
    if item not in newarray:
        newarray.append(item)
print (newarray)
