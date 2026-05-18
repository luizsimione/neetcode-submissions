class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSub = set(nums)
        longest = 0

        for i in nums:
            if (i-1 not in maxSub):
                length = 0
                while(i + length) in maxSub:
                    length += 1
                longest = max(length, longest)
        return longest