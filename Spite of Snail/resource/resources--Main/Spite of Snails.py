# ~ This is to import the modules for this(Do 'pip install pygame' if you don't have it installed):
import pygame
from sys import exit
from random import randint


def Score():
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = Font.render(f'Score: {time}', False, 'Black')
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)
    return time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for Obstacle_rectangle in obstacle_list:
            Obstacle_rectangle.x -= 5

            if Obstacle_rectangle.bottom == 300:
                screen.blit(Snail_Surface, Obstacle_rectangle)
            else:
                screen.blit(Fly_Surface, Obstacle_rectangle)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    global Player_Surface, Player_Index
    if Player_Rectangle.bottom < 300:
        Player_Surface = Player_Jump
    else:
        Player_Index += 0.1
        if Player_Index >= len(Player_Walk):
            Player_Index = 0
        Player_Surface = Player_Walk[int(Player_Index)]


# ~ This is to initiate PyGame:
pygame.init()
# ~ Basic Variables and Set-Up:
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Spite of Snails')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
obstacle_rect_list = []


# ~ These are the Directories For the images⬆️
# ? The '.convert()' and '.convert_alpha()' is to make the images more optimized and run better:
Sky = pygame.image.load('graphics\\Sky.png').convert()
Ground = pygame.image.load('graphics\\ground.png').convert()
Font = pygame.font.Font('font\\Pixeltype.ttf', 50)

# ~ These are the text part of the game:
Font_Surface = Font.render('', False, 'Black')
Text_Surface = Font_Surface
Text_Rectangle = Text_Surface.get_rect(center=(400, 50))

# ~ For the Snail🐌:
Snail_Surface = pygame.image.load('graphics\\snail\\snail1.png').convert_alpha()
Snail_Surface_Second = pygame.image.load('graphics\\snail\\snail2.png').convert_alpha()
Snail_Rectangle = Snail_Surface.get_rect(midbottom=(600, 300))

Snail_Frames = [Snail_Surface, Snail_Surface_Second]
Snail_Index = 0
Snail_Surfaces = Snail_Frames[Snail_Index]


# ~ For the Fly🕊️:
Fly_Surface = pygame.image.load('graphics\\Fly\\Fly1.png').convert_alpha()
Fly_Surface_Second = pygame.image.load('graphics\\Fly\\Fly2.png').convert_alpha()
Fly_Rectangle = Fly_Surface.get_rect(midbottom=(600, 200))


Fly_Frames = [Fly_Surface, Fly_Surface_Second]
Fly_Index = 0
Fly_Surfaces = Fly_Frames[Fly_Index]

# ~ For the Player🧑‍🦱:
Player_Walk_1 = pygame.image.load('graphics\\Player\\player_walk_1.png').convert_alpha()
Player_Walk_2 = pygame.image.load('graphics\\Player\\player_walk_2.png').convert_alpha()
Player_Walk = [Player_Walk_1, Player_Walk_2]
Player_Index = 0
Player_Jump = pygame.image.load('graphics\\Player\\jump.png').convert_alpha()
Player_Surface = Player_Walk[Player_Index]
Player_Rectangle = Player_Surface.get_rect(midbottom=(80, 300))
Player_Gravity = 0

PLayer_Stand = pygame.image.load('graphics\\Player\\player_stand.png').convert_alpha()
PLayer_Stand_Rectangle = PLayer_Stand.get_rect(center=(400, 200))

game_name = Font.render('Spite of the Snails and Birds', False, 'Black')
game_name_rectangle = game_name.get_rect(center=(400, 130))

Game_Message = Font.render('Press Space to play', False, ' Black')
Game_Message_rectangle = Game_Message.get_rect(center=(400, 320))

# ~ Timer:
Obstacle_Timer = pygame.USEREVENT + 1
pygame.time.set_timer(Obstacle_Timer, 1500)

Snail_Animation_Timer = pygame.USEREVENT + 2
pygame.time.set_timer(Snail_Animation_Timer, 500)

Fly_Animation_Timer = pygame.USEREVENT + 3
pygame.time.set_timer(Fly_Animation_Timer, 200)

# ~ This is to Stop the instance of PyGame 🐍 when quitting
# ~ This also to check if an instance of PyGame is Running or has Stopped:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # ? This is to stop the PyGame program(So an error would not come 💀):
            exit()

        # ~ KeyBoard Input:
        if game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and Player_Rectangle.bottom == 300:
                Player_Gravity = -21
            if event.type == pygame.MOUSEBUTTONDOWN and Player_Rectangle == 300:
                if Player_Rectangle.collidepoint(event.pos):
                    Player_Gravity = -30
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        # ~ Timer
        if game_active:
            if event.type == Obstacle_Timer:
                if randint(0, 2):
                    obstacle_rect_list.append(Snail_Surface.get_rect(midbottom=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(Fly_Surface.get_rect(midbottom=(randint(900, 1100), 210)))
            if event.type == Snail_Animation_Timer:
                if Snail_Index == 0:
                    Snail_Index = 1
                else:
                    Snail_Index = 0
                Snail_Surface = Snail_Frames[Snail_Index]
            if event.type == Fly_Animation_Timer:
                if Fly_Index == 0:
                    Fly_Index = 1
                else:
                    Fly_Index = 0
                Fly_Surface = Fly_Frames[Fly_Index]

    if game_active:
        # ~ This is the Surface Sprites
        # ? 'screen.blit()' is to basically paste the image onto the screen and position it, What is a screen?
        # Well it is basically the palette/window where the game will happen
        screen.blit(Sky, (0, 0))
        screen.blit(Ground, (0, 300))
        screen.blit(Text_Surface, Text_Rectangle)
        score = Score()

        # ~ For the Player🧑‍🦱:
        Player_Gravity += 1
        Player_Rectangle.y += Player_Gravity
        if Player_Rectangle.bottom >= 300:
            Player_Rectangle.bottom = 300
            Player_Gravity = 0
        player_animation()
        screen.blit(Player_Surface, Player_Rectangle)

        # ~ Obstacle:
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(Player_Rectangle, obstacle_rect_list)

    else:
        screen.fill('deepskyblue4')
        screen.blit(PLayer_Stand, PLayer_Stand_Rectangle)

        obstacle_rect_list.clear()
        Player_Rectangle.midbottom = (80, 300)
        Player_Gravity = 0

        score_message = Font.render(f'Your Score: {score}', False, 'Black')
        score_message_rectangle = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rectangle)

        if score == 0:
            screen.blit(Game_Message, Game_Message_rectangle)
        else:
            screen.blit(score_message, score_message_rectangle)

    # ~ To Update the display of pygame:
    pygame.display.update()
    # ~ To set the max Framerate of the game
    clock.tick(60)
