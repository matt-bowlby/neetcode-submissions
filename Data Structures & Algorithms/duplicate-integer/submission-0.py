class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup_set = set()

        for num in nums:
            if num in dedup_set:
                return True
            dedup_set.add(num)
        
        return False
