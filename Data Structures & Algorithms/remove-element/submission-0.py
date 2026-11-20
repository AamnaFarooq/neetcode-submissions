class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = []
        for i in range(len(nums)):
            if nums[i] != val:
                k.append(nums[i])

        for i in range(len(k)):
            nums[i] = k[i]

        return len(k)
    