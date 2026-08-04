class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        countS, countT = {},{} # creating a two colum hash map

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #for key error incase the character is not present
            countT[t[i]] = 1 + countT.get(t[i], 0) #for key error incase the character is not present
        for c in countS:
            if countS[c] != countT.get(c, 0): 
                return False
        return True 
        """
        a one line code for basically doint the same thing
        return Counter(s) == Counter(t) 

        another way of doung it by using sorting 
        return sorted(s) == sorted(t)
        """
