#Shyfr Cezarya
def cezar (sdvig, tekst):

    alphavit=(" abcdefghijklmnopqrstuvwxyz")
    result=('')
    for i in range(len(tekst)):
        for x in alphavit:
            if tekst[i]==x:
                num=alphavit.index(x)+sdvig
                while num >= len(alphavit):
                    num=num-len(alphavit)
                while num < 0:
                    num=num+len(alphavit)
                result=result+alphavit[num]
    return print (f"Result: \"{result}\"")

sdvig=int(input().strip())
text=input().strip()

cezar (sdvig, text)

