class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #cycle through the first index, and sum all until meets target value
        #else sum the next index
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
