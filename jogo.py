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
explosao_sound = pygame.mixer.Sound("assets/explosao.wav")
missile_sound = pygame.mixer.Sound("assets/missile.wav")
# Funções Gerais #############s
def mostraIron(x, y):
    gamedisplay.blit(car_img, (x, y))
def mostraMissile(x, y):
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
    pygame.mixer.Sound.play(explosao_sound)
    pygame.mixer.music.stop()
    message_display("Você bateu!")
def escrevePlacar(contador):
    font = pygame.font.SysFont("perpetua", 40)
    text = font.render("Desvios: "+str(contador), True, white)
    gamedisplay.blit(text, (10, 30))
def game_loop():
    # Looping do Jogo
    pygame.mixer.music.load("assets/ironsound.mp3")
    # parametro -1, é looping infinito
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    ironPosicaoX = 330
    ironPosicaoY = 450
    movimentoX = 0
    largura_car = 53
    altura_iron = 150
    # random é um sorteio de 0 até 800
    missilePosicaoX = random.randrange(0, larguraTela)
    missilePosicaoY = -600
    largura_missile = 53
    altura_missile = 150
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



        ironPosicaoX = ironPosicaoX + movimentoX
        gamedisplay.fill(white)
        gamedisplay.blit(fundo, (0, 0))
        mostraIron(ironPosicaoX, ironPosicaoY)
        escrevePlacar(contador)
        if ironPosicaoX > larguraTela - largura_car :
            ironPosicaoX = larguraTela-largura_car
        elif ironPosicaoX < 0:
            ironPosicaoX = 0
        mostraMissile(missilePosicaoX, missilePosicaoY)
        missilePosicaoY = missilePosicaoY + missile_speed
        if missilePosicaoY > alturaTela:
            missilePosicaoY = 0 - altura_missile
            missilePosicaoX = random.randrange(0, larguraTela)
            missile_speed = missile_speed + 1
            contador = contador + 1
            pygame.mixer.Sound.play(missile_sound)
        if ironPosicaoY + 50 < missilePosicaoY + altura_missile:
            if ironPosicaoX < missilePosicaoX and ironPosicaoX + largura_car > missilePosicaoX or missilePosicaoX+largura_missile > ironPosicaoX and missilePosicaoX+largura_missile < ironPosicaoX + largura_car:
                morteIron()
        pygame.display.update()
        clock.tick(60)
game_loop()
