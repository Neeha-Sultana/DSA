"""
#BruteForce
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-sys.maxsize - 1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                summ=0
                for k in range(i,j+1):
                    summ=summ+nums[k]
                    
                    if summ>maxi:
                        maxi=summ
        return maxi
    
#Better
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-sys.maxsize - 1
        n=len(nums)
        for i in range(n):
            summ=0
            for j in range(i,n):
                summ=summ+nums[j]
                if summ>maxi:
                    maxi=summ
                    
        return maxi
"""
#Optimal
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-sys.maxsize-1
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            
            if summ>maxi:
                maxi=summ
                
            if summ<0:
                summ=0
                
        return maxi
        
