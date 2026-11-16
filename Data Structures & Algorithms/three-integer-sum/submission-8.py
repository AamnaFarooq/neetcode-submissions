class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        soln = sorted(nums)
        result = []

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1

            while j < k:
                total = soln[i] + soln[j] + soln[k]
                
                if total > 0:
                    k -= 1


                elif total < 0:
                    j += 1
                    
                else: 
                    sum3 = [soln[i],soln[j],soln[k]]

                    if sum3 not in result:
                        result.append(sum3)

                    j += 1
                    k -= 1


        return result
       
