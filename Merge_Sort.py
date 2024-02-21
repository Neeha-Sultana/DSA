def mergesort(arr,low,high):
    med=(low+high)//2
    if low==high:
        return
    mergesort(arr,low,med)
    mergesort(arr,med+1,high)
    merge(arr,low,med,high)
    return arr
def merge(arr,low,med,high):
    x1=low
    x2=med+1
    tempp=[]
    while(x1<=med and x2<=high):
        if arr[x1]<=arr[x2]:
            tempp.append(arr[x1])
            x1+=1
        else:
            tempp.append(arr[x2])
            x2+=1

    while(x1<=med):
        tempp.append(arr[x1])
        x1+=1
    while(x2<=high):
        tempp.append(arr[x2])
        x2+=1

    for i in range(low,high+1):
        arr[i]=tempp[i-low]
        
 
print(mergesort([1,2,34,5,2,1,55,4],0,7))
    
            
