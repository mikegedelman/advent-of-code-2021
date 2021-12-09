
const readline = require("readline");

async function readInput() {
    const rd = readline.createInterface({
        input: process.stdin,
        crlfDelay: Infinity,
    });
    const inputLines = [];
    for await (const line of rd) {
        inputLines.push(line);
    }

    return inputLines;
}

function part1(entries) {
    const easyDigitCounts = {1: 0, 4: 0, 7: 0, 8: 0};
    entries.forEach(({outputs}) => {
        outputs.forEach(signal => {
            if (signal.length == 2) {
                easyDigitCounts[1] += 1;
            } else if (signal.length == 4) {
                easyDigitCounts[4] += 1;
            } else if (signal.length == 3) {
                easyDigitCounts[7] += 1;
            } else if (signal.length == 7) {
                easyDigitCounts[8] += 1;
            }
        });
    });

    const total = Object.values(easyDigitCounts).reduce((a, b) => a + b);
    console.log("Total of 1,4,7,8: ",  total);
}


// Return true if arrA is a subset of arrB
function subset(arrA, arrB) {
    return arrA.filter(x => arrB.includes(x)).length == arrA.length;
}

// return a string so we can easly concat them and then convert to int
function deduceDigit(signal, easyDigitsMap) {
    if (signal.length == 2) {
        return "1";
    } else if (signal.length == 4) {
        return "4";
    } else if (signal.length == 3) {
        return "7";
    } else if (signal.length == 7) {
        return "8";
    }

    // 0: len 6, not 9, contains 1
    // 2: len 5, contains 3 of the letters in 4
    // 3: len 5, contains 1
    // 5: len 5, not 2 or 3
    // 6: len 6, not 9 or 0
    // 9: len 6, contains 4

    if (signal.length == 5) {
        if (subset(easyDigitsMap[1], signal)) {
            return "3";
        } else {
            const intersect = signal.filter(x => easyDigitsMap[4].includes(x));
            if (intersect.length == 3) {
                return "5";
            } else {
                return "2";
            }
        }
    } else if (signal.length == 6) {
        if (subset(easyDigitsMap[4], signal)) {
            return "9";
        } else if (subset(easyDigitsMap[1], signal)) {
            return "0";
        } else {
            return "6";
        }
    }

    throw "this should be unreachable...";
}

function getOutput(entry) {
    const easyDigitsMap = {};

    const allSignals = entry.signalPatterns.concat(entry.outputs);
    allSignals.forEach(signal => {
        if (signal.length == 2) {
            easyDigitsMap[1] = signal;
        } else if (signal.length == 4) {
            easyDigitsMap[4] = signal;
        } else if (signal.length == 3) {
            easyDigitsMap[7] = signal;
        } else if (signal.length == 7) {
            easyDigitsMap[8] = signal;
        }
    });

    if (Object.keys(easyDigitsMap).length < 4) {
        console.log(entry);
        throw "not all easy digits known!";
    }

    return parseInt(entry.outputs.map(output => deduceDigit(output, easyDigitsMap)).join(""));
}

function part2(entries) {
    const total = entries.map(entry => getOutput(entry)).reduce((a, b) => a + b);
    console.log("Total of all digits: ", total);
}


async function main() {
    const inputLines = await readInput();

    const entries = inputLines.map(rawEntry => {
        const [signalPatternList, outputList] = rawEntry.split(" | ");
        return {
            signalPatterns: signalPatternList.split(" ").map(s => s.split("")),
            outputs: outputList.split(" ").map(s => s.split("")),
        };
    });

    part1(entries);
    part2(entries);
}

main();