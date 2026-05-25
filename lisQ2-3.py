class Solution:
    def longestIncreasing(self, nums):
        if len(nums) == 0:
            return 0
        # storing increasing numbers
        arr = []
        for num in nums:
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] < num:
                    start = mid + 1
                else:
                    end = mid - 1
            # adding number in list
            if start == len(arr):
                arr.append(num)
            else:
                arr[start] = num
        # final answer
        return len(arr)
    # to get 0 we have to keep list empty
nums = []
s = Solution()
print(s.longestIncreasing(nums))