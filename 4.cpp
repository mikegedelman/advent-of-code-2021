#include <iostream>
#include <vector>
#include <sstream>

int main() {
    std::vector<std::string> lines;

    for (std::string line; std::getline(std::cin, line);) {
        lines.push_back(line);
    }

    std::vector<int> bingo_numbers;
    std::stringstream ss(lines[0]);

    while (ss.good()) {
        std::string sub;
        std::getline(ss, sub, ',');
        bingo_numbers.push_back(std::stoi(sub));
    }

    for (auto &i: bingo_numbers) {
        std::cout << i << std::endl;
    }

    std::cout << "'" << lines[1].size() << "'" << std::endl;
}