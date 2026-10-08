class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        
        for i, num in enumerate(nums):
            leftover = target - num
            index = nums_dict.get(leftover)
            if index is not None and index != i:
                return [min(index, i), max(index, i)]
        
        return []