#include <inih/INIReaderVec.h>
#include <iostream>

template <typename T>
void printVector(const std::vector<T>& vec) {
    std::cout << "vector: [";
    for (auto iter = vec.begin(); iter != vec.end(); ++iter) {
        std::cout << *iter << ((iter < vec.end() - 1) ? ", " : "");
    }
    std::cout << "]" << std::endl;
}

int main(int argc, char const* argv[]) {
    inih::extended::INIReaderVec reader("./test.ini");
    std::cout << "parse error: " << reader.ParseError() << std::endl;

    auto boolVector = reader.GetBooleanVector("vector", "boolean_array");
    printVector(boolVector);

    auto intVector = reader.GetIntegerVector("vector", "integer_array");
    printVector(intVector);

    auto doubleVector = reader.GetRealVector("vector", "real_array");
    printVector(doubleVector);

    auto stringVector = reader.GetStringVector("vector", "string_array");
    printVector(stringVector);

    return 0;
}
