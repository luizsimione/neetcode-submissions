class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars1 = {}
        chars2 = {}
        for char in s:
            if char not in chars1:
                chars1[char] = 1
            else:
                chars1[char] += 1

        for char in t:
            if char not in chars2:
                chars2[char] = 1
            else:
                chars2[char] += 1
        
        return chars1 == chars2
