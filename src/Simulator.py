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

    def update(self, light_is_green, vehicle_ahead):
        if not self.crossed_stop_line:
                self.crossed_stop_line = self.check_stop_line()

            should_move = True

            if not self.crossed_stop_line and not light_is_green:
                dist_to_line = abs((self.y if self.road in "AB" else self.x) - self.stop_boundary)
                if dist_to_line < 10:
                    should_move = False

            if vehicle_ahead:
                distance = self.get_distance_to(vehicle_ahead)
                if distance < 50:
                    should_move = False
            if should_move:
                self.x += self.dir[0] * self.speed
                self.y += self.dir[1] * self.speed

    def get_distance_to(self, other_vehicle):
            if self.road == "A":
                return other_vehicle.y - self.y
            elif self.road == "B":
                return self.y - other_vehicle.y
            elif self.road == "C":
                return self.x - other_vehicle.x
            elif self.road == "D":
                return other_vehicle.x - self.x
            return float('inf')

    def draw(self, surface):
            surface.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))

    def draw_env(surface, controller):
        surface.fill(COLOR_BG)
        pygame.draw.rect(surface, COLOR_ROAD, (CENTER_X - ROAD_WIDTH, 0, ROAD_WIDTH * 2, WINDOW_HEIGHT))
        pygame.draw.rect(surface, COLOR_ROAD, (0, CENTER_Y - ROAD_WIDTH, WINDOW_WIDTH, ROAD_WIDTH * 2))

        # Stop Lines
        pygame.draw.line(surface, COLOR_WHITE, (CENTER_X - ROAD_WIDTH, CENTER_Y - ROAD_WIDTH - 5),
                         (CENTER_X, CENTER_Y - ROAD_WIDTH - 5), 4)  # A
        pygame.draw.line(surface, COLOR_WHITE, (CENTER_X, CENTER_Y + ROAD_WIDTH + 5),
                         (CENTER_X + ROAD_WIDTH, CENTER_Y + ROAD_WIDTH + 5), 4)  # B
        pygame.draw.line(surface, COLOR_WHITE, (CENTER_X + ROAD_WIDTH + 5, CENTER_Y - ROAD_WIDTH),
                         (CENTER_X + ROAD_WIDTH + 5, CENTER_Y), 4)  # C
        pygame.draw.line(surface, COLOR_WHITE, (CENTER_X - ROAD_WIDTH - 5, CENTER_Y),
                         (CENTER_X - ROAD_WIDTH - 5, CENTER_Y + ROAD_WIDTH), 4)  # D

        # Lines
        pygame.draw.line(surface, COLOR_YELLOW, (CENTER_X, 0), (CENTER_X, WINDOW_HEIGHT), 3)
        pygame.draw.line(surface, COLOR_YELLOW, (0, CENTER_Y), (WINDOW_WIDTH, CENTER_Y), 3)

        # Traffic Lights
        light_coords = {
            "A": (CENTER_X - ROAD_WIDTH - 30, CENTER_Y - ROAD_WIDTH - 30),
            "B": (CENTER_X + ROAD_WIDTH + 30, CENTER_Y + ROAD_WIDTH + 30),
            "C": (CENTER_X + ROAD_WIDTH + 30, CENTER_Y - ROAD_WIDTH - 30),
            "D": (CENTER_X - ROAD_WIDTH - 30, CENTER_Y + ROAD_WIDTH + 30)
        }
        for road, pos in light_coords.items():
            col = COLOR_GREEN if controller.lights[road].is_green() else COLOR_RED
            pygame.draw.circle(surface, (30, 30, 30), pos, 20)
            pygame.draw.circle(surface, col, pos, 15)
            label = font.render(road, True, COLOR_WHITE)
            surface.blit(label, (pos[0] - 5, pos[1] - 35))


if __name__ == "__main__":
    main()





