

from Roads import Road
from Lanes import LaneManager
from  Trafficlights import TrafficLight
import time

class TrafficController:
    def __init__(self):
        self.roads = ["A", "B", "C", "D"]
        self.t = 2
        self.lm = LaneManager()
        self.lights = {
            "A" : TrafficLight(),
            "B" : TrafficLight(),
            "C" : TrafficLight(),
            "D" : TrafficLight(),

        }
        self.priority_road = "A"
        self.priority_lane ="B"

    def vehicle_served(self) :
        normal_lanes = ["B", "C", "D"]
        total_vehicles = sum(self.lm.size(road, 2) for road in normal_lanes)
        n = len(normal_lanes)
        average = int (total_vehicles / n)
        return max (1, average)

    def priority(self):
        prioritycount = self.lm.size(self.priority_road, self.priority_lane)
        return prioritycount > 10

    def serve_if_priority(self):
       for road in self.roads :
           if road!=self.priority_road:
               self.lights[self.priority_road].set_red()

       self.lights[self.priority_road].set_green()

       while self.lm.size(self.priority_road, self.priority_lane) >= 5:
           vehicle_count = self.lm.size(self.priority_road, self.priority_lane)
           self.lm.dequeue(self.priority_road, self.priority_lane)

        self.lights[self.priority_road].set_green()


    def serve_normal(self) :
        normalroads = ["B","C","D"]
        lane = 2

        for road in normalroads:
            vehiclecount = self.vehicle_served()
            vehicle_number = self.lm.size(road,lane)

            if vehicle_number > 0 :
                self.lights[lane].set_green()

                for nonactiveroad in self.roads :
                        self.lights[nonactiveroad].set_red()

                green_time = vehiclecount*self.t

                for i in range( vehiclecount):
                    self.lm.dequeue(road, lane)
                    time.sleep(self.t)


                self.lights[road].set_red()


    def display_status(self):

        for road in self.roads:
            priority_marker = " (PRIORITY)" if road == self.priority_road else ""
            print(f"Road {road}{priority_marker}:")
            for lane in [1, 2, 3]:
                count = self.lm.size(road, lane)
                lane_type = ""
                if lane == 1:
                    lane_type = "(Incoming)"
                elif lane == 2:
                    lane_type = "(Priority - needs light)" if road == self.priority_road else "(Normal - needs light)"
                elif lane == 3:
                    lane_type = "(Free - left turn)"

                light_status = f"[{self.lights[road]}]" if lane == 2 else ""
                print(f"  Lane {lane} {lane_type}: {count} vehicles {light_status}")



    def run(self):
        cycle = 0

        while True:
            cycle += 1
            self.display_status()

            if self.priority() :
                self.serve_if_priority()
            else :
                self.serve_normal()
                time.sleep(self.t)



controller = TrafficController()
controller.run()





