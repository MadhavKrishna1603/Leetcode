class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        

        rev_s = s[::-1]
        a = 0
        x=rev_s.split()
        s_first=x[0]
        for i in s_first:
            a += 1
        return a
