#Question: sort colors (sorting o,1,2)
#pattern: sorting 

# Approch 
# use bubble sort to sort the entire array 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 1:
            return nums

        for j in range(n):
            i = 0
            while i < n - 1:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

                i += 1
    
        return nums
#Not optimal but works 

#pattern: Duch national flag (3 pointer)

#approch 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1