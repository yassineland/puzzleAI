# import pygame library
import pygame

''' DRAWING CONFIGURATION '''

# Titre
title = "3x4 Puzzle"
# Image path
img_path = "img.jpg"
# Matrix dimensions
nrows = 4
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

''' PREPARE IMAGE '''

# Load image
img = pygame.image.load(img_path)
# Resize to window Width x Height
img = pygame.transform.scale(img, (width, height))
# Initiate a list of image parts
img_parts = []
# Fill the list of image parts
for i in range(nrows):
    for j in range(ncols):
        # - Prepare a surface for a small square
        surf = pygame.Surface((stile, stile))
        # - Take an image part for row i and column j
        surf.blit(img, (0, 0), (j*stile, i*stile, j*stile + stile, i*stile + stile) )
        # - Add this image part to the list
        img_parts.append(surf)

''' GUI FUNCTIONS '''

# Function to draw the matrix
def draw_all(m, ok=False):

    # Detect exit event
    detect_exit()

    # Color background
    if ok:
        screen.fill((0, 200, 153))
    else:
        screen.fill((255, 255, 255))

    # Draw the cells (3x3)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]!= 0:
                # Fill cell with the image part of the number specified
                screen.blit(img_parts[m[i][j]-1], (j*stile, i*stile))

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
