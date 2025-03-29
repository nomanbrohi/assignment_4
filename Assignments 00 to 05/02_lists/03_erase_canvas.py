import pygame
import sys

pygame.init()

width, height = 800, 600
# print(width, height)
cell_size = 20
# print(cell_size)
cols = width // cell_size #40
# print(cols)
rows = height // cell_size #40
# print(rows)

blue = (0,0,255)
white = (255,255,255)
eraser_color = (255,0,0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Canvas Eraser")

grid = []

for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(blue)
    grid.append(row)

def erase_cells(eraser_pos, eraser_size):
    #eraser mouse current position
    #eraser width and height

    #convert pixels into grid cells
    eraser_col = eraser_pos[0] // cell_size
    eraser_row = eraser_pos[1] // cell_size

    eraser_width = eraser_size[0] // cell_size
    eraser_height = eraser_size[1] // cell_size

    for row in range(max(0, eraser_row), min(rows, eraser_row + eraser_height)):
        for col in range(max(0, eraser_col), min(cols, eraser_col + eraser_width)):
            grid[row][col] = white


def main():
    clock = pygame.time.Clock()
    eraser_size = (40, 40)
    eraser_pos = (0,0)
    eraser_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(*eraser_pos, *eraser_size).collidepoint(event.pos):
                    eraser_active = True
            elif event.type == pygame.MOUSEBUTTONUP:
                eraser_active = False
            elif event.type == pygame.MOUSEMOTION and eraser_active:
                eraser_pos = event.pos
                erase_cells(eraser_pos, eraser_size)

        for row in range(rows):
            for col in range(cols):
                pygame.draw.rect(screen, grid[row][col], (col*cell_size, row*cell_size,cell_size,cell_size))
        pygame.draw.rect(screen, eraser_color,(*eraser_pos, *eraser_size),2)

        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()