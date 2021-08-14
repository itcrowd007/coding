#print (input().split())
#y=input()
#import re
#print(re.sub(r'\s+', '_', re.sub(r'^\s+(.+?)\s+$', r'\1', input())))
#print (len(x))
#print (x)
#find1=str(input())
#new_list=''
#if find1 not in x:
#    print ('None')
#else:
#    for i in range(len(x)):
#        if (x[i]==find1):
#            new_list=new_list+str(i)+' '
#    print (new_list)
sdvig=int(input())
tekst=input()
alphavit=(" abcdefghijklmnopqrstuvwxyz")
#print (alphavit[sdvig])
result=('')
for i in range(len(tekst)):
    for x in alphavit:
        if tekst[i]==x:
            #print (alphavit.index(x))
            num=alphavit.index(x)+sdvig
            
            if num >= len(alphavit):
                num=num-len(alphavit)
            result=result+alphavit[num]
print (result)

