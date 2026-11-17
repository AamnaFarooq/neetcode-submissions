class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        nums_copy = nums[:]

        while left < len(nums_copy):
            if len(nums) == 1:
                break
            if nums_copy[left] == nums_copy[left-1]:
                nums.remove(nums_copy[left])

            left += 1

        return len(nums)