class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for c in s :
            if c.isalnum() :
                new_string += c.lower()
        if new_string[::-1] == new_string :
            return True
        return False