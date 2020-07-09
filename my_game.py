import pygame
import random

pygame.init()
pygame.font.init()

#        R    G   B
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

SIZE = (600, 600)
FPS = 60

SPAWNITEM = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNITEM, 500)

# Window
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Dodger')

my_font = pygame.font.SysFont('Comic Sans MS', 18)
my_font_1 = pygame.font.SysFont('Comic Sans MS', 30)

# Hero
hero_x, hero_y = 300, 560
hero_position = 1

possible_coords = [70, 300, 530]
items = []

clock = pygame.time.Clock()


class Item:
    def __init__(self, item_type):
        self.x = random.choice(possible_coords)
        self.y = -20
        self.item_type = item_type


def end_game():
    pygame.time.delay(1000)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                quit()


counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and hero_position:
                hero_x -= 230
                hero_position -= 1

            if event.key == pygame.K_RIGHT and hero_position != 2:
                hero_x += 230
                hero_position += 1

        if event.type == SPAWNITEM:
            items.append(Item(random.choice(['food', 'dirt'])))

    screen.fill(BLACK)

    for i in items:
        if i.y == hero_y and i.x == hero_x:
            if i.item_type == 'food':
                counter += 1
            else:
                screen.fill(BLACK)

                end = my_font_1.render('Game over. Press any key to exit', True, (255, 255, 255))
                screen.blit(end, (85, 255))
                pygame.display.update()

                end_game()

            del(items[items.index(i)])

        if i.y > 615:
            del(items[items.index(i)])

        i.y += 10
        pygame.draw.circle(screen, RED if i.item_type == 'food' else BROWN, (i.x, i.y), 15)

    pygame.draw.circle(screen, GREEN, (hero_x, hero_y), 25)

    score = my_font.render(f'Score: {counter}', True, (255, 255, 255))
    screen.blit(score, (10, 10))

    clock.tick(FPS)
    pygame.display.update()
