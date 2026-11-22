class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        best = 0
        result = 0
        for keys in count:
            if count[keys] > best:
                best = count[keys]
                result = keys

        return result
        