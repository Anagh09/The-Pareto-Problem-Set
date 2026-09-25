class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l<=r:
            #incase rotation is 0 or the array is now ascending
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return res
        #run time is O(log_2 n)
        