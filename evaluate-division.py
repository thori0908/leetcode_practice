from collections import defaultdict
from operator import ne


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1/value
        
        answers = []
        for query in queries:
            numer = query[0]
            denom = query[1]
            if numer not in graph or denom not in graph:
                answers.append(-1.0)
            elif numer == denom:
                answers.append(1.0)
            else:
                answer = self.answer(numer, denom, graph)
                answers.append(answer)
    
    def answer(self, current: float, target: float, graph: dict[str, dict[str, float]]) -> float:
        self.backtrack(current, target, graph[current], set())

    def backtrack(self, current: float, target: float, graph: dict[str, dict[str, float]], visited: set[str]) -> float:
        neighbors = graph[current]
        result = current
        stack = []

        # choose a neighbor
        # if visited
        #
        for neighbor in neighbors:
            neighbor in visited

