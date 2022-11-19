class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in mem:
                return [mem[remaining], idx]
            mem[num] = idx
        return []
