import pygame
from sys import exit
import random
import os

pygame.init()
WIN = pygame.display.set_mode((570, 570))
pygame.display.set_caption("Memory")
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 70)

backgroud_surf = pygame.Rect(0, 0, WIN.get_width(), WIN.get_height())

card_revers = pygame.image.load(os.path.join("img", "karta.png"))

rectangles = []
for i in range(3):
    for j in range(4):
        rectangles.append(pygame.Rect(j*139 + 14,i*139 + 14 + 139, 125, 125))


def main():
    cards = [
        [pygame.image.load(os.path.join("img", "ciri.png")), 0, 0],
        [pygame.image.load(os.path.join("img", "geralt.png")), 0, 1],
        [pygame.image.load(os.path.join("img", "iorweth.png")), 0, 2],
        [pygame.image.load(os.path.join("img", "jaskier.png")), 0, 3],
        [pygame.image.load(os.path.join("img", "triss.png")), 0, 4],
        [pygame.image.load(os.path.join("img", "yen.png")), 0, 5],
        [pygame.image.load(os.path.join("img", "ciri.png")), 0, 0],
        [pygame.image.load(os.path.join("img", "geralt.png")), 0, 1],
        [pygame.image.load(os.path.join("img", "iorweth.png")), 0, 2],
        [pygame.image.load(os.path.join("img", "jaskier.png")), 0, 3],
        [pygame.image.load(os.path.join("img", "triss.png")), 0, 4],
        [pygame.image.load(os.path.join("img", "yen.png")), 0, 5]
    ]

    random.shuffle(cards)
    attempts = 0
    opened_in_turn = []
    pares_opened = 0

    while True:
        pygame.event.clear()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                for rectangle in rectangles:
                    if rectangle.collidepoint(pygame.mouse.get_pos()):
                        if cards[i][1] == 0:
                            opened_in_turn.append(i)
                            cards[i][1] = 1
                        break
                    i += 1

        draw_window(cards, attempts)

        if len(opened_in_turn) == 2:
            attempts += 1
            if cards[opened_in_turn[0]][2] != cards[opened_in_turn[1]][2]:
                cards[opened_in_turn[0]][1] = 0
                cards[opened_in_turn[1]][1] = 0
                pygame.time.delay(2000)
            else:
                pares_opened += 1
                # Make correctly guessed pair disappear
                cards[opened_in_turn[0]][1] = 2
                cards[opened_in_turn[1]][1] = 2
                pygame.time.delay(1000)
            opened_in_turn.clear()

        if pares_opened == 6:
            handle_win(attempts)
            break

    main()
    

def draw_window(cards, attempts):
    pygame.draw.rect(WIN, (17, 93, 63), backgroud_surf)
    attempts_text = font.render(f"Attempts: {attempts}", False, WHITE)
    attempts_rect = attempts_text.get_rect(midtop=(backgroud_surf.width//2, 20))
    WIN.blit(attempts_text, attempts_rect)

    for i in range(3):
        for j in range(4):
            if cards[i*4 + j][1] == 1:
                WIN.blit(cards[i*4 + j][0], [j*139 + 14,i*139 + 14 + 139])
            elif cards[i*4 + j][1] == 0:
                WIN.blit(card_revers, [j*139 + 14,i*139 + 14 + 139])
    
    pygame.display.update()


def handle_win(attempts):
    pygame.draw.rect(WIN, (17, 93, 63), backgroud_surf)

    attempts_text1 = font.render(f"You Won!", False, WHITE) # Only for metrics
    metric = (WIN.get_height() - attempts_text1.get_height()*3 + 20*2) // 2 - 40
    attempts_text1 = font.render(f"You Won!", False, WHITE)
    attempts_rect1 = attempts_text1.get_rect(midtop=(backgroud_surf.width//2, metric))
    attempts_text2 = font.render(f"Total Attempts:", False, WHITE)
    attempts_rect2 = attempts_text2.get_rect(midtop=(backgroud_surf.width//2, metric + 20 + attempts_text1.get_height()))
    attempts_text3 = font.render(str(attempts), False, WHITE)
    attempts_rect3 = attempts_text3.get_rect(midtop=(backgroud_surf.width//2, metric + 40 + 2*attempts_text1.get_height()))
    WIN.blit(attempts_text1, attempts_rect1)
    WIN.blit(attempts_text2, attempts_rect2)
    WIN.blit(attempts_text3, attempts_rect3)

    pygame.display.update()
    pygame.time.delay(5000)


if __name__ == "__main__":
    main()