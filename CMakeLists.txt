cmake_minimum_required(VERSION 2.8.11)
project(cmake_wrapper)

include(conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_SYSTEM_PROCESSOR ${CONAN_SETTINGS_ARCH})

add_subdirectory("source_subfolder")
