class Solution:
    def twoSum(self, nums, target):
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i], i))

        arr.sort()

        n = len(arr)

        for i in range(n):
            complement = target - arr[i][0]

            left = i + 1
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid][0] == complement:
                    return [arr[i][1], arr[mid][1]]

                elif arr[mid][0] < complement:
                    left = mid + 1

                else:
                    right = mid - 1