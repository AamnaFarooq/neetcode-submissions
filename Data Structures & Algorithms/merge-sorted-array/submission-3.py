class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pt_zero = m 
        pt_nums = 0

        while pt_nums < n:
            nums1[pt_zero] = nums2[pt_nums]

            pt_zero += 1
            pt_nums += 1

        nums1.sort()
       

        



