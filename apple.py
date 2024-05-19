import pygame, random
from pygame.math import Vector2
from snake import Snake
from config import *

class Apple:
    """Class to represent the regular Apple in the game."""
    def __init__(self):
        self.random_apple()

    def draw_apple(self,image):
        """Draw the apple on the screen."""
        screen.blit(image, (self.x*cell_size,self.y*cell_size))

    def random_apple(self):
        snake = Snake
        """Randomize the position of the apple."""
        self.x = random.randint(1, cell_number-2)
        self.y = random.randint(6, cell_number-10)
        self.pos = Vector2(self.x,self.y)
        