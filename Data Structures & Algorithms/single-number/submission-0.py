class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen =[]
        
        for x in nums:
            if x in seen:
                seen.remove(x)
            else:
                seen.append(x)

        return seen[0]
        