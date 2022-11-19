class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = "({["
        closing_brackets = ")}]"
        brackets_mapping = dict(zip(closing_brackets, opening_brackets))
        for current_char in s:
            if current_char in closing_brackets:
                # closing bracket
                if stack == []:
                    return False
                if stack[-1] == brackets_mapping[current_char]:
                    stack.pop()
                else:
                    return False
            else:
                # opening bracket
                stack.append(current_char)
        return stack == []
