class Solution:
    def findLongest(self, nums):
        list1 = []
        for i in nums:
            start = 0
            end = len(list1) - 1
            # looking for a position
            while start <= end:
                mid = (start + end) // 2
                if list1[mid] < i:
                    start = start + 1
                else:
                    end = mid - 1
            #value adding
            if start >= len(list1):
                list1.append(i)
            else:
                list1[start] = i
        return len(list1)

a = [7,7,7,7,7]
obj = Solution()
print(obj.findLongest(a))