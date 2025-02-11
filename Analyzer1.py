class Solution:
    def removeOccurrences(self, text: str, pattern: str) -> str:
        stack = []
        pattern_length = len(pattern)
        last_char = pattern[-1]

        for char in text:
            stack.append(char)

            if char == last_char and len(stack) >= pattern_length:
                if "".join(stack[-pattern_length:]) == pattern:
                    del stack[-pattern_length:]

        return "".join(stack)
