class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > len(nums) // 3 and num not in res:
                res.append(num)

        return res