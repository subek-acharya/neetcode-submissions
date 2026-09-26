class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hash_set = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in hash_set:
                stack.append(int(token)) # push numbers to stack
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+":
                    result = val1 + val2
                elif token == "-":
                    result = val1 - val2
                elif token == "*":
                    result = val1 * val2
                else:  # token == "/"
                    result = int(val1 / val2)         # Truncate toward zero
                
                stack.append(result)
                
        return stack.pop()

    


        