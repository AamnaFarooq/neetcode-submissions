class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        sorts = []
  
        for key in nums:
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
        
        sorts = sorted(count, key=count.get, reverse=True)

        return sorts[:k]
