import sys

class Board:
    def __init__(self, lines):
        self.data = []
        for line in lines:
            self.data.append([int(s.strip()) for s in line.split(" ") if s])
    
    def num_moves_to_win(self, bingo_numbers):
        self.hits = [[0 for _ in range(5)] for _ in range(5)]

        num_moves = 0
        for bingo_number in bingo_numbers:
            num_moves += 1
            for row_idx, row in enumerate(self.data):
                for col_idx in range(len(row)):
                    if self.data[row_idx][col_idx] == bingo_number:
                        self.hits[row_idx][col_idx] = 1
            
            if self.is_win():
                self.winning_number = bingo_number
                return num_moves
    
    def is_win(self):
        return any(sum(x) == 5 for x in self.hits) or any(sum(x) == 5 for x in zip(*self.hits))
    
    def score(self):
        unmarked_score = 0
        for row_idx, row in enumerate(self.hits):
            for col_idx in range(len(row)):
                if self.hits[row_idx][col_idx] == 0:
                    unmarked_score += self.data[row_idx][col_idx]
        
        return unmarked_score * self.winning_number

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    
    bingo_numbers = [int(num) for num in lines[0].split(",")]

    cur_line = 2
    boards = []
    while cur_line < len(lines):
        boards.append(Board(lines[cur_line:cur_line+5]))
        cur_line += 6
    
    moves_per_board = {}
    for idx, board in enumerate(boards):
        moves_per_board[idx] = board.num_moves_to_win(bingo_numbers)
    
    best_board_idx = min(moves_per_board, key = moves_per_board.get)
    best_board = boards[best_board_idx]
    worst_board_idx = max(moves_per_board, key = moves_per_board.get)
    worst_board = boards[worst_board_idx]

    print("Best board score: ", best_board.score())
    print("Worst board score: ", worst_board.score())


if __name__ == "__main__":
    main()