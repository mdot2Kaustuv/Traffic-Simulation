from Trafficlights import TrafficLight
import time


class TrafficController:
    def __init__(self, shared_lm):
        self.roads = ["A", "B", "C", "D"]
        self.lm = shared_lm
        self.lights = {
            "A": TrafficLight(),
            "B": TrafficLight(),
            "C": TrafficLight(),
            "D": TrafficLight(),
        }

        # Configuration
        self.priority_road = "A"
        self.priority_threshold = 10
        self.priority_min = 5
        self.delay = 0.5

    def vehicle_served(self):
        normal_lanes = ["B", "C", "D"]
        total_vehicles = sum(self.lm.size(road, 1) for road in normal_lanes)
        n = len(normal_lanes)
        average = int(total_vehicles / n)
        return max(1, average)

    def get_green_duration(self, t):
        V = self.vehicle_served()
        return V * t

    def set_active_light(self, active_road):
        for road in self.roads:
            if road == active_road:
                self.lights[road].set_green()
            else:
                self.lights[road].set_red()

    def get_controlled_cars_count(self, road):
        return self.lm.size(road, 1)

    def dequeue_controlled_vehicle(self, road):

        if self.lm.size(road, 1) > 0:
                self.lm.dequeue(road, 1)
                return True
        return False

    def priority_condition_met(self):
        return (
            self.get_controlled_cars_count(self.priority_road)
            > self.priority_threshold
        )

    def serve_priority(self):
        self.set_active_light(self.priority_road)

        while (
            self.get_controlled_cars_count(self.priority_road)
            > self.priority_min
        ):

            served = self.dequeue_controlled_vehicle(self.priority_road)
            if served:
                time.sleep(self.delay)
            else:
                break

    def serve_normal_cycle(self):
        all_roads = ["A", "B", "C", "D"]

        for road in all_roads:
            if self.priority_condition_met():
                return

            vehicle_count = self.get_controlled_cars_count(road)

            if vehicle_count > 0:
                self.set_active_light(road)

                cars_to_serve = min(vehicle_count, 5)

                for _ in range(cars_to_serve):

                    served = self.dequeue_controlled_vehicle(road)
                    if served:
                        time.sleep(self.delay)

    def run(self):
        print("Traffic Controller Started.")
        while True:

            if self.priority_condition_met():
                self.serve_priority()
            else:
                self.serve_normal_cycle()

            time.sleep(0.1)


if __name__ == "__main__":
    from Lanes import LaneManager

    lm = LaneManager()
    c = TrafficController(lm)
    c.run()
