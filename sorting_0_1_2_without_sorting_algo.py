


# code here
c1,c2,c3=[],[],[]
arr=[0,2,1,2,0]
for i in range(len(arr)):
   if arr[i]==0:
     c1.append(arr[i])
   elif arr[i]==1:
       c2.append(arr[i])
   elif arr[i]==2:
       c3.append(arr[i])
for i in range(len(c1)):
    arr[i]=0
for i in range(len(c1),len(c2)):
    arr[i]=1
for i in range(len(c2),len(c3)):
    arr[i]=2
print(*(c1+c2+c3))