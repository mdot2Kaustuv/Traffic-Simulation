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
        self.service_delay = 0.5

    def set_active_light(self, active_road):
        for road in self.roads:
            if road == active_road:
                self.lights[road].set_green()
            else:
                self.lights[road].set_red()

    def get_controlled_cars_count(self, road):
        return self.lm.size(road, 1) + self.lm.size(road, 2)

    def service_free_lanes(self):

        for road in self.roads:
            if self.lm.size(road, 3) > 0:
              self.lm.dequeue(road, 3)

    def dequeue_controlled_vehicle(self, road):
        for lane in [1, 2]:
            if self.lm.size(road, lane) > 0:
                self.lm.dequeue(road, lane)
                return True
        return False

    def priority_condition_met(self):
        return self.get_controlled_cars_count(self.priority_road) > self.priority_threshold

    def serve_priority(self):
        self.set_active_light(self.priority_road)

        # Serve until queue drops below 5 (as per PDF)
        while self.get_controlled_cars_count(self.priority_road) > self.priority_min:
            self.service_free_lanes()  # Keep free lanes moving!

            served = self.dequeue_controlled_vehicle(self.priority_road)
            if served:
                time.sleep(self.service_delay)
            else:
                break

    def serve_normal_cycle(self):
        normal_roads = ["B", "C", "D"]
        all_roads = ["A", "B", "C", "D"]

        for road in all_roads:
            if self.priority_condition_met():
                return  # Interrupt to handle priority

            vehicle_count = self.get_controlled_cars_count(road)

            if vehicle_count > 0:
                self.set_active_light(road)


                cars_to_serve = min(vehicle_count, 5)

                for _ in range(cars_to_serve):
                    self.service_free_lanes()  # Keep free lanes moving!

                    served = self.dequeue_controlled_vehicle(road)
                    if served:
                        time.sleep(self.service_delay)

    def run(self):
        print("Traffic Controller Started.")
        while True:
            self.service_free_lanes()

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