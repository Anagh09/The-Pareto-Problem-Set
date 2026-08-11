class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap
        freq = [[] for i in range(len(nums)+1)] #this is the bucket sort descending order array

        for n in nums:
            count[n] = 1+count.get(n,0) # this gets the count for each number in array
        for n, c in count.items():
            freq[c].append(n) #this gets the opposite that is count==>values
        
        res = []
        #cuz i want it in descending order i.e largest first
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # this if statement is supposed to be true at some point for sure
                if len(res) == k:
                    return res
