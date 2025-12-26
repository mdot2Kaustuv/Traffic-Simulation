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


