class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for val in tokens:
            if val in operators:
                operend2 = int(stack.pop())
                operend1 = int(stack.pop())
                
                if val == operators[0]:
                    new_value = operend1 + operend2
                elif val == operators[1]:
                    new_value = operend1 - operend2
                elif val == operators[2]:
                    new_value = operend1 * operend2
                elif val == operators[3]:
                    new_value = int(operend1 / operend2)
                stack.append(new_value)
            else:
                stack.append(int(val))
        
        return stack.pop()