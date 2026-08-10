class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of anagrams
        
        for s in strs:
            count = [0]*26 #a-z
            #this is for each character in the string
            for c in s: 
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s) 
            #for each string it is tupled to similar matches

        return list(res.values())