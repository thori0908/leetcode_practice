class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counters = [0] * 26
        for letter in p:
            letter_index = ord(letter) - ord('a')
            p_counters[letter_index] += 1

        window_counters = [0] * 26
        p_size = len(p)
        head = 0
        results = []
        for tail, tail_letter in enumerate(s):
            # increment tail
            tail_index = ord(tail_letter) - ord('a')
            window_counters[tail_index] += 1
            # decrement head
            if tail+1 > p_size:
                head_index = ord(s[head]) - ord('a')
                window_counters[head_index] -= 1
                head += 1
            
            if p_counters == window_counters:
                results.append(head)

        return results
