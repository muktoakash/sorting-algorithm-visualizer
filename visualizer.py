import pygame
import random
pygame.init()

# Global Class
class DrawInformation:
    """Sets up global information"""

    #colors
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOUR = WHITE

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, list):
        """constructor that takes in the starting list lst for storage"""
        self.width = width
        self.height = height

        # global attribute:Window
        self.window = pygame.display.set_mode
        ((width, height))

        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        """Sets up parameters for visualizing the list"""
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD)
                                  / (self.max_val - self.min_val))
        self.start_x= self.SIDE_PAD // 2

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst
