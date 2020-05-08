cmake_minimum_required(VERSION 2.8)

project(CAPE)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}//home/jaredub/opencv/build)

SET("OpenCV_DIR" "home/jaredub/opencv/build")

find_package(OpenCV REQUIRED PATHS "home/jaredub/opencv/build")
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

set (CMAKE_CXX_FLAGS "-O2")

set(CMAKE_BUILD_TYPE Release)

include_directories(${EIGEN3_INCLUDE_DIR})

add_executable(cape_offline
	run_cape_offline.cpp
	CAPE.cpp
	PlaneSeg.cpp
	CylinderSeg.cpp
	Histogram.cpp)

target_link_libraries(cape_offline ${OpenCV_LIBS} ${Eigen_LIBRARIES})


