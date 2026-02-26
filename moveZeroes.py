"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements. Note that you must do this in-place without making a copy of the array."""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos = insert_pos+1
            else:
                continue
        for i in range(insert_pos,len(nums)):
            nums[i] = 0
        return nums
# ---------------------------------------------------
# Solution 2 - inplace swapping
# ---------------------------------------------------

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         insert_pos = 0
        
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
#                 insert_pos += 1