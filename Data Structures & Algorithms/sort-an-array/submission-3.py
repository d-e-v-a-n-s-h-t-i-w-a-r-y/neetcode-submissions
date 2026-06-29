class Solution:
    def sortArray(self, nums):

        for i in range(1, len(nums)):
            key = nums[i]

            left, right = 0, i - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1

            j = i - 1

            while j >= left:
                nums[j + 1] = nums[j]
                j -= 1

            nums[left] = key

        return nums