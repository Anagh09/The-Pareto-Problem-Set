class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]        
        
        """
        cleaned = []

        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())

        i = 0
        j = len(cleaned) - 1

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False

            i += 1
            j -= 1

        return True
        """