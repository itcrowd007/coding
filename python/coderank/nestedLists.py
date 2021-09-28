spisok2=[]
#Formiruem nested list
for _ in range(int(input())):
     spisok1=[]
     spisok1.append(input())
     spisok1.append(float(input()))
     spisok2.append(spisok1)
#formiruem spisok score
arr=[]
for inner in spisok2:
     arr.append(inner[1])
#nahodim second minimalnoe score 
arr = list(set(arr))
arr.remove(min(arr))
min_score=min(arr)
#formiruem spisok studentov, sortiruem s vyvodim
students=[]
for inner in spisok2:
      if min_score in inner:
          students.append(inner[0])
students.sort()
for student in students:
    print(student)
