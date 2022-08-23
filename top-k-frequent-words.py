

import heapq
from typing import List

class Element:
    def __init__(self, count: int, word: str) -> None:
        self.count = count
        self.word = word
    
    def __lt__(self, other: 'Element') -> bool:
        if self.count == other.count:
            return self.word > other.word # たぶん、aの順番 < bの順番だから、逆になっている
        else:
            return self.count < other.count

    def __eq__(self, other: 'Element') -> bool:
        return self.count == other.count and self.word == other.word

    

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencyMap = {}
        for word in words:
            if frequencyMap.get(word) != None:
                frequencyMap[word] += 1
            else:
                frequencyMap[word] = 0
        queue = []
        heapq.heapify(queue)

        for word, frequency in frequencyMap.items():
            heapq.heappush(queue, Element(frequency, word))
            if len(queue) > k:
                heapq.heappop(queue)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(queue).word)

        return result[::-1]
        

# alphabeticalにするために、Elementなどのクラスを定義するしかなさそう
# https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)