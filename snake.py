import pygame
import time
import random

pygame.init()

snake_colour = (69, 139, 0)
background = (255, 245, 238)
text = (0, 0, 0)
snake_food = (255, 64, 64)

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

display_width = 600
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont('bahnschrift', 37)
score_font = pygame.font.SysFont('comicsansms', 20)

def Your_score (score):
    value = score_font.render(f'    Your Score: {str(score)}', True, text)
    display.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_colour, [x[0], x[1], snake_block, snake_block])

def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    display.blit(mesg, [display_width/18, display_height/2])
    
def gameLoop():
    game_over = False
    game_close = False
    
    x1 = display_width/2
    y1 = display_height/2
    
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True:
            display.fill(background)
            message('You lost! Press Q-Quit or C-Play Again', red)
            
            Your_score(Length_of_snake -1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(background)
        
        pygame.draw.rect(display, snake_food, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake -1)
        
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)

    pygame.quit()
    quit()
    
gameLoop()

# https://www.edureka.co/blog/snake-game-with-pygame/
# https://www.pygame.org/news