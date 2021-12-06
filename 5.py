import sys
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    @staticmethod
    def from_str(s):
        [x_str, y_str] = s.split(",")
        return Point(int(x_str), int(y_str))

@dataclass
class Line:
    begin: Point
    end: Point

    @staticmethod
    def from_str(s):
        [begin_str, end_str] = s.split(" -> ")
        return Line(Point.from_str(begin_str), Point.from_str(end_str))


def plot_line(plot, line):
    if line.begin.y == line.end.y:
        for x_coord in range(min(line.begin.x, line.end.x), max(line.begin.x, line.end.x) + 1):
            plot[line.begin.y][x_coord] += 1
    elif line.begin.x == line.end.x:
        for y_coord in range(min(line.begin.y, line.end.y), max(line.begin.y, line.end.y) + 1):
            plot[y_coord][line.begin.x] += 1
    else:
        # diagonal cases:
        #   positive slope: (1, 1) -> (5, 5). Add one to each coord every step.
        #   negative slope: (0, 8) -> (8, 0). X coord increasing, Y coord decreasing.
        slope = int((line.end.y - line.begin.y) / (line.end.x - line.begin.x))
        assert slope in (1, -1)
        
        if line.begin.x < line.end.x:
            begin_point = line.begin
            end_point = line.end
        else:
            begin_point = line.end
            end_point = line.begin

        cur_point = begin_point
        while cur_point.x <= end_point.x:
            plot[cur_point.y][cur_point.x] += 1
            cur_point = Point(cur_point.x + 1, cur_point.y + slope)



def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line)

    lines = []
    max_coord = 0
    for input_line in input_lines:
        line = Line.from_str(input_line)
        lines.append(line)
        max_coord = max(max_coord, line.begin.x)
        max_coord = max(max_coord, line.end.x)
        max_coord = max(max_coord, line.begin.y)
        max_coord = max(max_coord, line.end.y)
    
    plot = [[0 for _ in range(max_coord + 1)] for _ in range(max_coord + 1)]
    for line in lines:
        plot_line(plot, line)

    num_overlaps = 0
    for i in range(max_coord + 1):
        for j in range(max_coord + 1):
            if plot[i][j] > 1:
                num_overlaps += 1
    
    # for row in plot:
    #     for col in row:
    #         print("." if col == 0 else col, end="")
    #     print("")
        
    print("Number of intersections: ", num_overlaps)

if __name__ == "__main__":
    main()