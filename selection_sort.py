
def selec_sort(lst1):
    for i in range(len(lst1)):
        sm = lst1[i]
        x = i
        print("i=", i)
        for j in range(i+1, len(lst1)):
            if sm > lst1[j]:
                sm = lst1[j]
                x = j

        # Move the following two lines outside the inner loop
        lst1[x] = lst1[i]
        lst1[i] = sm
        print(lst1)

    return lst1

lst = [10, 7, 9, 4, 20, 8]
print(selec_sort(lst))

