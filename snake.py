import pygame
from pygame.math import Vector2
from config import *

class Snake:
    """Class to represent the Snake in the game."""
    def __init__(self):
        self.body = [Vector2(15,15),Vector2(14,15),Vector2(13,15)]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.snake_speed = speed
        self.hp = 3
        self.add = Vector2(1,6)
        self.head = None
        self.tail = None
       
    def draw_snake(self):
        """Draw the snake with directional images."""
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = block.x * cell_size + cell_size
            y_pos = block.y * cell_size + 6*cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                screen.blit(snake_body_image, block_rect)
                
    def update_head_graphics(self):
        """Update the head graphic based on direction."""
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = pygame.transform.rotate(snake_head_image, 180)
        elif head_relation == Vector2(-1, 0):
            self.head = pygame.transform.rotate(snake_head_image, 0)
        elif head_relation == Vector2(0, 1):
            self.head = pygame.transform.rotate(snake_head_image, 90)
        elif head_relation == Vector2(0, -1):
            self.head = pygame.transform.rotate(snake_head_image, -90)

    def update_tail_graphics(self):
        """Update the tail graphic based on direction."""
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = pygame.transform.rotate(snake_tail_image, 0)
        elif tail_relation == Vector2(-1, 0):
            self.tail = pygame.transform.rotate(snake_tail_image, 180)
        elif tail_relation == Vector2(0, 1):
            self.tail = pygame.transform.rotate(snake_tail_image, -90)
        elif tail_relation == Vector2(0, -1):
            self.tail = pygame.transform.rotate(snake_tail_image, 90)

    def move_snake(self):
        """Move the snake based on its current direction."""
        x = (self.body[0].x + self.direction.x + cell_number-2)%(cell_number-2)
        y = (self.body[0].y + self.direction.y + cell_number-10)%(cell_number-10)
        x1 = (self.body[0].x + self.direction.x + cell_number-2)//(cell_number-2)
        y1 = (self.body[0].y + self.direction.y + cell_number-10)//(cell_number-10)
        if x1 == 0 or x1 == 2 or y1 == 0 or y1 == 2: self.hp -= 1
        if self.new_block: 
            body_copy = self.body[:] 
            self.new_block = False          
        else: 
            body_copy = self.body[:-1]  
        body_copy.insert(0, Vector2(x,y))
        self.body = body_copy         

    def add_block(self):
        """Add a new block to the snake."""
        self.new_block = True
        
    def len(self):
        """
        Get the length of the snake.

        Returns:
            int: The number of segments in the snake's body.
        """
        return len(self.body)
    def get_body(self):
        return self.body
    def reset(self):
        """Reset the snake to the initial state."""
        self.__init__()
