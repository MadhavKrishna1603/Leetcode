class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            ans = nums.index(target)
            return ans
        

        elif target not in nums:
            nums.append(target)
            sorted_nums = nums.sort()
            ans = nums.index(target)
            return ans
