class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        pairs = [(num, freq) for num, freq in freq.items()]
        pairs.sort(key = lambda x: x[1], reverse = True)
        return [num for num, freq in pairs[:k]]