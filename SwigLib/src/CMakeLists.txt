cmake_minimum_required(VERSION 3.0.2)

project(SwigLib)
SET(CMAKE_CXX_STANDARD 11)

IF(NOT ANDROID)
    SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb -std=c++11 -Wunused-variable")
    SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O2 -Wall -std=c++11 -Wunused-variable")
ELSE()
    # 如果是安卓平台使用 ToolChain文件中提供的选项    
    SET(MY_CXX_FLAG "-Wunused-variable")
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" )
    SET(CCMAKE_C_FLAGS "${CMAKE_C_FLAGS}")
ENDIF(NOT ANDROID)

# 收集源代码
INCLUDE_DIRECTORIES(.)

IF(ANDROID)
    # 安卓打包时需要用到的额外文件
    INCLUDE_DIRECTORIES($ENV{ANDROID_NDK_HOME}/sources/android/native_app_glue)
ENDIF(ANDROID)

#swig接口文件
FILE(GLOB_RECURSE SWIG_SRC "swig/swiglib_wrap.cxx")
#test源码
FILE(GLOB_RECURSE TEST_SRC "test/*.cpp")

#安卓平台打包
IF(ANDROID)
    ADD_LIBRARY(swiglib SHARED 
        ${SWIG_SRC} 
        ${TEST_SRC} 
    )
    TARGET_LINK_LIBRARIES(swiglib android log)
ENDIF(ANDROID)

# IOS平台打包
IF(IOS)
    # 设置编译器
    SET(CMAKE_C_COMPILER clang)
    SET(CMAKE_CXX_COMPILER clang++)
    # 设置目标构架
    SET(CMAKE_OSX_ARCHITECTURES "armv7 arm64")
    # 设置目标系统
    SET(CMAKE_OSX_SYSROOT iphoneos11.1)
    # 设置最低兼容系统
    set(CMAKE_XCODE_ATTRIBUTE_IPHONEOS_DEPLOYMENT_TARGET "7.0")

    ADD_LIBRARY(swiglib 
        ${SWIG_SRC}  
        ${TEST_SRC} 
    )
ENDIF(IOS)

# MACOSX平台打包
IF(MACOSX)

    ADD_LIBRARY(swiglib MODULE 
        ${SWIG_SRC}  
        ${TEST_SRC} 
    )
    SET_TARGET_PROPERTIES(swiglib PROPERTIES BUNDLE TRUE)

)

ENDIF(MACOSX)
