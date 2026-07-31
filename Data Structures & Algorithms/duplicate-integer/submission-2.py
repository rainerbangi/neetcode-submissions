class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        main_check = set()
        for n in nums:
            if n in main_check:
                return True
            main_check.add(n)
        return False