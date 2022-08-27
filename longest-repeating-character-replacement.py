class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # [a=>0,b=>0,c=>0,...]
        counters = [0] * 26
        head = 0
        max_length = 0
        for tail, tail_letter in enumerate(s):
            # tailとheadが同じ位置だと、文字数は1なので注意
            window_size = tail - head + 1
            tail_letter_index = ord(tail_letter) - ord('A')
            counters[tail_letter_index] += 1

            if window_size - max(counters) <= k:
                if window_size > max_length:
                   max_length = window_size
            else:
                head_letter = s[head]
                head_letter_index = ord(head_letter) - ord('A')
                counters[head_letter_index] -= 1
                head += 1
        

        return max_length
