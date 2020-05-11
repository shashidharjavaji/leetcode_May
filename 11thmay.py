class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        k = len(image)
        m = len(image[0])
        def dfs(x, y, prev_color):
            if x < 0 or x >= k or y < 0 or y >= m: 
                return
            if image[x][y] != prev_color or image[x][y] == newColor:
                return
            # fill ..
            image[x][y] = newColor
            # .. recursively
            dfs(x - 1, y, prev_color)
            dfs(x, y - 1, prev_color)
            dfs(x, y + 1, prev_color)
            dfs(x + 1, y, prev_color)
            
        dfs(sr, sc, image[sr][sc])
        
        return image
