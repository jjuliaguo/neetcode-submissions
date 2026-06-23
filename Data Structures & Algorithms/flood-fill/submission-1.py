class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        #place here because it stops the code before dfs even starts
        #example 2 shows that to only start if starting pixel not same as target pixel
        if orig == color:
            return image

        m, n = len(image), len(image[0])

        #recursive step is to fill each cell (not filling out entire image again)
        def dfs(r, c):
            #instead of r<0 and c<0, you can use (min(r, c) < 0
            #checks out of bounds (either too left, right, up, or down)
            #read the question correctly because it's also only checking
            #for the ones that have same color as start hence != orig
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return

            #this is where you're actually changing the color
            image[r][c] = color
            #moves in every direction
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image