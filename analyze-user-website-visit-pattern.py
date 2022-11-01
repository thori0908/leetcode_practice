from collections import Counter
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pattern_counter = Counter()
        user_latest_visited_map = {}


        for user, time, page in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            latest_visited = user_latest_visited_map[user] if user in user_latest_visited_map else []

            if len(latest_visited) >= 3:
                latest_visited.pop()

            latest_visited.append(page)

            if len(latest_visited) == 3:
                pattern_counter.update(Counter(set(combinations(latest_visited, 3))))

            user_latest_visited_map[user] = latest_visited
        
        return max(sorted(pattern_counter), key=pattern_counter.get)