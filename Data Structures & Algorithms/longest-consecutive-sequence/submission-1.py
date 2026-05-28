class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        res = 0

        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in d:
            if i - 1 not in d:
                resT = 1
                t = i + 1
                while t in d:
                    resT += 1
                    t += 1
                res = max(res, resT) 
        return res