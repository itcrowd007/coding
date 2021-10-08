#Мое длинное решение
n=int(input().strip())
arr=[]
for i in range (1, n+1):
    arr.append(input().strip())
for j in arr:
    newstring1 = newstring2 = ""
    for x in range (0, len(j)):
        if x%2 ==0:
            newstring1=newstring1+j[x]
        else:
            newstring2=newstring2+j[x]    
    print(newstring1+" "+newstring2)


#Чужое решение
for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
