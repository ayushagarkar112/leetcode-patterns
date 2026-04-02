#Question: Maximum subarray
#pattern: kanades algorithm

# Approch 
# use a var sum to store the sum as you go throuhg the array
# if the sum is greater than max_sum (biggest sum found ) update it 
# if the sum goes below 0 sum is reset to 0 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        sum=0

        for num in nums:
            sum+=num
            if max_sum<sum:
                max_sum=sum
            if sum <0:
                sum=0
        return max_sum