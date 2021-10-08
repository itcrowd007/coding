my_dict={}
for n in range(int(input().strip())): s=input().split(); my_dict[s[0]]=s[1]
g=""
while g!=None:
    try:
        g=input().strip()
        if my_dict.get(g) !=None:
            print(f"{g}={my_dict.get(g)}")
        else:
            print("Not found")
    except:
        break
