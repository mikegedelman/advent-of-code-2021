#include <iostream>
#include <optional>

int main() {
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
