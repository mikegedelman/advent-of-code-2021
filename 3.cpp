#include <iostream>
#include <vector>
#include <string>

struct DiagnosticInfo {
    std::vector<std::string> lines;
    std::vector<int> count_of_1s;
    int num_lines;
};

struct PowerDiag {
    std::string gamma;
    std::string epsilon;
};

DiagnosticInfo process_input() {
    bool initialized = false;
    // int num_lines = 0;
    // std::vector<int> count_of_1s;
    DiagnosticInfo result;

    for(std::string line; std::getline(std::cin, line);) {
        result.lines.push_back(line);
        result.num_lines += 1;
    }

    for(auto &line: result.lines) {  
        // this is ugly but whatever - don't see an easy way to peek at
        // stdin input
        if (!initialized) {
            result.count_of_1s.resize(line.size(), 0);
        }

        int pos = 0;
        for (auto &bit: line) {
            if (bit == '1') {
                // std::cout << "here " << pos << std::endl;
                result.count_of_1s[pos] += 1;
            }
            pos += 1;
        }
    }

    return result;
}

PowerDiag part1(std::vector<int> count_of_1s, int num_lines) {
    std::string gamma = "";
    std::string epsilon = "";
    for (int i = 0; i < count_of_1s.size(); i++) {
        std::cout << count_of_1s[i] << " ";
        if (count_of_1s[i] > num_lines / 2) {
            gamma += "1";
            epsilon += "0";
        } else {
            gamma += "0";
            epsilon += "1";
        }
    }
    std::cout << std::endl;

    unsigned long long gamma_decimal = std::strtoull(gamma.c_str(), 0, 2);
    unsigned long long epsilon_decimal = std::strtoull(epsilon.c_str(), 0, 2);
    std::cout << "Gamma: " << gamma_decimal << " " << gamma << std::endl;
    std::cout << "Epsilon: " << epsilon_decimal << " " << epsilon << std::endl;

    PowerDiag diag;
    diag.gamma = gamma;
    diag.epsilon = epsilon;

    return diag;
}

void part2(std::vector<std::string> &lines, std::string gamma, std::string epsilon) {
    auto oxygen_candidates = std::vector(lines);
    auto co2_candidates = std::vector(lines);
    for (int i = 0; i < gamma.size(); i++) {
        oxygen_candidates.erase(std::remove_if(
            oxygen_candidates.begin(),
            oxygen_candidates.end(), 
            [i, gamma](std::string &line) { return line[i] != gamma[i]; }
        ));
    }

    for (auto &line: oxygen_candidates) {
        if (line.size() == 0) continue;
        std::cout << line << std::endl;
    }
}

int main() {
    // InputCounts counts = process_input()
    DiagnosticInfo diag = process_input();
    PowerDiag power_diag = part1(diag.count_of_1s, diag.num_lines);
    part2(diag.lines, power_diag.gamma, power_diag.epsilon);
}