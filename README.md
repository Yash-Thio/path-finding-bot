# Pathfinding Robot Project

## Overview
This project implements an autonomous pathfinding robot using A* search algorithm, Python, and an ESP32 microcontroller with Bluetooth communication.

## Components
1. **algorithm.py**: A* Pathfinding Algorithm Implementation
2. **pathfinder.py**: Maze Solving and Bluetooth Communication Script
3. **pathfinder1.ino**: ESP32 Robot Control Firmware

### 1. A* Search Algorithm (algorithm.py)
The A* search algorithm is a sophisticated pathfinding technique that finds the optimal path between two points in a grid-based environment.

#### Key Features:
- Implements a heuristic-based search
- Supports 4-directional movement
- Calculates path cost efficiently
- Handles blocked and unblocked cells

#### Algorithm Steps:
1. Initialize start and destination cells
2. Maintain open and closed lists
3. Calculate path cost (f = g + h)
4. Explore grid cells
5. Trace the optimal path

### 2. Maze Solver (pathfinder.py)
This Python script solves mazes and prepares path instructions for Bluetooth transmission.

#### Key Functionalities:
- A* maze solving algorithm
- Converts path to directional instructions
- Bluetooth communication via serial port
- User-interactive maze navigation

### 3. Robot Control Firmware (pathfinder1.ino)
The ESP32 firmware controls the robot's movement based on received Bluetooth instructions.

#### Movement Capabilities:
- Forward movement
- Left and right rotations
- Precise directional control
- Bluetooth instruction parsing

## System Workflow
1. User defines start and end points in a maze
2. Python script calculates the optimal path
3. Path converted to directional instructions
4. Instructions sent via Bluetooth
5. Robot receives and executes movement commands

## Hardware Requirements
- ESP32 Microcontroller
- Motor Driver Module
- DC Motors
- Bluetooth Module

## Software Requirements
- Python 3.x
- PySerial Library
- Arduino IDE
- ESP32 Board Support

## Installation and Setup
1. Clone the repository
2. Install required Python dependencies
3. Upload Arduino firmware to ESP32
4. Configure Bluetooth COM port
5. Run pathfinder.py

## Potential Improvements
- Implement obstacle detection
- Add dynamic maze generation
- Enhance path optimization
- Integrate advanced sensor feedback

## Limitations
- Fixed grid-based navigation
- Requires pre-defined maze layout
- Limited to 2D grid environments
