class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        s = s.lower()

        for char in s:
            if ord(char) not in range(97,122) and ord(char) not in range(48,57):
                s = s.replace(char,"")
  
        left = 0
        right = -1
        
        for i in range(0,len(s)):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True