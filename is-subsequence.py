class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True

        if s == "" and t != "":
            return True

        if s != "" and t == "":
            return False
        
        queue = []
        for char_s in s:
            queue.append(char_s)

        for char_t in t:
            if len(queue) == 0:
                break
            next_s = queue[0]
            if (next_s == char_t):
                queue.pop(0)

        return len(queue) == 0

        # queue = [a,b,c]
        # a ->b ->c

        # s = "a b  c"
        # t = "ahbgdc"
        # エッジケースがややこしい