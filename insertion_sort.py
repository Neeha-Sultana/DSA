"""
def bub_sort(lst1):
    for i in range(1,len(lst1)):
        for j in range(i,0,-1):
            print("i=",i,"j=",j,"lst1=",lst1)
            if lst1[j-1]>lst1[j]:
                lst1[j],lst1[j-1]=lst1[j-1],lst1[j]
    return lst1
lst = [10, 7, 9, 4, 20, 8]
print(bub_sort(lst))
"""
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            
            j=j-1
        arr[j+1]=key
    return arr
arr=[10, 7, 9, 4, 20, 8]
print(insertion_sort(arr))
        



