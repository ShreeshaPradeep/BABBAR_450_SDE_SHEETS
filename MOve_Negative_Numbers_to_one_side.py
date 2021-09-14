a = list(map(int,input().split()))
b = []
c = []
for i in range(len(a)):
    if a[i]<0:
        b.append(a[i])
    else:
        c.append(a[i])
#print("b = ",b,"c = ",c)

for i in range(len(b)):
   a[i]=b[i]
   print(i)
j=0
for i in range(len(b),len(a)):
        a[i]=c[j]
        j=j+1

print(a)

