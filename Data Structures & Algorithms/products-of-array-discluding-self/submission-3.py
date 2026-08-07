class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        prod = 1
        zeros = 0
        before_product = 1

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeros += 1

        if zeros > 1:
            return [0]*len(nums)

        res = [0] * len(nums)

        for index, value in enumerate(nums):
            if zeros == 1:
                if value == 0:
                    res[index] = prod
                else:
                    res[index] = 0

            else:
                res[index] = prod//value
        

        return res
