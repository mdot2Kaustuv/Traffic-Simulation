

from Roads import Road
from Lanes import LaneManager
from  Trafficlights import TrafficLight

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


    def vehicle_served(self):
        count = self.lm.get_vehicles()
        n = 4
        average = count / n
        return max(1, int(average))

    def priority(self):
        priority_road = False
        priority_road_num = None

        for road in self.roads:
            if self.lm.size(road, 2) > 10:
                priority_road = True
                priority_road_num = road
                break

        return priority_road, priority_road_num

    def serve_roads(self):
        priority_road, priority_road_num = self.priority()

        if priority_road:
            while self.lm.size(priority_road_num, 2) >= 5:
                self.lm.roads[priority_road_num].dequeue(2)


        else :
            count = self.vehicle_served()
        for road in self.roads:
            green_time = count * self.t
            self.lm.roads[road].dequeue(2)
            





