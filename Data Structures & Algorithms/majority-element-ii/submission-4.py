class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        ans = []
        limit = len(nums) // 3

        # Find majority elements
        for num in count:
            if count[num] > limit:
                ans.append(num)

        return ans