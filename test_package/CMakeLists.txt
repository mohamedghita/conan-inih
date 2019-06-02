cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

add_executable(example_c example_c.cpp)
target_link_libraries(example_c ${CONAN_LIBS})

add_executable(example_cpp_vector example_cpp_vector.cpp)
target_link_libraries(example_cpp_vector ${CONAN_LIBS})


# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
