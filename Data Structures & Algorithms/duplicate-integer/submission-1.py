class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated_nums = []
        for num in nums:
            if num not in repeated_nums:
                repeated_nums.append(num)

            else:
                return True

        return False