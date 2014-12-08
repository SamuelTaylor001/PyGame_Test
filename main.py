#PLEASE READ
#The purpose of this file is to act as a framework for the actual project
#The file will later be split in to sections
#Please feel free to create your own classes but ONLY call your classes within the game loop
import pygame

#initializes all of the pygame modules
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#Sets the canvas
gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Pygame test yo!')

gameExit = False

#The variables for the lead block
lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

#exit function
def exit_game(exit_event):
    if exit_event.type == pygame.QUIT:
            return True

#gameloop

while not gameExit:
    for event in pygame.event.get():
        gameExit = exit_game(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change



    gameDisplay.fill(white)

    gameDisplay.fill(black, rect=[lead_x, lead_y, 10, 10])

    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()
