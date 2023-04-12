# import pygame library
import pygame

''' DRAWING CONFIGURATION '''

# Titre
title = "8 Puzzle"
# Matrix dimensions
nrows = 3
ncols = 3
# Tile size
stile = 60
# Initialise configs
width = ncols * stile
height = nrows * stile
# Set title
pygame.display.set_caption(title)
# Set window dimensions
screen = pygame.display.set_mode((width, height))
# initialise the pygame font
pygame.font.init()
# Load a font for future use
font1 = pygame.font.SysFont("comicsans", 30)

''' GUI FUNCTIONS '''

# Function to draw the matrix
def draw_all(m, ok=False):

    # Detect exit event
    detect_exit()

    # White color background
    screen.fill((255, 255, 255))

    # Draw the cells (3x3)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]!= 0:

                # Fill cell color
                if ok:
                    pygame.draw.rect(screen, (0, 200, 153), (j * stile, i * stile, stile + 1, stile + 1))
                else:
                    pygame.draw.rect(screen, (200, 200, 153), (j * stile, i * stile, stile + 1, stile + 1))

                # Fill cell with number specified
                text1 = font1.render(str(m[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (j * stile + 10, i * stile + 10))

    # Update window
    pygame.display.update()

''' KEYBOARD/MOUSE INPUT '''

def detect_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# detect keyboard press
def detect_keyboard():

    # Loop through the events stored in event.get()
    for event in pygame.event.get():

        # Get if key pressed
        if event.type == pygame.KEYDOWN:
        
            # Arrow key (return the direction)
            if event.key == pygame.K_LEFT:
                return "l"
            if event.key == pygame.K_RIGHT:
                return "r"
            if event.key == pygame.K_UP:
                return "t"
            if event.key == pygame.K_DOWN:
                return "d"

    return ""
