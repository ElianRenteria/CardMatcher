import pygame
import random, time
import card


pygame.init()
matchSound = pygame.mixer.Sound("sounds/match.mp3")
matchSound.set_volume(.5)
flipSound = pygame.mixer.Sound("sounds/flip.wav")
flipSound.set_volume(.5)
game_complete_sound = pygame.mixer.Sound("sounds/game_complete.mp3")
game_complete_sound.set_volume(.75)
game_complete = False
font = pygame.font.Font('freesansbold.ttf', 32)
winner_text = font.render("Play Again", True, (35, 35, 35))
textRect = winner_text.get_rect()
textRect.center = (800, 500)
play_again_button = pygame.Rect(550,450,500,100)
cards = []
for i in range(0,14):
    cards.append(pygame.transform.scale(pygame.image.load("images/"+str(i)+".png"),(100,145)))

game = []
match = pygame.transform.scale(pygame.image.load("match.png"),(578,262))
def shuffle():
    global game
    game = []
    deck1 = cards[1:14]
    deck2 = cards[1:14]
    while len(deck1) > 0 or len(deck2) > 0:
        if len(deck1) > 0:
            r = random.randint(0, len(deck1)-1)
            c = card.Card(deck1[r])
            c.type = cards.index(deck1[r])
            game.append(c)
            deck1.remove(deck1[r])
        if len(deck2) > 0:
            r = random.randint(0, len(deck2)-1)
            c = card.Card(deck2[r])
            c.type = cards.index(deck2[r])
            game.append(c)
            deck2.remove(deck2[r])

def pickCard():
    global card1, card2
    for card in game:
        if card.hitBox.collidepoint(pygame.mouse.get_pos()):
            if card1 is None:
                card.show = True
                card1 = card
                flipSound.play(0,300,250)
            elif card2 is None and (card1 != card):
                card.show = True
                card2 = card
                check(card1, card2)

def check(c1,c2):
    global card1, card2, matchSound, game, game_complete
    if c1.type != c2.type:
        draw()
        pygame.display.update()
        flipSound.play(0,300,250)
        pygame.time.wait(1000)
        c1.show = False
        c2.show = False
    elif c1.type == c2.type:
        draw()
        window.blit(match, (511, 300))
        pygame.display.update()
        matchSound.play(0,2500,500)
        pygame.time.wait(1000)
    card1, card2 = None, None
    game_complete = True
    for card in game:
        if not card.show:
            game_complete = False
            break
    if game_complete:
        game_complete_sound.play(0,3000,500)



def draw():
    if not game_complete:
        window.fill((53, 101, 77))
        for i in range(0, len(game)):
            if i < 6:
                if game[i].show:
                    window.blit(game[i].image, ((i)*150+380, 100))
                else:
                    window.blit(cards[0], ((i) * 150 + 380, 100))
                    game[i].x = (i) * 150 + 380
                    game[i].y = 100
                    game[i].hitBox = pygame.Rect(game[i].x, game[i].y, 100, 145)
            elif i < 13:
                if game[i].show:
                    window.blit(game[i].image, ((i-6)*150+300, 300))
                else:
                    window.blit(cards[0], ((i - 6) * 150 + 300, 300))
                    game[i].x = (i-6)*150+300
                    game[i].y = 300
                    game[i].hitBox = pygame.Rect(game[i].x, game[i].y, 100, 145)
            elif i < 20:
                if game[i].show:
                    window.blit(game[i].image, ((i-13)*150+300, 500))
                else:
                    window.blit(cards[0], ((i - 13) * 150 + 300, 500))
                    game[i].x = (i - 13) * 150 + 300
                    game[i].y = 500
                    game[i].hitBox = pygame.Rect(game[i].x, game[i].y, 100, 145)
            else:
                if game[i].show:
                    window.blit(game[i].image, ((i-20)* 150+380, 700))
                else:
                    window.blit(cards[0], ((i - 20) * 150 + 380, 700))
                    game[i].x = (i - 20) * 150 + 380
                    game[i].y = 700
                    game[i].hitBox = pygame.Rect(game[i].x, game[i].y, 100, 145)
    else:
        global font
        window.fill((40,40,40))
        if not play_again_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, (0, 153, 0), play_again_button,0,100)
        elif play_again_button.collidepoint(pygame.mouse.get_pos()) and not pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(window, (50, 163, 50), play_again_button, 0, 100)
        else:
            pygame.draw.rect(window, (0, 200, 0), play_again_button, 0, 100)
        window.blit(winner_text, textRect)


window = pygame.display.set_mode((1600,1000))




card1, card2 = None, None
run = True
shuffle()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP and not game_complete:
            pickCard()
    draw()
    pygame.display.update()
