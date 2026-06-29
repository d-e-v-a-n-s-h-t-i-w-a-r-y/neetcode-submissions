class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(1, n):
            key = nums[i]

            # Binary search for insertion position
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= key:
                    left = mid + 1
                else:
                    right = mid

            # Shift elements
            j = i
            while j > left:
                nums[j] = nums[j - 1]
                j -= 1

            nums[left] = key