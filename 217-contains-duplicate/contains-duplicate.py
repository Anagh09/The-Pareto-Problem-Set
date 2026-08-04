class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using hashset for O(n) time and space complexity which is the best
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
        """
        normal double for loop takes too much time
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i] == nums[j]:
                    return True
        return False
        """
