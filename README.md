# Traffic Management System and DSA Queue Management System

## Title

Assignment: 1

Name: Kaustuv Bhandari

Roll Number: 11

Course: COMP202

Submitted to: Rupak Ghimire

Date: 2025-12-27

## Overview
This project simulates a 4-way traffic intersection using Python and Pygame. The core objective of this project is to demonstrate the practical use of Data Structures and Algorithms (DSA).

This project demonstrates the use of Queue and Priority Queue algorithms to simulate a four-way junction using linear data structures to manage vehicle flow and traffic light transitions based on real-time lane conditions. Unlike standard traffic lights which use timers, this simulation uses a Priority Queue logic. If North most lane (Road A, Lane 1) traffic exceeds more than 10, the system prioritizes the lane AL2 to handle the traffic congestion.



## Simulator Demo

[Simulator Demo](https://raw.githubusercontent.com/mdot2Kaustuv/DSA-Queue-Simulator/main/Simulator.mp4)


### System Overview

The system follows a Producer-Consumer pattern. The Generator produces vehicle data (incoming traffic), while the Simulator and Traffic_Controller consume that data to manage the junction flow using data structures.

- Generator.py: Produces vehicle data (incoming traffic) by randomly determining the Vehicle ID, Time, road, and lane, then writes it to the Traffic.data file.

- Traffic_controller.py & Trafficlights.py: Traffic_controller.py monitors these queues, triggering a high-priority state if lane AL1 exceeds 10 vehicles, ensuring it is served first until the count drops below 5. Trafficlights.py switches lights between State 1 (Red/Stop) and State 2 (Green/Go).

- Queues.py, Lanes.py, & Roads.py: Implements the linear logic where vehicles enter (enqueue) and exit (dequeue) the junction.

- Simulator.py: Integrates these components using Pygame to visually render the junction, manage traffic light states (Red/Green), and ensure safety by preventing deadlocks through strict state management.

## Features

- Intelligent Priority Management:The system actively monitors the queue length of Lane AL2. When congestion exceeds 10 vehicles, it activates a "Priority Mode" that overrides standard cycles to grant a continuous green light until the lane count is reduced to 5 or fewer.

- Left-Hand Traffic (LHT) Standard: The simulation is designed to follow LHT protocols, which are the standard driving rules in regions like Nepal and the UK.

- Real-Time Graphical Visualization:## Utilizing Pygame, the simulator.py script provides a high-fidelity visualization featuring animated vehicle movement, realistic lane markings, and glowing traffic light indicators.

- Traffic Generation:Using a producer-consumer architecture, Generator.py simulates varying traffic loads by writing vehicle data to Traffic.data, which the simulator then polls to update internal lane queues.

## Installation and Prerequisites
This project requires Python 3.13 to run smoothly and as intended. You will also need to install the external library Pygame for visualization.

- Install Dependencies
Pygame is the only external dependency required. Open your terminal or command prompt and run:

```bash
pip install pygame
```

- Setup
Clone the repository:

```bash
git clone https://github.com/mdot2Kaustuv/DSA-Queue-Simulator
```

Ensure your folder format looks like this:

## Directory 
```
/DSA-Queue-Simulator/
├── src/
│   ├── Generator.py
│   ├── Lanes.py
│   ├── Queues.py
│   ├── Roads.py
│   ├── Simulator.py
│   ├── Traffic_controller.py
│   ├── Traffic.data
│   ├── Vehicles.py
├── .gitignore
├── README.md
└── Simulator.mp4
```
## Execution Instructions
After cloning the repository, access the directory:


```bash
cd traffic-light-simulation-dsa
```
If you have an IDE, you can directly run the project by opening Simulator.py. Otherwise, use the command line:

Starting Generator.py:

```bash
python src/Generator.py
```

Example Output: 2480,2,C,1766727594.3392065

(This window can be kept open or closed as Simulator.py will automatically run it.)

Starting the Simulator:

```bash
python src/Simulator.py
```

Output: A Pygame window with the simulation.

# Time Complexity 

The complexity is divided into two parts: the Backend Logic (Queues & Controller) and the Frontend Visualization (Simulator).

 1. Data Structure Operations (Queues.py)
 This is the foundation of your simulation's performance.

 - enqueue: O(1)
   self.queue.append(vehicle) adds to the end of the  list. This is a constant time
   
 - dequeue: O(N)
   self.queue.pop(0) removes the first element of a Python list.

2. Traffic Controller Logic (Traffic_controller.py)The controller runs in a separate thread. Its complexity depends on the number of cars waiting in the lanes (N)
- get_controlled_cars_count: O(1)
  It calls len() on the list, which is constant time.
- dequeue_controlled_vehicle: O(N) It calls the dequeue method from Queues.py, inheriting the O(N) cost described above.
- serve_normal_cycle: O(K * N)
  It iterates through a constant number of roads (4).It dequeues up to $K$ cars (where $K=5$ in your code).Since each    dequeue is $O(N)$, one cycle step is linear with respect to the queue size.3. Visual Simulator (Simulator.py)

3. Visual Simulator (Simulator.py)
This is where the heaviest computational load exists. Let V be the number of visible vehicles currently moving on the screen.
- Spawning Logic: O(V)
  You filter the list of vehicles: [v for v in visual_vehicles ...]To do this, the code must iterate through every existing vehicle on screen.
- Collision Detection
  Inside the main loop, you iterate through every vehicle
  **Complexity**: Quadratic Time

# Best Case
 The simulation runs smoothly at $O(1)$

# Worst Case 
 -**Backend:** O(N) (Linear) : As queues grow, releasing cars gets slightly slower, but this is usually negligible for N < 10,000.

-**Frontend** O(V^2) : This is the critical performance hitter. If you increase the traffic density significantly, the frame rate will drop exponentially
