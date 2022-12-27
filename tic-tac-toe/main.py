import pygame
from sys import exit

pygame.init()
WIN = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 70)

player_surf = pygame.Rect(0, 0, 300, 300)

O = font.render("O", False, "Green")
X = font.render("X", False, "Red")

LIGHT_GREEN = (204, 255, 204)
LIGHT_RED = (255, 204 ,203)

rectangles = []
for i in range(3):
    for j in range(3):
        rectangles.append(pygame.Rect(i*100, j*100, 100, 100))

symbol = "X"


def main():
    symbol = choose_starting_symbol()
    nr_of_guesses = 9
    # 0 represents 'there was no guess'
    # 1 represents '0'
    # 2 represent 'X'
    guesses = [0] * 9

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                i = 0
                for rectangle in rectangles:
                    if rectangle.collidepoint(mouse_pos):
                        if symbol == "O" and guesses[i] == 0: 
                            guesses[i] = 1
                            symbol = "X"
                            nr_of_guesses -= 1
                        elif symbol == "X" and guesses[i] == 0: 
                            guesses[i] = 2
                            symbol = "O"
                            nr_of_guesses -= 1
                    i += 1

        draw_window(guesses)

        winner = check_for_win(guesses)
        if winner:
            if winner[0] == 1:
                draw_winner(LIGHT_GREEN, winner, guesses)
                wait_for_user_click()
                break
            elif winner[0] == 2:
                draw_winner(LIGHT_RED, winner, guesses)
                wait_for_user_click()
                break
        if nr_of_guesses == 0:
            wait_for_user_click()
            break

    main()


def draw_window(guesses):
    pygame.draw.rect(WIN, "Black", player_surf)

    vertical_line1 = pygame.Rect(99, 0, 2, 300)
    vertical_line2 = pygame.Rect(199, 0, 2, 300)
    horizontal_line1 = pygame.Rect(0, 99, 300, 2)
    horizontal_line2 = pygame.Rect(0, 199, 300, 2)
    pygame.draw.rect(WIN, "White", horizontal_line1)
    pygame.draw.rect(WIN, "White", horizontal_line2)
    pygame.draw.rect(WIN, "White", vertical_line1)
    pygame.draw.rect(WIN, "White", vertical_line2)

    for i in range(9):
        if guesses[i] == 1: WIN.blit(O, (rectangles[i].x + 20, rectangles[i].y))
        elif guesses[i] == 2: WIN.blit(X, (rectangles[i].x + 20, rectangles[i].y))
    
    pygame.display.update()


def choose_starting_symbol():
    global symbol
    if symbol == "O": symbol = "X"
    elif symbol == "X": symbol = "O"
    return symbol


def check_for_win(guesses):
    if guesses[0] == 1 and guesses[1] == 1 and guesses[2] == 1: return 1, 0, 1, 2
    elif guesses[0] == 2 and guesses[1] == 2 and guesses[2] == 2: return 2, 0, 1, 2
    elif guesses[3] == 1 and guesses[4] == 1 and guesses[5] == 1: return 1, 3, 4, 5
    elif guesses[3] == 2 and guesses[4] == 2 and guesses[5] == 2: return 2, 3, 4, 5
    elif guesses[6] == 1 and guesses[7] == 1 and guesses[8] == 1: return 1, 6, 7, 8
    elif guesses[6] == 2 and guesses[7] == 2 and guesses[8] == 2: return 2, 6, 7, 8

    elif guesses[0] == 1 and guesses[3] == 1 and guesses[6] == 1: return 1, 0, 3, 6
    elif guesses[0] == 2 and guesses[3] == 2 and guesses[6] == 2: return 2, 0, 3, 6
    elif guesses[1] == 1 and guesses[4] == 1 and guesses[7] == 1: return 1, 1, 4, 7
    elif guesses[1] == 2 and guesses[4] == 2 and guesses[7] == 2: return 2, 1, 4, 7
    elif guesses[2] == 1 and guesses[5] == 1 and guesses[8] == 1: return 1, 2, 5, 8
    elif guesses[2] == 2 and guesses[5] == 2 and guesses[8] == 2: return 2, 2, 5, 8

    elif guesses[0] == 1 and guesses[4] == 1 and guesses[8] == 1: return 1, 0, 4, 8
    elif guesses[0] == 2 and guesses[4] == 2 and guesses[8] == 2: return 2, 0, 4, 8
    elif guesses[2] == 1 and guesses[4] == 1 and guesses[6] == 1: return 1, 2, 4, 6
    elif guesses[2] == 2 and guesses[4] == 2 and guesses[6] == 2: return 2, 2, 4, 6

    return False


def wait_for_user_click():
    while True:
        flag = True
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if not flag:
            break


def draw_winner(color, n, guesses):
    pygame.draw.rect(WIN, "Black", player_surf)

    pygame.draw.rect(WIN, color, rectangles[n[1]])
    pygame.draw.rect(WIN, color, rectangles[n[2]])
    pygame.draw.rect(WIN, color, rectangles[n[3]])

    vertical_line1 = pygame.Rect(99, 0, 2, 300)
    vertical_line2 = pygame.Rect(199, 0, 2, 300)
    horizontal_line1 = pygame.Rect(0, 99, 300, 2)
    horizontal_line2 = pygame.Rect(0, 199, 300, 2)
    pygame.draw.rect(WIN, "White", horizontal_line1)
    pygame.draw.rect(WIN, "White", horizontal_line2)
    pygame.draw.rect(WIN, "White", vertical_line1)
    pygame.draw.rect(WIN, "White", vertical_line2)

    for i in range(9):
        if guesses[i] == 1: WIN.blit(O, (rectangles[i].x + 20, rectangles[i].y))
        elif guesses[i] == 2: WIN.blit(X, (rectangles[i].x + 20, rectangles[i].y))

    pygame.display.update()


if __name__ == "__main__":
    main()