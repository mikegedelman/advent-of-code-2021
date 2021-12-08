import sys

def get_fuel_cost(from_pos, to_pos):
    dist = abs(from_pos - to_pos)
    return int((dist * (dist + 1)) / 2)

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line)
    
    horiz_positions = [int(s.strip()) for s in input_lines[0].split(",")]

    max_horiz = max(horiz_positions)
    fuel_costs = {}
    for align_to_horiz in range(max_horiz):
        fuel_cost = 0
        for crab_pos in horiz_positions:
            fuel_cost += get_fuel_cost(crab_pos, align_to_horiz)
        
        fuel_costs[align_to_horiz] = fuel_cost
    
    best_align_to = min(fuel_costs, key=fuel_costs.get)
    print("best: ", best_align_to, f"({fuel_costs[best_align_to]})")

if __name__ == "__main__":
    main()
