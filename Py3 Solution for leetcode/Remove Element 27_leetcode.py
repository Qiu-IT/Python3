class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        for i in range(l-1,-1,-1):
            if nums[i] == val:
                del nums[i]