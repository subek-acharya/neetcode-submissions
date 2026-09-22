class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_a = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict_a:
                return [dict_a[diff], i]
            dict_a[n] = i
        return
         