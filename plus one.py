class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(map(str,digits)))
        ans = a+1
        real_ans = list(map(int,str(ans)))
        return real_ans
