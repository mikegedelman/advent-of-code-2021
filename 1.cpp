#include <iostream>
#include <vector>
#include <unistd.h>

void part1() {
    std::string line;
    std::getline(std::cin, line);
    int last = std::stoi(line);
    int num_increased = 0;

    while(std::getline(std::cin, line)) {
        int cur = std::stoi(line);
        if (cur > last) {
            num_increased += 1;
        }
        last = cur;
    }

    std::cout << "Depth measurement increases: " << num_increased << std::endl;
}

void part2() {
    std::vector<int> measurements;
    for(std::string line; std::getline(std::cin, line);) {
        measurements.push_back(std::stoi(line));
    }

    int increases = 0;
    std::vector last_window(measurements.begin(), measurements.begin() + 3);
    for (int i = 1; i < measurements.size() - 2; i++) {
        std::vector cur_window(measurements.begin() + i, measurements.begin() + i + 3);
        int last_window_sum = 0;
        for (auto x: last_window) {
            last_window_sum += x;
        }

        int cur_window_sum = 0;
        for (auto x: cur_window) {
            cur_window_sum += x;
        }

        if (cur_window_sum > last_window_sum) {
            increases += 1;
        }
        last_window = cur_window;

    }

    std::cout << "Depth measurement increases: " << increases << std::endl;
}

int main() {
    part2();
}