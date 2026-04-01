#Pattern
# Primary = Greedy (Lexicographic Permutation)
# Secondary = Two-Pointer (suffix reversal)

#Approach
# Traverse from right to find the first decreasing element (pivot).
# Swap it with the smallest element greater than it on the right side.
# Reverse the suffix to get the next smallest lexicographic permutation.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i != 0:
            index = i

            for j in range(n-1, i-1, -1):
                if nums[j] > nums[i - 1]:
                    index = j
                    break
            nums[i - 1], nums[index] = nums[index], nums[i-1]
        
        nums[i:] = reversed(nums[i:])

#Testcases
#[1,2,3],[3,2,1]