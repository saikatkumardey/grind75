class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        nrows = len(image)
        ncols = len(image[0])

        def get_neighbors(x, y):

            dx = (1, -1, 0, 0)
            dy = (0, 0, 1, -1)

            for dx, dy in zip(dx, dy):
                if 0 <= x + dx < nrows and 0 <= y + dy < ncols:
                    yield x + dx, y + dy

        def dfs(row, col):
            original_color = image[row][col]
            image[row][col] = color
            for nx, ny in get_neighbors(row, col):
                if image[nx][ny] == original_color:
                    dfs(nx, ny)

        if image[sr][sc] != color:
            dfs(sr, sc)

        return image
