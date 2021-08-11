x=input().split(' ')
print (x)
find1=str(input())
new_list=''
if find1 not in x:
    print ('None')
else:
    for i in range(len(x)):
        if (x[i]==find1):
            new_list=new_list+str(i)+' '
    print (new_list)


