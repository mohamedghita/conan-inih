
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


# include directories
set(include_directories "${CMAKE_CURRENT_SOURCE_DIR}/inih ${CMAKE_CURRENT_SOURCE_DIR}inih/cpp")
include_directories(BEFORE ${include_directories})

# inih library
set(source_files "${CMAKE_CURRENT_SOURCE_DIR}/inih/ini.c" "${CMAKE_CURRENT_SOURCE_DIR}/inih/cpp/INIReader.cpp")
if(SHARED_INIH)
    add_library(inih SHARED ${source_files})
else() 
    add_library(inih STATIC ${source_files})
endif()
target_link_libraries(inih ${CONAN_LIBS})