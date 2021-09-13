arr = list(map(int,input().split()))
a = int(input())
arr.sort(reverse=True)
print(arr[a-1])