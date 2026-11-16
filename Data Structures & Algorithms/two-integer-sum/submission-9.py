class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        nums_dict = {}
        for i,val in enumerate(nums):
            nums_dict[val] = i

        for i,val in enumerate(nums):
            diff = target - val
            if diff in nums_dict and nums_dict[diff] != i:
                return [i,nums_dict[diff]]
        return []