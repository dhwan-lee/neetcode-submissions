class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        temp = ""

        for char in s:
            if char.isalnum():
                temp += char.lower()

        for j in range(len(temp) - 1, -1, -1):
            ptr1 = temp[i]
            if ptr1 != temp[j]:
                return False

            i += 1

        
        return True