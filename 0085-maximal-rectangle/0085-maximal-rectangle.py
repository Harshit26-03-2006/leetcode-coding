class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        ans = 0
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans