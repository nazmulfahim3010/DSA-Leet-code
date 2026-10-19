class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if not words or not s:
            return []
        word_len = len(words[0])
        n = word_len * len(words)
        si = Counter(words)
        left, right = 0, n - 1
        result = []
        while right < len(s):
            window = s[left:right + 1]
# Counting word by word len for words lists sub strings
            temp = Counter(
                window[i:i + word_len]
                for i in range(0, len(window), word_len)
            )
            if temp == si:
                result.append(left)
            left += 1
            right += 1
        return result