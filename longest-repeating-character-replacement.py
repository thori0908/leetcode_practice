class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        letter_counters = [0] * 26
        left = 0
        for right, right_letter in enumerate(s):
            window = right-left+1 # 文字数
            letter_counters[self.getIndexOf(right_letter)] += 1
            # counters of window_s
            if window <= max(letter_counters) + k:
                if result <= window:
                    result = window
            else:
                letter_counters[self.getIndexOf(s[left])] -= 1
                left += 1

        return result

    def getIndexOf(self, letter: str) -> int:
        return ord(letter) - ord('A')
