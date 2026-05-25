def findPlace(arr, num):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        # checking middle value
        if arr[m] < num:
            l = m + 1
        else:
            r = m - 1
    return l
def lis(nums):
    temp = []
    for i in nums:
        # finding correct position
        p = findPlace(temp, i)
        # print
        if p == len(temp):
            temp.append(i)
        else:
            temp[p] = i
        # print( temp)
    return len(temp)

a = [0,1,0,3,2,3]
ans = lis(a)
print(ans)