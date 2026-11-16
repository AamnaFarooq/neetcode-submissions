class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = []
        current_seq = 1
        sorted_list = sorted(nums)
        if len(nums) == 0:
            return 0
        for num in range(1, len(sorted_list)):
            if sorted_list[num] > sorted_list[num-1] + 1:
                longest_seq.append(current_seq)
                current_seq = 1
            
            if sorted_list[num] == sorted_list[num-1] + 1:
                current_seq += 1

        longest_seq.append(current_seq)
        return max(longest_seq)

