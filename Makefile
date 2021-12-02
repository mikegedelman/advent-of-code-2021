CXXFLAGS := -std=c++17

EXECUTABLES := $(shell find . -name "*.cpp" -exec basename {} .cpp \;)

%: %.cpp
	clang++ $(CXXFLAGS) $^ -o $@

.PHONY: all clean

all: $(EXECUTABLES)

clean:
	rm $(EXECUTABLES)