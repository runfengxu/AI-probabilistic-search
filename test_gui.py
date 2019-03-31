import pygame
import sys
from pygame.locals import *
import terrain_block
from terrain_block import *

white = (255,255,255)
black = (0,0,0)

class Pane(object):
    def __init__(self, input_M = []):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', SIZE)
        self.font.set_bold(True)
        pygame.display.set_caption('Search Target')
        self.screen = pygame.display.set_mode((SCREEN_DIM + TOTAL_LINE, SCREEN_DIM + TOTAL_LINE))
        self.screen.fill((white))

        for i in range(BLOCK_DIM+1):
            pygame.draw.line(self.screen, black, [i * (SIZE+LINE_WIDTH),0],
                             [i * (SIZE+LINE_WIDTH), SCREEN_DIM + TOTAL_LINE])
        for j in range(BLOCK_DIM + 1):
            pygame.draw.line(self.screen, black, [0, j * (SIZE + LINE_WIDTH)],
                             [SCREEN_DIM + TOTAL_LINE, j * (SIZE + LINE_WIDTH)])

        self.terrain = terrain(input_M)
        for row in self.terrain._block:
            for cell in row:
                pos = (LINE_WIDTH + cell.x * (SIZE + LINE_WIDTH), LINE_WIDTH + cell.y * (SIZE + LINE_WIDTH))
                pos_rect = (
                LINE_WIDTH + cell.x * (SIZE + LINE_WIDTH), LINE_WIDTH + cell.y * (SIZE + LINE_WIDTH), SIZE, SIZE)
                if cell.FN == FN_FLAT:
                    pygame.draw.rect(self.screen, colorFlat, pygame.Rect(pos_rect))
                elif cell.FN == FN_HILL:
                    pygame.draw.rect(self.screen, colorHill, pygame.Rect(pos_rect))
                elif cell.FN == FN_FOREST:
                    pygame.draw.rect(self.screen, colorForest, pygame.Rect(pos_rect))
                else:
                    pygame.draw.rect(self.screen, colorMaze_Cave, pygame.Rect(pos_rect))

                # if cell.status == RevealStatus.uncover:
                #     self.screen.blit(self.font.render("X", True, red, pos))

        pygame.display.update()

    def addAgent_event(self, pair):
        x, y = pair
        cell = self.terrain.get_cell(x, y)
        pos = ((SIZE + LINE_WIDTH)//3 + cell.x * (SIZE + LINE_WIDTH), cell.y * (SIZE + LINE_WIDTH))
        cell.status = RevealStatus.uncover
        self.screen.blit(self.font.render("X", True, red), pos)
        pygame.display.update()

if __name__ == '__main__':
    Pan_terrain = Pane()
    x = 10
    y =20
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pan_terrain.addAgent_event((x, y))
                    x+=1
                    y+=1
