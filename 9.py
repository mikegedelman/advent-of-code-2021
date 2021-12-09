import functools
import heapq
import sys
from dataclasses import dataclass
from queue import SimpleQueue

@dataclass
class Point:
    row: int
    col: int

    def value(self, lines):
        return lines[self.row][self.col]
    
    def surrounding(self, lines):
        """Return a list of points surrounding this point."""
        surrounding = []
        if self.col > 0:
            surrounding.append(Point(self.row, self.col - 1))
        if self.col < len(lines[self.row]) - 1:
            surrounding.append(Point(self.row, self.col + 1))

        if self.row > 0:
            prev_line = lines[self.row - 1]
            from_col = max(self.col - 1, 0)
            to_col = min(self.col + 2, len(prev_line))
            surrounding += [Point(self.row - 1, col) for col in range(from_col, to_col)]

        if self.row < len(lines) - 1:
            next_line = lines[self.row + 1]
            from_col = max(self.col - 1, 0)
            to_col = min(self.col + 2, len(next_line))
            surrounding += [Point(self.row + 1, col) for col in range(from_col, to_col)]

        return surrounding
    

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))
    
    def __repr__(self):
        return f"({self.row}, {self.col})"


def bfs(lines, root):
    """Return a list of points that represents a basin."""
    basin_points = {root}
    q = SimpleQueue()
    q.put(root)

    while not q.empty():
        cur = q.get()
        cur_val = cur.value(lines)

        for adjacent in cur.surrounding(lines):
            adj_val = adjacent.value(lines)
            if adj_val < 9 and adj_val == (cur_val + 1):
                basin_points.add(adjacent)
                q.put(adjacent)
    
    return list(basin_points)


def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line)
    
    int_lines = [[int(x) for x in line.strip()] for line in input_lines]
    
    low_points = []
    for row, line in enumerate(int_lines):
        for col, _ in enumerate(line):
            point = Point(row, col)
            surrounding = point.surrounding(int_lines)
            if all(point.value(int_lines) < neighbor.value(int_lines) for neighbor in surrounding):
                low_points.append(Point(row, col))

    print("Risk sum: ", sum(p.value(int_lines) + 1 for p in low_points))
    basin_sizes = []
    for low_point in low_points:
        basin = bfs(int_lines, low_point)
        basin_sizes.append(len(basin))

    # basins = [bfs(int_lines, p) for p in low_points]
    # for basin in basins:
    #     print(basin)
    largest_3_basins = heapq.nlargest(3, basin_sizes)
    print(len(basin_sizes))
    print(largest_3_basins)
    print("Largest 3 basins multiplied: ", functools.reduce(lambda a, b: a * b, largest_3_basins))

main()
