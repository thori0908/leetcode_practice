class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphicMap = {}
        is_isomorphic = True

        for index, s_char in enumerate(s):
            letter = isomorphicMap.get(s_char) # dictはisomorphicMap[s_char]は存在しないキーの時、エラーが出る
            if letter != t[index]:
                is_isomorphic = False
                break

            if letter in isomorphicMap.values:
                is_isomorphic = False
                break

            if letter == None:
                isomorphicMap[s_char] = t[index]

        return is_isomorphic 



        # if s = egg, t = add, then {"e" : "a", "g" : "d"}
        # s= badc, t= baba {b:b, a:a, d:b, c:a }
        