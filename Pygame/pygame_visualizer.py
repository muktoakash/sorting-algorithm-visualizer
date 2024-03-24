""" ./Pygame/pygame_visualizer.py """
import random
import math
import pygame


# import sorting algorithms
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

# initialize pygame
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

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    #fonts
    FONT = pygame.font.SysFont('arial', 12)
    LARGE_FONT = pygame.font.SysFont('arial', 20)

    #padding
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        """constructor that takes in the starting list lst for storage"""
        self.width = width
        self.height = height

        # global attribute:Window
        self.window = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        """Sets up parameters for visualizing the list"""
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # set up unit width and height
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))

        # starting point in the horizontal axis
        self.start_x= self.SIDE_PAD // 2

def generate_starting_list(n, min_val, max_val):
    """
    generates a random list of n numbers from min_val to max_val
    """
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def draw(draw_info, algo_name, ascending):
    """
    Draws the frame for visualizing the list at a given time
    """

    # clear the background
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)

    # generate  title info
    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1, draw_info.GREEN)
    # display title info
    draw_info.window.blit(title,
                          (draw_info.width / 2 - title.get_width()
                           /2,5))

    # generate controls info
    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Sort | A - Ascending | D - Descending",
        1, draw_info.BLACK)
    # display controls
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width()/2,35))

    # genarate sorting options
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    # display sorting options
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width()/2,65))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions=None, clear_bg = False):
    """
    display the current list at a given
    iteration of sorting
    """
    lst = draw_info.lst

    if not color_positions:
        color_positions = dict()

    # initailizing the frame for the first iteration
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)

        pygame.draw.rect(draw_info.window,
                         draw_info.BACKGROUND_COLOUR, clear_rect)

    # working through drawing the list
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

def draw_sort(sorting_algorithm, draw_info, ascending, algo_name):
    """visualize the sorting by drawing blocks affected by sorting"""

    # try sorting to the next iteration
    try:
        j = next(sorting_algorithm(draw_info, ascending))
        draw_list(draw_info, {j: draw_info.GREEN, j + 1:
                              draw_info.RED}, True)
    # stop once completely sorted
    except StopIteration:
        draw(draw_info, algo_name, ascending)
        return False

    return True


def main():
    """driver for the visualizer"""
    run = True
    clock = pygame.time.Clock()

    # setting up a demo list
    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)

    # intial list visualized
    draw_info = DrawInformation(800, 600, lst)

    # set parameters
    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"

    while run:
        clock.tick(60)

        if sorting:
            sorting = draw_sort(sorting_algorithm, draw_info, ascending, sorting_algo_name)
        else:
            draw(draw_info, sorting_algo_name, ascending)

        pygame.display.update()

        # listen to the key-press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting is False:
                sorting = True
            elif event.key == pygame.K_a and sorting is False:
                ascending = True
            elif event.key == pygame.K_d and sorting is False:
                ascending = False
            elif event.key == pygame.K_i and sorting is False:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and sorting is False:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

    pygame.quit()

if __name__== "__main__":
    main()
