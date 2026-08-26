class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {} #val:index 
        #a one-pass hash table 
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff]+1, i+1]
            prevMap[n] = i
        return