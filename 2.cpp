#include <iostream>

struct Position {
    int horizontal = 0;
    int depth = 0;
    int aim = 0;
};

void update_position_part1(Position &pos, std::string command) {
    std::string direction = command.substr(0, command.find(" "));
    std::string value_str = command.substr(command.find(" ") + 1, command.size());
    int value = std::stoi(value_str);

    if (direction == "forward") {
        pos.horizontal += value;
    } else if (direction == "down") {
        pos.depth += value;
    } else if (direction == "up") {
        pos.depth -= value;
    }
}


void update_position_part2(Position &pos, std::string command) {
    std::string direction = command.substr(0, command.find(" "));
    std::string value_str = command.substr(command.find(" ") + 1, command.size());
    int value = std::stoi(value_str);

    if (direction == "forward") {
        pos.horizontal += value;
        pos.depth += pos.aim * value;
    } else if (direction == "down") {
        pos.aim += value;
    } else if (direction == "up") {
        pos.aim -= value;
    }
}

int main() {
    Position position;

    for(std::string line; std::getline(std::cin, line);) {
        update_position_part2(position, line);
    }

    std::cout << "Final position: (" << position.horizontal << ", " << position.depth << ")" << std::endl;
}
