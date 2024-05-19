import pygame, sys, math
from pygame.math import Vector2
from snake import Snake
from apple import Apple
from config import *

class Main():
    """Main class to run the Snake Game."""
    def __init__(self):        
        self.apple = Apple()
        self.green_apple = Apple()
        self.snake = Snake()
        self.counter = 0
        self.red_apple_count = 0
        self.green_apple_visible = False
        self.green_apple_timer = 100
        self.game_active = False  
        self.start_screen = True

    def draw_all(self):
        """Draw all game elements on the screen."""
        screen.fill('#483D8B')
        self.border()
        self.apple.draw_apple(apple_image)
        if self.green_apple_visible:
            self.green_apple.draw_apple(green_apple_image)
            self.draw_green_apple_timer()
        self.snake.draw_snake()
        self.Your_score()
        pygame.display.update()

    def border(self):
        """Draw the play area on the screen."""
        pygame.draw.rect(screen, 'white', (0, 5*cell_size, cell_size*cell_number, (cell_number-8)*cell_size))
        screen.blit(bg, (cell_size-cell_size/2, 6*cell_size-cell_size/2))

    def update(self):
        """Update the game state."""
        self.snake.move_snake()
        self.check_collision()
        self.check_fall()

    def check_collision(self):
        """Check for collisions between snake and apples."""
        if self.apple.pos == self.snake.body[0] + self.snake.add:
            self.red_apple_count += 1
            self.apple.random_apple()
            while self.apple.pos in self.snake.body: self.apple.random_apple() 
            self.snake.add_block()
            if self.snake.snake_speed < 21:
                self.snake.snake_speed += 1
            if self.red_apple_count % 5 == 0:
                self.green_apple.random_apple()
                while self.apple.pos in self.snake.body: self.apple.random_apple()
                self.green_apple_visible = True
                self.green_apple_timer = 100

        if self.green_apple_visible and self.green_apple.pos == self.snake.body[0] + self.snake.add:
            self.snake.hp += 1
            self.green_apple_visible = False
            self.snake.add_block()
            if self.snake.snake_speed < 21:
                self.snake.snake_speed += 1   

    def check_fall(self):
        """Check if the snake collides with itself or the walls."""
        if (self.snake.body[0] + self.snake.direction) in self.snake.body:
            self.snake.hp -= 1
            if self.snake.body[0].x >= cell_number: self.snake.body[0].x = 0
            if self.snake.body[0].x < 0: self.snake.body[0].x = cell_number
            if self.snake.body[0].y >= cell_number: self.snake.body[0].y = 0
            if self.snake.body[0].y < 0: self.snake.body[0].y = cell_number
        if self.snake.hp < 1:
            self.game_end()

    def game_over(self):
        """Handle game over state."""
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.apple.random_apple()
                        self.snake.reset()
                        self.score = 0
                        self.counter = 0
                        self.special_apple_spawn_counter = 0
                        self.game_active = True
                        game = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def game_end(self):
        screen.blit(end_screen, (-cell_size,-cell_size))

        mesg1 = font_msg1.render("Game Over", True, 'yellow')
        screen.blit(mesg1, [cell_number*cell_size // 2 - mesg1.get_width() // 2, cell_number*cell_size // 12])

        mesg2 = font_msg.render(f"Time: {math.trunc(self.counter//60):02}:{math.trunc(self.counter%60):02}", True, 'yellow')
        screen.blit(mesg2, [cell_number*cell_size // 2 - mesg2.get_width() // 2, cell_number*cell_size // 12 + 3*cell_size])

        mesg3 = font_msg1.render(f"Your Score: {self.snake.len()-3}", True, 'yellow')
        screen.blit(mesg3, [cell_number*cell_size // 2 - mesg3.get_width() // 2, cell_number*cell_size // 2])

        mesg4 = font_msg.render("Press P-Play Again", True, 'yellow')
        screen.blit(mesg4, [cell_number*cell_size // 2 - mesg4.get_width() // 2, cell_number*cell_size - cell_number*cell_size // 6])

        mesg5 = font_msg.render("Press Q-Quit", True, 'yellow')
        screen.blit(mesg5, [cell_number*cell_size // 2 - mesg5.get_width() // 2, cell_number*cell_size - cell_number*cell_size // 6 + 2*cell_size])
        
        pygame.display.update()
        self.game_over()

    def message(self, msg, color, width, height):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width, height])

    def Your_score(self):
        self.message(f"Your Score: {self.snake.len() - 3}", score_color, cell_size, cell_size)
        self.message("HP: " + str(self.snake.hp), score_color, cell_size, 3*cell_size)
        self.message("Time", score_color, (cell_number-6)*cell_size, cell_size)
        self.message(f'{math.trunc(self.counter//60):02}:{math.trunc(self.counter % 60):02}', score_color, (cell_number-6)*cell_size, 3*cell_size)

    def draw_green_apple_timer(self):
        timer_width = int(cell_size * (cell_number-1) * (self.green_apple_timer / 100))
        pygame.draw.rect(screen, 'white', (cell_size, cell_number * cell_size - 2*cell_size, timer_width, cell_size))

    def show_start_screen(self):
        """Show the start screen."""
        screen.blit(start_screen, (-cell_size,-cell_size))
        title_surface = font_home.render('Snake Game', True, 'red')
        screen.blit(title_surface, (cell_number*cell_size // 2 - title_surface.get_width() // 2, cell_number*cell_size // 3))
        start_button = pygame.Rect(cell_number*cell_size // 2 - 2*cell_size, cell_number*cell_size - cell_number*cell_size // 6, 6*cell_size, 3*cell_size)           
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        start_text = font_msg.render('START', True, (0, 0, 0))
        screen.blit(start_text, (start_button.x + cell_size, start_button.y + cell_size))
        pygame.display.update()
        return start_button
    
    def run(self):
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0,-1)
                        
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0,1)
                        
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1,0)
                        
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:                        
                            self.snake.direction = Vector2(1,0)
                        
                    if event.key == pygame.K_ESCAPE:
                        self.game_end()            
            
            self.update()
            self.draw_all()  

            if self.green_apple_visible:
                self.green_apple_timer -= 1
                if self.green_apple_timer <= 0:
                    self.green_apple_visible = False

            pygame.display.update()
            self.counter += 1/self.snake.snake_speed
            clock.tick(self.snake.snake_speed)

if __name__ == '__main__':
    main_game = Main()
    start_button = main_game.show_start_screen()
    while main_game.start_screen:
        main_game.show_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main_game.start_screen = False
                    main_game.game_active = True
        clock.tick(60)
    main_game.run()