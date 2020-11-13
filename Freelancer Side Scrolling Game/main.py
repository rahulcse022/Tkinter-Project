import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (9, 182, 11)
black = (0, 0, 0)

# Creating window
screen_width = 500
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("A Simple Scrolling Game")
pygame.display.update()

#Background Image
bgimg = pygame.image.load("bg1.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

## Character load
character = pygame.image.load("char.png")
harm = pygame.image.load("harm.png")
benefit = pygame.image.load("benefit.png")


# Game specific variables
score = 0
exit_game = False
game_over = False
player_xDirection = 20
player_yDirection = 500/2
player_life = 1


benefit_xDirection = 480
benefit_yDirection = random.randint(0, screen_height)
harm_xDirection = 480
harm_yDirection = random.randint(0, screen_height)

player_size = 24
fps = 60
clock = pygame.time.Clock()

##  SCore Board
font = pygame.font.SysFont(None, 55)

def score_board(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# Game Loop
while not exit_game:
    # background put
    gameWindow.blit(bgimg, (0, 0))
    ## character place in game window
    gameWindow.blit(character, (player_xDirection, player_yDirection)) # robot
    gameWindow.blit(harm, (harm_xDirection, harm_yDirection)) # harm
    gameWindow.blit(benefit, (benefit_xDirection, benefit_yDirection)) # benefit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player_yDirection > 20 :
                    player_yDirection = player_yDirection - 12
                

            if event.key == pygame.K_DOWN:
                if player_yDirection < 480 :
                    player_yDirection = player_yDirection + 12
                
                    
    ## collision of green and black                
    if abs(player_xDirection - benefit_xDirection) < 15 and abs(player_yDirection - benefit_yDirection ) < 15 :
        score += 1
        print("Score : ", score * 10, " Life : ", player_life)
        benefit_xDirection = 480
        benefit_yDirection = random.randint(0, screen_height-20)
    ## Collision b/t harm and char 
    if abs(player_xDirection - harm_xDirection) < 20 and abs(player_yDirection - harm_yDirection ) < 20 :
        player_life -= 1
        print("Score : ", score * 10, " Life : ", player_life)
        harm_xDirection = 480
        harm_yDirection = random.randint(0, screen_height-20)
        
        
    
    ## when black missed green rect.
    if benefit_xDirection < player_xDirection :
        benefit_xDirection = 480
        benefit_yDirection = random.randint(0, screen_height-20)
    
    ## when black missed red rect.
    if harm_xDirection < player_xDirection : 
        harm_xDirection = 480
        harm_yDirection = random.randint(0, screen_height-20)
               
                
                
                
    #### benefit and harm ... moving to +x direction to -x direction 
    benefit_xDirection = benefit_xDirection - 2
    harm_xDirection = harm_xDirection - 2          
                

    #gameWindow.fill(white)
    
    score_board("Score : " + str(score * 10) + " Life : "+ str(player_life), black , 80, 10)
    #pygame.draw.rect(gameWindow, red, [harm_xDirection, harm_yDirection, 50, 50])
    #pygame.draw.rect(gameWindow, green, [benefit_xDirection, benefit_yDirection, 50, 50])
    #pygame.draw.rect(gameWindow, black, [player_xDirection, player_yDirection, 40, 40])
    if player_life > 0 :
        pygame.display.update()
    else:
        gameWindow.fill(white)
        score_board("Game Over", black, 100, 200)
        pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
