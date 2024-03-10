def bub_sort(arr,x):
    if x==1:
        return
    for j in range(0,x-2):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    bub_sort(arr,x-1)
    return arr
print(bub_sort([2,54,21,1,556],5))
