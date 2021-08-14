#variant s funktsiei
def cezar (sdvig, tekst):

    alphavit=(" abcdefghijklmnopqrstuvwxyz")
    result=('')
    for i in range(len(tekst)):
        for x in alphavit:
            if tekst[i]==x:
                num=alphavit.index(x)+sdvig
                if num >= len(alphavit):
                    num=num-len(alphavit)
                result=result+alphavit[num]
    return print (result)

sdvig=int(input())
text=input()

cezar (sdvig, text)

'''
#1 variant resheniaya

sdvig=int(input())
text=input()

alphavit=(" abcdefghijklmnopqrstuvwxyz")
result=('')
for i in range(len(tekst)):
    for x in alphavit:
        if tekst[i]==x:
            num=alphavit.index(x)+sdvig
            if num >= len(alphavit):
                num=num-len(alphavit)
            result=result+alphavit[num]

print (result)
'''
