#include <iostream>
#include <vector>
#include <string>

struct DiagnosticInfo {
    std::vector<std::string> lines;
    int num_lines = 0;
};

DiagnosticInfo process_input() {
    DiagnosticInfo result;

    for(std::string line; std::getline(std::cin, line);) {
        result.lines.push_back(line);
        result.num_lines += 1;
    }

    return result;
}

std::vector<int> get_count_of_1s(std::vector<std::string> lines) {
    std::vector<int> count_of_1s(lines[0].size());
    for(auto &line: lines) {  
        int pos = 0;
        for (auto &bit: line) {
            if (bit == '1') {
                count_of_1s[pos] += 1;
            }
            pos += 1;
        }
    }

    return count_of_1s;
}

void part1(DiagnosticInfo &diag) {
    std::vector<int> count_of_1s = get_count_of_1s(diag.lines);

    std::string gamma = "";
    std::string epsilon = "";
    for (int i = 0; i < count_of_1s.size(); i++) {
        if (count_of_1s[i] > (diag.num_lines - count_of_1s[i])) {
            gamma += "1";
            epsilon += "0";
        } else {
            gamma += "0";
            epsilon += "1";
        }
    }

    std::cout << "Gamma: " << std::strtoull(gamma.c_str(), 0, 2) << " " << gamma << std::endl;
    std::cout << "Epsilon: " << std::strtoull(epsilon.c_str(), 0, 2) << " " << epsilon << std::endl;
}

std::string life_support_rating(DiagnosticInfo &diag, char (*determine_most_common_bit)(int, int)) {
    std::vector<std::string> candidates(diag.lines);
    int bit_position = 0;
    while (candidates.size() > 1) {
        std::vector<int> count_of_1s = get_count_of_1s(candidates);
        char most_common_bit = determine_most_common_bit(count_of_1s[bit_position], candidates.size());

        std::vector<std::string> new_candidates;
        for (auto &candidate: candidates) {
            if (candidate[bit_position] == most_common_bit) {
                new_candidates.push_back(candidate);
            }
        }

        candidates = new_candidates;
        bit_position += 1;
    }

    return candidates[0];
}

char most_common_bit(int num_1s, int list_size) {
    return num_1s >= (list_size - num_1s) ? '1' : '0';
}

char least_common_bit(int num_1s, int list_size) {
    return num_1s < (list_size - num_1s) ? '1' : '0';
}

void part2(DiagnosticInfo &diag) {
    std::string oxygen_rating = life_support_rating(diag, most_common_bit);
    std::string co2_rating = life_support_rating(diag, least_common_bit);
    std::cout << "Oxygen rating: " << std::strtoull(oxygen_rating.c_str(), 0, 2) << " " << oxygen_rating << std::endl;
    std::cout << "CO2 rating: " << std::strtoull(co2_rating.c_str(), 0, 2) << " " << co2_rating << std::endl;
}

int main() {
    DiagnosticInfo diag = process_input();
    part1(diag);
    part2(diag);
}