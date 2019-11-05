# Color-based-Ball-Tracking
This repo includes C++ Source for Color-based Ball Tracking Project

Color-based Tracking ball and Measuring the distance from the Webcam to the ball using OpenCV Library and C++ Programming.
Link to Project Video on Youtube: https://www.youtube.com/watch?v=GYbKhNLTJbw&t=15s

## Edit
The python Source also added.

## Usage for Python
Just Run the .py file 
```
python -u BallTracker.py 
```

## Usage for C++
on the dir you clone, run this commands
```
nano CMakeLists.txt
```
Then, Paste the below text in `CMakeLists.txt` file:
```
cmake_minimum_required(VERSION 2.8)
project( BallTracking )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( BallTracking BallTracking.cpp )
target_link_libraries( BallTracking ${OpenCV_LIBS} )
```
Run commands:
```
CMake .
Make
```
To Run:
```
./BallTracking 
```

