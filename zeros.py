arr = [int(i) for i in input().split()]
i = 0
for i in range(len(arr)-1):
    for j in range(i,len(arr)):
        if arr[i]==0 and arr[j]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            break
print(arr)
