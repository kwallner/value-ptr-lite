# Copyright 2017-2018 by Martin Moene
#
# https://github.com/martinmoene/value_ptr-lite
#
# Distributed under the Boost Software License, Version 1.0. 
# (See accompanying file LICENSE.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

cmake_minimum_required( VERSION 3.5 )

# value_ptr-lite version, updated by script/update-version.py:

set( value_ptr_lite_version "0.0.0" )

# At default, enable building and performing of tests and building of examples:

option( VALUE_PTR_LITE_BUILD_TEST    "Build and perform value_ptr-lite tests" ON )
option( VALUE_PTR_LITE_BUILD_EXAMPLE "Build value_ptr-lite examples" ON )

project( value_ptr_lite LANGUAGES CXX VERSION ${value_ptr_lite_version})

include( GNUInstallDirs )

set( package_name "value_ptr_lite" )
set( include_source_dir "${PROJECT_SOURCE_DIR}/include" )

# Interface library:

add_library(                
    ${package_name} INTERFACE )
    
target_include_directories( 
    ${package_name} INTERFACE "$<BUILD_INTERFACE:${include_source_dir}>" "$<INSTALL_INTERFACE:include>")

# Installation:

install( 
    DIRECTORY ${CMAKE_SOURCE_DIR}/include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR} )

# If requested, build and perform tests, build examples:

enable_testing()

if ( VALUE_PTR_LITE_BUILD_TEST )
    add_subdirectory( test )
endif()

if ( VALUE_PTR_LITE_BUILD_EXAMPLE )
    add_subdirectory( example )
endif()

#
# Create Config Files
#
install(TARGETS ${package_name}
    EXPORT Targets
    INCLUDES DESTINATION include
    )

install(EXPORT Targets
    FILE ${PROJECT_NAME}Targets.cmake
    DESTINATION share/cmake/${PROJECT_NAME}
    )

#
# Export Library
#
include(CMakePackageConfigHelpers)

write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMinorVersion
    )

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/script/LibraryConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    @ONLY
    )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    DESTINATION
        . # Root Directory
    )

# end of file
