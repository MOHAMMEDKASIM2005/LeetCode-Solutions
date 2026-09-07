class Solution:
    def floodFill(self, image, sr, sc, color):

        original = image[sr][sc]

        # If the color is already the same
        if original == color:
            return image

        def dfs(r, c):

            # Change current pixel
            image[r][c] = color

            # Up
            if r > 0 and image[r - 1][c] == original:
                dfs(r - 1, c)

            # Down
            if r < len(image) - 1 and image[r + 1][c] == original:
                dfs(r + 1, c)

            # Left
            if c > 0 and image[r][c - 1] == original:
                dfs(r, c - 1)

            # Right
            if c < len(image[0]) - 1 and image[r][c + 1] == original:
                dfs(r, c + 1)

        dfs(sr, sc)

        return image