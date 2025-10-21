cmake_minimum_required(VERSION 3.15)
project(simeis VERSION 0.1.0 LANGUAGES NONE)

find_program(CARGO cargo REQUIRED)
if(NOT CARGO)
    message(FATAL_ERROR "Cargo not found. Please install Rust and Cargo.")
endif()

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Release")
    set(CARGO_BUILD_FLAGS --release)
    set(CARGO_BUILD_DIR release)
else()
    set(CARGO_BUILD_FLAGS "-F heavy-testing")
    set(CARGO_BUILD_DIR debug)
endif()

add_custom_target(rust_server ALL
    COMMAND ${CARGO} build ${CARGO_BUILD_FLAGS}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Building Rust workspace with Cargo (${CMAKE_BUILD_TYPE} mode)"
)

add_custom_target(cargo_clean
    COMMAND ${CARGO} clean
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Cleaning Cargo build artifacts"
)

add_custom_target(cargo_test
    COMMAND ${CARGO} test
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Running Cargo tests"
)

set(TYPST_INPUT ${CMAKE_CURRENT_SOURCE_DIR}/doc/manual.typ)
set(TYPST_OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/doc/output.pdf)

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/doc/output.pdf
    COMMAND typst compile ${CMAKE_CURRENT_SOURCE_DIR}/doc/manual.typ ${CMAKE_CURRENT_SOURCE_DIR}/doc/output.pdf
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Building Typst documentation"
)

add_custom_target(doc ALL DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/doc/output.pdf)

enable_testing()
add_test(NAME rust_tests
    COMMAND ${CARGO} test
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

install(PROGRAMS ${CMAKE_SOURCE_DIR}/target/${CARGO_BUILD_DIR}/simeis-server
    DESTINATION bin
    OPTIONAL
)

# Print configuration summary
message(STATUS "CMake Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Cargo found at: ${CARGO}")
message(STATUS "Cargo build flags: ${CARGO_BUILD_FLAGS}")
