'''
def selec_sort(lst1):
    for i in range(len(lst1)):
        sm = lst1[i]
        x = i
        for j in range(i+1, len(lst1)):
            if sm > lst1[j]:
                sm = lst1[j]
                x = j
        # Move the following two lines outside the inner loop
        lst1[x] = lst1[i]
        lst1[i] = sm
    return lst1 
lst = [10, 7, 9, 4, 20, 8]
print(selec_sort(lst))
'''

def SelectSort(arr):
    for i in range(len(arr)):
        sm=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[sm]:
                sm=j
        arr[i],arr[sm]=arr[sm],arr[i]
    return arr
                
