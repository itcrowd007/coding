# Find the Runner-Up Score!
#мой вариант рабочий
n = int(input())
if n >2 and n <= 10:
    arr = list(map(int, input().split()[:n]))
    if len(arr) >= 2:
        arr = list(set(arr))
        arr.remove(max(arr))
        print (max(arr))
#чужой вариант тоже рабочий
#i = int(input())
#lis = list(map(int,input().strip().split()))[:i]
#z = max(lis)
#while max(lis) == z:
#    lis.remove(max(lis))
#print (max(lis))

