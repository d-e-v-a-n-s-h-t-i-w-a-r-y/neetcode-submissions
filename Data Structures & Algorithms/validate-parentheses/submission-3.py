class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for ch in s:
            if ch in pairs:
                # Opening bracket
                stack.append(ch)
            else:
                # Closing bracket
                if not stack:
                    return False

                top = stack.pop()

                if pairs[top] != ch:
                    return False

        return len(stack) == 0