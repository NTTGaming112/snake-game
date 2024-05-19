import pygame

cell_size = 30
cell_number = 30
speed = 10

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r'music\background_music.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((cell_number*cell_size,cell_size*cell_number))
pygame.display.set_caption("Snake Game")

font_style = pygame.font.SysFont("comicsansms", cell_size)
font_msg = pygame.font.SysFont(None, 2*cell_size)
font_msg1 = pygame.font.SysFont(None, 4*cell_size)
font_home = pygame.font.SysFont(None, 6*cell_size)

score_color = pygame.Color('yellow')

background_image = pygame.image.load(r'background\background.png')
bg = pygame.transform.scale(background_image,(cell_size*(cell_number-2)+cell_size, (cell_number-10)*cell_size+cell_size))

snake_head_image = pygame.image.load(r'model\head.png')
snake_body_image = pygame.image.load(r'model\body.png')
snake_tail_image = pygame.image.load(r'model\tail.png')
snake_head_image = pygame.transform.scale(snake_head_image,(cell_size,cell_size))
snake_body_image = pygame.transform.scale(snake_body_image,(cell_size,cell_size))
snake_tail_image = pygame.transform.scale(snake_tail_image,(cell_size,cell_size))

start_screen = pygame.image.load(r'background\start_screen.gif')
start_screen = pygame.transform.scale(start_screen,(cell_size*(cell_number)+cell_size, (cell_number)*cell_size+cell_size))
end_screen = pygame.image.load(r'background\end_screen.gif')
end_screen = pygame.transform.scale(end_screen,(cell_size*(cell_number)+cell_size, (cell_number)*cell_size+cell_size))

apple_image = pygame.image.load(r'model\apple.png')
apple_image = pygame.transform.scale(apple_image,(cell_size,cell_size))
green_apple_image = pygame.image.load(r'model\spec_apple.png')
green_apple_image = pygame.transform.scale(green_apple_image,(cell_size,cell_size))

clock = pygame.time.Clock()
