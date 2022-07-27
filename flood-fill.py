class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        columns = len(image[0])

        query_color = image[sr][sc]
        queue = [(sr, sc)] 

        if query_color == color:
            return image

        while queue:
            i, j = queue.pop()
            if image[i][j] == query_color:
                image[i][j] = color
            else:
                continue

            if j-1 >= 0:
                queue.append((i, j-1))
            if j+1 <= columns-1:
                queue.append((i, j+1))
            if i+1 <= rows-1:
                queue.append((i+1, j))
            if i-1 >= 0:
                queue.append((i-1, j))
        return image

    # 重なった点をどうするか