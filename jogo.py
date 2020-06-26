import pygame
import time
import random
pygame.init()
# Variáveis Gerais #############s
larguraTela = 335
alturaTela = 512
gamedisplay = pygame.display.set_mode((larguraTela, alturaTela))
clock = pygame.time.Clock()
# RGB (Red, Green, Blue) (0,255)
fontes = pygame.font.get_fonts()
print(fontes)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
car_img = pygame.image.load('assets/car_p.png').convert_alpha()
mini_img = pygame.image.load('assets/minii.png').convert_alpha()
fundo = pygame.image.load("assets/rua.png")
iconeJogo = pygame.image.load("assets/icon.png")
pygame.display.set_icon(iconeJogo)
pygame.display.set_caption('Getaway driver')
#explosao_sound = pygame.mixer.Sound("assets/")

# Funções Gerais #############s
def mostraCar(x, y):
    gamedisplay.blit(car_img, (x, y))
def mostraMini(x, y):
    gamedisplay.blit(mini_img, (x, y))
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game_loop()
def morteIron():
    #pygame.mixer.Sound.play(explosao_sound)
    pygame.mixer.music.stop()
    message_display("Você bateu!")
def escrevePlacar(contador):
    font = pygame.font.SysFont("perpetua", 40)
    text = font.render("Desvios: "+str(contador), True, white)
    gamedisplay.blit(text, (10, 30))
def game_loop():
    # Looping do Jogo
    pygame.mixer.music.load("assets/Top_Gear.mp3")
    # parametro -1, é looping infinito
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    car_posicaoX = 330
    car_posicaoY = 450
    movimentoX = 0
    largura_car = 53
    altura_car = 150
    # random é um sorteio de 0 até 800
    missilePosicaoX = random.randrange(0, larguraTela)
    missilePosicaoY = -600
    largura_mini = 53
    altura_mini = 150
    missile_speed = 7
    contador = 0
    iron_speed = 10
    while True:
        # inicio -  event.get() devolve uma lista de eventos que estão acontecendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit() é comando native terminar o programa
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = iron_speed * -1 
                elif event.key == pygame.K_RIGHT:
                    movimentoX = iron_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoX = 0
        # fim -  event.get() devolve uma lista de eventos que estão acontecendo



        car_posicaoX = car_posicaoX + movimentoX
        gamedisplay.fill(white)
        gamedisplay.blit(fundo, (0, 0))
        mostraCar(car_posicaoX, car_posicaoY)
        escrevePlacar(contador)
        if car_posicaoX > larguraTela - largura_car :
            car_posicaoX = larguraTela-largura_car
        elif car_posicaoX < 0:
            car_posicaoX = 0
        mostraMini(missilePosicaoX, missilePosicaoY)
        missilePosicaoY = missilePosicaoY + missile_speed
        if missilePosicaoY > alturaTela:
            missilePosicaoY = 0 - altura_mini
            missilePosicaoX = random.randrange(0, larguraTela)
            missile_speed = missile_speed + 1
            contador = contador + 1

        if car_posicaoY + 50 < missilePosicaoY + altura_mini:
            if car_posicaoX < missilePosicaoX and car_posicaoX + largura_car > missilePosicaoX or missilePosicaoX+largura_mini > car_posicaoX and missilePosicaoX+largura_mini < car_posicaoX + largura_car:
                morteIron()
        pygame.display.update()
        clock.tick(60)
game_loop()
