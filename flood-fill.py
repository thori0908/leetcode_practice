class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_size = len(image)
        column_size = len(image[0])

        flooded_stack = []
        flooded_stack.append((sr, sc))

        start_color = image[sr][sc]

        # これがないと無限ループになる
        if start_color == color:
            return image

        while flooded_stack:
            # pop a pixel from stack
            (row, column) = flooded_stack.pop()
            # flood the pixel
            image[row][column] = color
            # push pixels if the color is start_color
            # up (row - 1, column)
            if row-1 >= 0 and image[row - 1][column] == start_color:
                flooded_stack.append((row - 1, column))
            # down (row + 1, column)
            if row + 1 <= row_size - 1 and image[row + 1][column] == start_color:
                flooded_stack.append((row + 1, column))
            # left (row, column-1)
            if column - 1>= 0 and image[row][column-1] == start_color:
                flooded_stack.append((row, column-1))
            # right (row, column+1)
            if column + 1 <= column_size - 1 and image[row][column+1] == start_color:
                flooded_stack.append((row, column+1))
           

        return image