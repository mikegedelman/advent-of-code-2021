import sys
from collections import deque


def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line)
    
    initial_lanternfish_states = [int(i.strip()) for i in input_lines[0].split(",")]
    lanternfish_hist = deque([0] * 9)
    for num_days in initial_lanternfish_states:
        lanternfish_hist[num_days] += 1

    for _ in range(256):
        num_new_lanternfish = lanternfish_hist.popleft()
        lanternfish_hist[6] += num_new_lanternfish
        lanternfish_hist.append(num_new_lanternfish)
    
    print("Number of lanternfish: ", sum(lanternfish_hist))


if __name__ == "__main__":
    main()
