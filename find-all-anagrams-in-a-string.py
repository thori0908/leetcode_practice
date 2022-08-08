class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size_s, size_p = len(s), len(p)
        if size_s < size_p:
            return []

        result = []
        window = len(p)
        counts_p = self.getCountsOf(p)
        counts_window_s = [0] * 26

        for i, letter in enumerate(s):
            counts_window_s[self.getNumberOf(letter)] += 1
            # windowの外になる分を引く
            if i >= window:
                counts_window_s[self.getNumberOf(s[i-window])] -= 1

            if counts_p == counts_window_s:
                result.append(i-window+1)

        return result

    def getCountsOf(self, string: str) -> List[int]:
        counts = [0] * 26
        for letter in string:
            counts[self.getNumberOf(letter)] += 1

        return counts

    def getNumberOf(self, letter: str) -> int :
        return ord(letter)-ord('a') # ordでunicodeの番号. -ord('a')でoffset
