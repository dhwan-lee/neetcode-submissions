class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ["{", "[", "("]
        stack = []
        for char in s:
            
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if char == ")" and top != "(":
                    return False
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False
        
        return not stack

