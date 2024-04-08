'''
#Memoization
def get_lis(arr,dp,n,ind,prev_ind):
    if ind==n:
        return 0
    if dp[ind][prev_ind+1]!=-1:
        return dp[ind][prev_ind+1]
    not_take=0+get_lis(arr,dp,n,ind+1,prev_ind)
    take=0
    if prev_ind==-1 or arr[ind]>arr[prev_ind]:
        take =1+get_lis(arr,dp,n,ind+1,ind)
    dp[ind][prev_ind+1]=max(take,not_take)
    return dp[ind][prev_ind+1]
def lis(arr):
    n=len(arr)
    dp=[[-1 for _ in range(n+1)] for _ in range(n)]
    return get_lis(arr,dp,n,0,-1)
arr=[10, 9, 2, 5, 3, 7, 101, 18]
print(lis(arr))



'''

#tabulation
def lis(arr):
    n = len(arr)
    lis_lengths = [1] * n
    lis_sequences = [[arr[i]] for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1
                lis_sequences[i] = lis_sequences[j] + [arr[i]]

    max_length_index = lis_lengths.index(max(lis_lengths))
    lis_sequence = lis_sequences[max_length_index]

    return lis_sequence

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Longest Increasing Subsequence:", lis(arr))
print("Length of LIS is", len(lis(arr)))
