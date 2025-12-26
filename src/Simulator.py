import pygame

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
LANE_WIDTH = 40
ROAD_WIDTH = LANE_WIDTH * 2
COLOR_BG = (34, 139, 34)
COLOR_ROAD = (50, 50, 50)
COLOR_YELLOW = (255, 215, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 50, 50)
COLOR_GREEN = (50, 255, 50)
COLOR_ORANGE = (255, 165, 0)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Traffic Simulation (Fixed Timings)")
font = pygame.font.SysFont('Arial', 16, bold=True)

class VisualVehicle:
    def __init__(self, logical_vehicle):
        self.id = logical_vehicle.id
        self.road = logical_vehicle.road
        self.lane = logical_vehicle.lane
        self.speed = 4
        self.crossed_stop_line = False

        # Lane
        if self.lane == 1:
            lane_offset = LANE_WIDTH / 2
        else:
            lane_offset = LANE_WIDTH + LANE_WIDTH / 2

        if self.road == "A":  # top DOWN
            self.x = CENTER_X - lane_offset
            self.y = -40
            self.dir = (0, 1)
            self.stop_boundary = CENTER_Y - ROAD_WIDTH - 10
            self.angle = 180
        elif self.road == "B":  #  bottom  UP
            self.x = CENTER_X + lane_offset
            self.y = WINDOW_HEIGHT + 40
            self.dir = (0, -1)
            self.stop_boundary = CENTER_Y + ROAD_WIDTH + 10
            self.angle = 0
        elif self.road == "C":  #  right  LEFT
            self.x = WINDOW_WIDTH + 40
            self.y = CENTER_Y - lane_offset
            self.dir = (-1, 0)
            self.stop_boundary = CENTER_X + ROAD_WIDTH + 10
            self.angle = 90
        elif self.road == "D":  #  left  RIGHT
            self.x = -40
            self.y = CENTER_Y + lane_offset
            self.dir = (1, 0)
            self.stop_boundary = CENTER_X - ROAD_WIDTH - 10
            self.angle = 270

        self.image = pygame.Surface((18, 32), pygame.SRCALPHA)
        colors = [(100, 150, 255), (255, 100, 100), (100, 255, 100), (255, 255, 100)]
        color = colors[self.id % len(colors)]
        pygame.draw.rect(self.image, color, (0, 0, 18, 32), border_radius=4)
        pygame.draw.rect(self.image, (200, 200, 255), (2, 2, 14, 10), border_radius=2)
        self.image = pygame.transform.rotate(self.image, self.angle)

    def check_stop_line(self):
        if self.crossed_stop_line:
            return True

        if self.road == "A":
            return self.y > self.stop_boundary
        elif self.road == "B":
            return self.y < self.stop_boundary
        elif self.road == "C":
            return self.x < self.stop_boundary
        elif self.road == "D":
            return self.x > self.stop_boundary
        return False









if __name__ == "__main__":
    main()





