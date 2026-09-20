class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}

        for char in s:
            ss[char] = ss.get(char, 0) + 1
        for char in t:
            tt[char] = tt.get(char, 0) + 1     

        return ss == tt    