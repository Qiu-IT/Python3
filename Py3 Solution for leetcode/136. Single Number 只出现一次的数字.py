Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(len(nums))
        print(nums)
        if len(nums) == 1:
            return nums[0]
        for i in range(0,len(nums),2):
            if i == len(nums)-1:
                return nums[i]
            if nums[i]!=nums[i+1]:
                return nums[i]
