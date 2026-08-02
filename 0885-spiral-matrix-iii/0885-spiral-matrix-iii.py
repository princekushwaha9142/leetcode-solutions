class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        result = []
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = rStart, cStart
        step = 1
        while len(result) < rows * cols:
            for i, (dx, dy) in enumerate(directions):
                for _ in range(step):
                    if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                        result.append([x, y])
                        visited.add((x, y))
                    x += dx
                    y += dy
                if i == 1 or i == 3:
                    step += 1
        return result