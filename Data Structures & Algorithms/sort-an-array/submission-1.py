from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            val = nums[i]
            
            # Binary Search to find the position to insert nums[i]
            low = 0
            high = i - 1
            
            while low <= high:
                mid = (low + high) // 2
                if val < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            # The correct position is 'low'
            # We shift all elements to the right and insert the value
            nums[:] = nums[:low] + [val] + nums[low:i] + nums[i+1:]
            
        return nums