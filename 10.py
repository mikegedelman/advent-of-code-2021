import sys

open_to_close = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

error_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

autocomplete_score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def check_syntax(line):
    stack = []
    for ch in line:
        if ch in open_to_close.keys():
            stack.append(ch)
        elif ch in open_to_close.values():
            top_stack = stack.pop()
            if ch != open_to_close[top_stack]:
                return error_score[ch]
    
    return 0


def complete_line(line):
    stack = []
    for ch in line:
        if ch in open_to_close.keys():
            stack.append(ch)
        elif ch in open_to_close.values():
            top_stack = stack.pop()
            if ch != open_to_close[top_stack]:
                raise ValueError(line)
    
    to_complete = []
    while stack:
        to_complete.append(open_to_close[stack.pop()])
    
    score = 0
    for char in to_complete:
        score *= 5
        score += autocomplete_score[char]
    
    return score

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line)

    incomplete_lines = []
    error_score = 0
    for line in input_lines:
        score = check_syntax(line)
        if score == 0:
            incomplete_lines.append(line)
        error_score += score

    print("Error score: ", error_score)

    autocomplete_scores = sorted(complete_line(line) for line in incomplete_lines)
    print("Middle autocomplete score: ", autocomplete_scores[int(len(autocomplete_scores) / 2)])

main()
