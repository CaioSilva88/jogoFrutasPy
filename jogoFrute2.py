import pygame
from random import randint
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.font.init()

# texto

font = pygame.font.get_default_font()
# para MENU
opcao = pygame.font.SysFont(font, 30)
opcao2 = pygame.font.SysFont(font, 30)
venceu = pygame.font.SysFont(font, 100)
# para placar e time
placar = pygame.font.SysFont(font,30)

# tela

tela = pygame.display.set_mode((700,400))
pygame.display.set_caption('After Life')


# posicoes, velocidades, clock, contadores e sair

branco = (255,255,255)
velocidade = 20
relogio = pygame.time.Clock()
sair = True
sair2 = True
x = 350
y = 270
x1 = randint(0,600)
y1 = - 100
x2 = randint(0,600)
y2 = - 60
x3 = randint(0,600)
y3 = -50
x4 = randint(0,600)
y4 = -200
x5 = randint(0,600)
y5 = -50
posx_fruta1 = randint(0,600)
posy_fruta1 = -100
x6 = randint(0,600)
y6 = - 80
x7 = randint(0,600)
y7 = - 120
x8 = randint(0,600)
y8 = - 100
x9 = randint(0,600)
y9 = - 90

cont = 0 #cont melancia
cont2 = 0 # cont maca
cont3 = 0 # abacate
cont4 = 0 #lagrima 1
cont5 = 0 #laranja

# imagens

fundo = pygame.image.load('night01.png')
fundoFase2 = pygame.image.load('fundoFase2.png')
fundoFase3 = pygame.image.load('fundoFase3.png')
fundoFinal = pygame.image.load('final.png')
fundoArcade = pygame.image.load('fundoArcade.jpg')
contextoArcade =pygame.image.load('contextoArcade.jpg')
contextoDesafio = pygame.image.load('contextoDesafio.jpg')
gameOver = pygame.image.load('gameOver.jpg')
menu = pygame.image.load('./fruta/menu2.png')
p1 = pygame.image.load('f1.png')
p2 = pygame.image.load('f2.png')
p3 = pygame.image.load('f3.png')
m1 = pygame.image.load('m1.png')
m2 = pygame.image.load('m2.png')
melancia = pygame.image.load('./fruta/melancia02.png')
maca = pygame.image.load('./fruta/maca.png')
abacate = pygame.image.load('./fruta/Abacate.png')
laranja = pygame.image.load('./fruta/Laranja.png')
lagrima = pygame.image.load('./fruta/Lagrima.png')
cereja = pygame.image.load('./fruta/Cereja.png')
ct1 = pygame.image.load('ola.png')
ct2 = pygame.image.load('boas vindas.png')
ct3 = pygame.image.load('contexto1.png')
ct4 = pygame.image.load('contexto2.png')
ct5 = pygame.image.load('contexto3.png')
ct6 = pygame.image.load('contexto4.png')
ct7 = pygame.image.load('contexto5.png')
ct8 = pygame.image.load('contexto6.png')
ct9 = pygame.image.load('contexto7.png')
ct10 = pygame.image.load('contexto8.png')



def fase1():
    global menu_selecao,quadro,melancia,event,maca,abacate,laranja,lagrima,cereja,fundo,x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,velocidade,posx_fruta1,posy_fruta1,sair,cont,cont2,cont3,cont4,cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        # eventos do controle

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d and x < 610:
                x += velocidade

            if event.key == pygame.K_a and x > 0:
                x -= velocidade




        # tela, imagem1

        tela.blit(fundo, (0, 0))

        # velocidade em andamento

       # y1 += velocidade - 10  # melancia
        y2 += velocidade - 11  # maca
        #y3 += velocidade - 8  # abacate
        y4 += velocidade - 5  # lagrima1
        y5 += velocidade - 10  # laranja
        #posy_fruta1 += velocidade - 8  # lagrima2

        # frutas no final, volta
        if (y1 > 400):
            x1 = randint(0, 600)
            y1 = -30
        if (y2 > 400):
            x2 = randint(0, 600)
            y2 = -30
        if (y3 > 400):
            x3 = randint(0, 600)
            y3 = -30
        if (y4 > 380):
            x4 = randint(0, 600)
            y4 = -30
        if (y5 > 400):
            x5 = randint(0, 600)
            y5 = -30
        if (posy_fruta1 > 380):
            posy_fruta1 = -30

        # placar
        #text = opcao.render('Melancia: ' + str(cont), 1, (branco))
        #tela.blit(text, (5, 10))
        text = opcao.render('Pegue 10 Macas:  ' + str(cont2), 1, (branco))
        tela.blit(text, (5, 10))
        #text = opcao.render('| Abacate: ' + str(cont3), 1, (branco))
       # tela.blit(text, (220, 10))
        text = opcao.render('Pegue 10 Laranjas: ' + str(cont5), 1, (branco))
        tela.blit(text, (5, 40))
        text = opcao.render('  | Lagrimas: ' + str(cont4), 1, (branco))
        tela.blit(text, (200, 40))
        text = opcao.render('FASE 1  ' , 1, (branco))
        tela.blit(text, (5, 380))

        # colisao
        # melancia
        if ((x < x1 + 60 and y < y1 + 80) and (x + 50 > x1 and y < y1 + 80)):
            cont += 1
            x1 = randint(0, 600)
            y1 = -100
        # maca
        if ((x < x2 + 60 and y < y2 + 80) and (x + 50 > x2 and y < y2 + 80)):
            if(cont2<=9):
                cont2 += 1
            x2 = randint(0, 600)
            y2 = -100
        # abacate
        if ((x < x3 + 60 and y < y3 + 80) and (x + 50 > x3 and y < y3 + 80)):
            cont3 += 1
            x3 = randint(0, 600)
            y3 = -100
        # lagrima1
        if ((x < x4 + 60 and y < y4 + 80) and (x + 50 > x4 and y < y4 + 80)):
            if(cont2>=1):
                cont2 -= 1  # maca
            if(cont5>=1):
                cont5 -= 1  # laranja

            cont4 += 1

            x4 = randint(0, 600)
            y4 = -100
        # largrima 2
        if ((x < posx_fruta1 + 60 and y < posy_fruta1 + 80) and (x + 50 > posx_fruta1 and y < posy_fruta1 + 80)):
            cont4 += 1
            posx_fruta1 = randint(0, 600)
            posy_fruta1 = -100

        # laranja
        if ((x < x5 + 60 and y < y5 + 80) and (x + 50 > x5 and y < y5 + 80)):
            if (cont5 <= 9):
                cont5 += 1
            x5 = randint(0, 600)
            y5 = -100

        # chamando os quadros / animacao

        frame = animacao(quadro)
        quadro += 1
        if quadro >= 7:
            quadro = 1

        # blitar na tela

        tela.blit(frame, (x, y))
        #tela.blit(melancia, (x1, y1))
        tela.blit(maca, (x2, y2))
        #tela.blit(abacate, (x3, y3))
        tela.blit(lagrima, (x4, y4))
        tela.blit(laranja, (x5, y5))
       # tela.blit(lagrima, (posx_fruta1, posy_fruta1))

        if(cont5>=10 and cont2 >=10):
            cont2 = 0
            cont4 = 0
            cont5 = 0
            fase2()

        relogio.tick(15)
        pygame.display.update()

def fase2():

    global menu_selecao, quadro, melancia, event, maca, abacate, laranja, lagrima, cereja, fundo, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, velocidade, posx_fruta1, posy_fruta1, sair, cont, cont2, cont3, cont4, cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        # eventos do controle

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d and x < 610:
                x += velocidade

            if event.key == pygame.K_a and x > 0:
                x -= velocidade

        # tela, imagem1

        tela.blit(fundoFase2, (0, 0))

        # velocidade em andamento

        # y1 += velocidade - 10  # melancia
        y2 += velocidade - 11  # maca
        y3 += velocidade - 8  # abacate
        y4 += velocidade - 5  # lagrima1
        y5 += velocidade - 10  # laranja
        # posy_fruta1 += velocidade - 8  # lagrima2

        # frutas no final, volta
        if (y1 > 400):
            x1 = randint(0, 600)
            y1 = -30
        if (y2 > 400):
            x2 = randint(0, 600)
            y2 = -30
        if (y3 > 400):
            x3 = randint(0, 600)
            y3 = -30
        if (y4 > 380):
            x4 = randint(0, 600)
            y4 = -30
        if (y5 > 400):
            x5 = randint(0, 600)
            y5 = -30
        if (posy_fruta1 > 380):
            posy_fruta1 = -30

        # placar
        # text = opcao.render('Melancia: ' + str(cont), 1, (branco))
        # tela.blit(text, (5, 10))
        text = opcao.render('Pegue 10 Macas:  ' + str(cont2), 1, (branco))
        tela.blit(text, (5, 10))
        text = opcao.render('Pegue 10 Abacates: ' + str(cont3), 1, (branco))
        tela.blit(text, (220, 10))
        text = opcao.render('Pegue 10 Laranjas: ' + str(cont5), 1, (branco))
        tela.blit(text, (5, 40))
        text = opcao.render('  | Lagrimas: ' + str(cont4), 1, (branco))
        tela.blit(text, (200, 40))
        text = opcao.render('FASE 2  ', 1, (branco))
        tela.blit(text, (5, 380))

        # colisao
        # melancia
        if ((x < x1 + 60 and y < y1 + 80) and (x + 50 > x1 and y < y1 + 80)):
            cont += 1
            x1 = randint(0, 600)
            y1 = -100
        # maca
        if ((x < x2 + 60 and y < y2 + 80) and (x + 50 > x2 and y < y2 + 80)):
            if (cont2 <= 9):
                cont2 += 1
            x2 = randint(0, 600)
            y2 = -100
        # abacate
        if ((x < x3 + 60 and y < y3 + 80) and (x + 50 > x3 and y < y3 + 80)):
            cont3 += 1
            x3 = randint(0, 600)
            y3 = -100
        # lagrima1
        if ((x < x4 + 60 and y < y4 + 80) and (x + 50 > x4 and y < y4 + 80)):
            if (cont2 >= 1):
                cont2 -= 1  # maca
            if (cont5 >= 1):
                cont5 -= 1  # laranja
            if(cont3>=1):
                cont3 -=1 # abacate

            cont4 += 1

            x4 = randint(0, 600)
            y4 = -100
        # largrima 2
        if ((x < posx_fruta1 + 60 and y < posy_fruta1 + 80) and (x + 50 > posx_fruta1 and y < posy_fruta1 + 80)):
            cont4 += 1
            posx_fruta1 = randint(0, 600)
            posy_fruta1 = -100

        # laranja
        if ((x < x5 + 60 and y < y5 + 80) and (x + 50 > x5 and y < y5 + 80)):
            if (cont5 <= 9):
                cont5 += 1
            x5 = randint(0, 600)
            y5 = -100

        # chamando os quadros / animacao

        frame = animacao(quadro)
        quadro += 1
        if quadro >= 7:
            quadro = 1

        # blitar na tela

        tela.blit(frame, (x, y))
        # tela.blit(melancia, (x1, y1))
        tela.blit(maca, (x2, y2))
        tela.blit(abacate, (x3, y3))
        tela.blit(lagrima, (x4, y4))
        tela.blit(laranja, (x5, y5))
        # tela.blit(lagrima, (posx_fruta1, posy_fruta1))

        if (cont5 >= 10 and cont2 >= 10 and cont3 >=10):
            cont2 = 0
            cont3 = 0
            cont4 = 0
            cont5 = 0
            fase3()


        relogio.tick(15)
        pygame.display.update()


def arcade():

    global menu_selecao, quadro, melancia, event, maca, abacate, laranja, lagrima, cereja, fundo, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, velocidade, posx_fruta1, posy_fruta1, sair, cont, cont2, cont3, cont4, cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        # eventos do controle

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d and x < 610:
                x += velocidade

            if event.key == pygame.K_a and x > 0:
                x -= velocidade
            if event.key == pygame.K_0:
                sair = False
        # tela, imagem1

        tela.blit(fundoArcade, (0, 0))

        # velocidade em andamento

        y1 += velocidade - 10  # melancia
        y2 += velocidade - 11  # maca
        y3 += velocidade - 8  # abacate
        y4 += velocidade - 5  # lagrima1
        y5 += velocidade - 10  # laranja
        posy_fruta1 += velocidade - 8  # lagrima2

        # frutas no final, volta
        if (y1 > 400):
            x1 = randint(0, 600)
            y1 = -30
        if (y2 > 400):
            x2 = randint(0, 600)
            y2 = -30
        if (y3 > 400):
            x3 = randint(0, 600)
            y3 = -30
        if (y4 > 380):
            x4 = randint(0, 600)
            y4 = -30
        if (y5 > 400):
            x5 = randint(0, 600)
            y5 = -30
        if (posy_fruta1 > 380):
            posy_fruta1 = -30

        # placar

        text = opcao.render('Macas:  ' + str(cont2), 1, (branco))
        tela.blit(text, (5, 10))
        text = opcao.render('Abacates: ' + str(cont3), 1, (branco))
        tela.blit(text, (220, 10))
        text = opcao.render('Laranjas: ' + str(cont5), 1, (branco))
        tela.blit(text, (5, 40))
        text = opcao.render(' Lagrimas: ' + str(cont4), 1, (branco))
        tela.blit(text, (200, 40))
        text = opcao.render('Melancias: ' + str(cont), 1, (branco))
        tela.blit(text, (340, 40))
        text = opcao.render('ARCADE ', 1, (branco))
        tela.blit(text, (5, 380))
        text = opcao.render('Pressione 0 para sair ', 1, (branco))
        tela.blit(text, (490, 380))

        # colisao
        # melancia
        if ((x < x1 + 60 and y < y1 + 80) and (x + 50 > x1 and y < y1 + 80)):

            cont += 1
            x1 = randint(0, 600)
            y1 = -100
        # maca
        if ((x < x2 + 60 and y < y2 + 80) and (x + 50 > x2 and y < y2 + 80)):

            cont2 += 1
            x2 = randint(0, 600)
            y2 = -100
        # abacate
        if ((x < x3 + 60 and y < y3 + 80) and (x + 50 > x3 and y < y3 + 80)):

            cont3 += 1
            x3 = randint(0, 600)
            y3 = -100
        # lagrima1
        if ((x < x4 + 60 and y < y4 + 80) and (x + 50 > x4 and y < y4 + 80)):
            if (cont2 >= 1):
                cont2 -= 1  # maca
            if (cont5 >= 1):
                cont5 -= 1  # laranja
            if(cont3>=1):
                cont3 -=1 # abacate
            if(cont>=1):
                cont -=1

            cont4 += 1

            x4 = randint(0, 600)
            y4 = -100
        # largrima 2
        if ((x < posx_fruta1 + 60 and y < posy_fruta1 + 80) and (x + 50 > posx_fruta1 and y < posy_fruta1 + 80)):
            cont4 += 1
            if (cont2 >= 1):
                cont2 -= 1  # maca
            if (cont5 >= 1):
                cont5 -= 1  # laranja
            if (cont3 >= 1):
                cont3 -= 1  # abacate
            if (cont >= 1):
                cont -= 1
            posx_fruta1 = randint(0, 600)
            posy_fruta1 = -100

        # laranja
        if ((x < x5 + 60 and y < y5 + 80) and (x + 50 > x5 and y < y5 + 80)):

            cont5 += 1
            x5 = randint(0, 600)
            y5 = -100

        # chamando os quadros / animacao

        frame = animacao(quadro)
        quadro += 1
        if quadro >= 7:
            quadro = 1

        # blitar na tela

        tela.blit(frame, (x, y))
        tela.blit(melancia, (x1, y1))
        tela.blit(maca, (x2, y2))
        tela.blit(abacate, (x3, y3))
        tela.blit(lagrima, (x4, y4))
        tela.blit(laranja, (x5, y5))
        tela.blit(lagrima, (posx_fruta1, posy_fruta1))




        relogio.tick(15)
        pygame.display.update()


def final():
    global menu_selecao, quadro, melancia, event, maca, abacate, laranja, lagrima, cereja, fundo, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, velocidade, posx_fruta1, posy_fruta1, sair, cont, cont2, cont3, cont4, cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        tela.blit(fundoFinal,(0,0))
        tela.blit(m1,(500,270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Pressione ENTER para sair ', 1, (branco))
        tela.blit(text, (5, 10))

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                sair = False

        relogio.tick(15)
        pygame.display.update()

        #if event.type == pygame.KEYDOWN:

def fase3():

    global menu_selecao, quadro, melancia, event, maca, abacate, laranja, lagrima, cereja, fundo, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, velocidade, posx_fruta1, posy_fruta1, sair, cont, cont2, cont3, cont4, cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        # eventos do controle

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d and x < 610:
                x += velocidade

            if event.key == pygame.K_a and x > 0:
                x -= velocidade

        # tela, imagem1

        tela.blit(fundoFase3, (0, 0))

        # velocidade em andamento

        y1 += velocidade - 10  # melancia
        y2 += velocidade - 11  # maca
        y3 += velocidade - 8  # abacate
        y4 += velocidade - 5  # lagrima1
        y5 += velocidade - 10  # laranja
        posy_fruta1 += velocidade - 8  # lagrima2

        # frutas no final, volta
        if (y1 > 400):
            x1 = randint(0, 600)
            y1 = -30
        if (y2 > 400):
            x2 = randint(0, 600)
            y2 = -30
        if (y3 > 400):
            x3 = randint(0, 600)
            y3 = -30
        if (y4 > 380):
            x4 = randint(0, 600)
            y4 = -30
        if (y5 > 400):
            x5 = randint(0, 600)
            y5 = -30
        if (posy_fruta1 > 380):
            posy_fruta1 = -30

        # placar

        text = opcao.render('Pegue 10 Macas:  ' + str(cont2), 1, (branco))
        tela.blit(text, (5, 10))
        text = opcao.render('Pegue 10 Abacates: ' + str(cont3), 1, (branco))
        tela.blit(text, (220, 10))
        text = opcao.render('Pegue 10 Laranjas: ' + str(cont5), 1, (branco))
        tela.blit(text, (5, 40))
        text = opcao.render('  | Lagrimas: ' + str(cont4), 1, (branco))
        tela.blit(text, (200, 40))
        text = opcao.render('Pegue 10 Melancias: ' + str(cont), 1, (branco))
        tela.blit(text, (340, 40))
        text = opcao.render('FASE 3 ', 1, (branco))
        tela.blit(text, (5, 380))

        # colisao
        # melancia
        if ((x < x1 + 60 and y < y1 + 80) and (x + 50 > x1 and y < y1 + 80)):
            if(cont<=9):
                cont += 1
            x1 = randint(0, 600)
            y1 = -100
        # maca
        if ((x < x2 + 60 and y < y2 + 80) and (x + 50 > x2 and y < y2 + 80)):
            if (cont2 <= 9):
                cont2 += 1
            x2 = randint(0, 600)
            y2 = -100
        # abacate
        if ((x < x3 + 60 and y < y3 + 80) and (x + 50 > x3 and y < y3 + 80)):
            if(cont3<=9):
                cont3 += 1
            x3 = randint(0, 600)
            y3 = -100
        # lagrima1
        if ((x < x4 + 60 and y < y4 + 80) and (x + 50 > x4 and y < y4 + 80)):
            if (cont2 >= 1):
                cont2 -= 1  # maca
            if (cont5 >= 1):
                cont5 -= 1  # laranja
            if(cont3>=1):
                cont3 -=1 # abacate
            if(cont>=1):
                cont -=1

            cont4 += 1

            x4 = randint(0, 600)
            y4 = -100
        # largrima 2
        if ((x < posx_fruta1 + 60 and y < posy_fruta1 + 80) and (x + 50 > posx_fruta1 and y < posy_fruta1 + 80)):
            cont4 += 1
            if (cont2 >= 1):
                cont2 -= 1  # maca
            if (cont5 >= 1):
                cont5 -= 1  # laranja
            if (cont3 >= 1):
                cont3 -= 1  # abacate
            if (cont >= 1):
                cont -= 1
            posx_fruta1 = randint(0, 600)
            posy_fruta1 = -100

        # laranja
        if ((x < x5 + 60 and y < y5 + 80) and (x + 50 > x5 and y < y5 + 80)):
            if (cont5 <= 9):
                cont5 += 1
            x5 = randint(0, 600)
            y5 = -100

        # chamando os quadros / animacao

        frame = animacao(quadro)
        quadro += 1
        if quadro >= 7:
            quadro = 1

        # blitar na tela

        tela.blit(frame, (x, y))
        tela.blit(melancia, (x1, y1))
        tela.blit(maca, (x2, y2))
        tela.blit(abacate, (x3, y3))
        tela.blit(lagrima, (x4, y4))
        tela.blit(laranja, (x5, y5))
        tela.blit(lagrima, (posx_fruta1, posy_fruta1))

        if (cont5 >= 10 and cont2 >= 10 and cont3 >=10 and cont >=10):
            cont = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            cont5 = 0
            final()


        relogio.tick(15)
        pygame.display.update()



def desafio():

    global x6,y6,x7,y7,x8,y8,x9,y9,menu_selecao, quadro, melancia, event, maca, abacate, laranja, lagrima, cereja, fundo, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, velocidade, posx_fruta1, posy_fruta1, sair, cont, cont2, cont3, cont4, cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        # eventos do controle

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d and x < 610:
                x += velocidade

            if event.key == pygame.K_a and x > 0:
                x -= velocidade
            if event.key == pygame.K_0:
                sair = False
        # tela, imagem1

        tela.blit(fundoArcade, (0, 0))

        # velocidade em andamento


        y4 += velocidade - 5  # lagrima1
        posy_fruta1 += velocidade - 8  # lagrima2
        y6 += velocidade - 5
        y7 += velocidade - 2
        y8 += velocidade - 10
        y9 += velocidade - 5

        # frutas no final, volta

        if (y4 > 380):
            x4 = randint(0, 600)
            y4 = -30
        if (y6 > 380):
                x6 = randint(0, 600)
                y6 = -60
        if (y7 > 380):
            x7 = randint(0, 600)
            y7 = -90
        if(y8 > 380):
            x8 = randint(0, 600)
            y8 = -90
        if (y9 > 380):
            x9 = randint(0, 600)
            y9 = -90

        if (posy_fruta1 > 380):
            posy_fruta1 = -30

        # placar


        text = opcao.render(' Lagrimas: ' + str(cont4), 1, (branco))
        tela.blit(text, (200, 40))

        text = opcao.render('DESAFIO ', 1, (branco))
        tela.blit(text, (5, 380))
        text = opcao.render('Pressione 0 para sair ', 1, (branco))
        tela.blit(text, (490, 380))

        # colisao
        # lagrima1
        if ((x < x6 + 60 and y < y6 + 80) and (x + 50 > x6 and y < y6 + 80)):

            cont4 += 1

            x6 = randint(0, 600)
            y6 = -100
        if ((x < x7 + 60 and y < y7 + 80) and (x + 50 > x7 and y < y7 + 80)):
            cont4 += 1

            x7 = randint(0, 600)
            y7 = -50
        if ((x < x8 + 60 and y < y8 + 80) and (x + 50 > x8 and y < y8 + 80)):
            cont4 += 1

            x8 = randint(0, 600)
            y8 = -100
        if ((x < x9 + 60 and y < y9 + 80) and (x + 50 > x9 and y < y9 + 80)):
            cont4 += 1

            x9 = randint(0, 600)
            y9 = -100
        if ((x < x4 + 60 and y < y4 + 80) and (x + 50 > x4 and y < y4 + 80)):
            cont4 += 1

            x4 = randint(0, 600)
            y4 = -100
        # largrima 2
        if ((x < posx_fruta1 + 60 and y < posy_fruta1 + 80) and (x + 50 > posx_fruta1 and y < posy_fruta1 + 80)):
            cont4 += 1
            posx_fruta1 = randint(0, 600)
            posy_fruta1 = -100


        # chamando os quadros / animacao

        frame = animacao(quadro)
        quadro += 1
        if quadro >= 7:
            quadro = 1

        if(cont4 >=3):
            over()

        # blitar na tela

        tela.blit(frame, (x, y))
        tela.blit(lagrima, (x4, y4))
        tela.blit(lagrima, (x6, y6))
        tela.blit(lagrima, (x7, y7))
        tela.blit(lagrima, (x8, y8))
        tela.blit(lagrima, (x9, y9))
        tela.blit(lagrima, (posx_fruta1, posy_fruta1))




        relogio.tick(15)
        pygame.display.update()


def over():
    global menu_selecao, quadro, melancia, event, maca, abacate, laranja, lagrima, cereja, fundo, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, velocidade, posx_fruta1, posy_fruta1, sair, cont, cont2, cont3, cont4, cont5

    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        tela.blit(gameOver, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_0:
                sair = False

        relogio.tick(15)
        pygame.display.update()



def animacao(gid):

    if(gid == 1):
        return p1
    if (gid == 2):
        return p1
    if (gid == 3):
        return p1
    if (gid == 4):
        return p2
    if (gid == 5):
        return p2
    if (gid == 6):
        return p3
    if (gid == 7):
        return p3
quadro = 1
quadro2 = 1





# funcao de menu

def Menu(numero):
    global tela, menu,menu_selecao,quadro2

    # iniciar jogo
    if (numero == 1):
        tela.blit(menu, (0, 0))

        text = opcao.render('> Jogar < ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('Controles ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Sobre ', 1, (branco))
        tela.blit(text, (280, 280))
        text = opcao.render('Sair ', 1, (branco))
        tela.blit(text, (280, 310))

        relogio.tick(15)
        pygame.display.update()

        #controles
    if (numero == 2):
        tela.blit(menu, (0, 0))

        text = opcao.render('Jogar ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('> Controles < ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Sobre ', 1, (branco))
        tela.blit(text, (280, 280))
        text = opcao.render('Sair ', 1, (branco))
        tela.blit(text, (280, 310))

        relogio.tick(15)
        pygame.display.update()

        # sobre
    if (numero == 3):
            tela.blit(menu, (0, 0))

            text = opcao.render('Jogar ', 1, (branco))
            tela.blit(text, (280, 220))
            text = opcao.render('Controles ', 1, (branco))
            tela.blit(text, (280, 250))
            text = opcao.render('> Sobre < ', 1, (branco))
            tela.blit(text, (280, 280))
            text = opcao.render('Sair ', 1, (branco))
            tela.blit(text, (280, 310))

            relogio.tick(15)
            pygame.display.update()

        # sair
    if (numero == 4):
        tela.blit(menu, (0, 0))

        text = opcao.render('Jogar ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('Controles ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Sobre ', 1, (branco))
        tela.blit(text, (280, 280))
        text = opcao.render('> Sair < ', 1, (branco))
        tela.blit(text, (280, 310))

        relogio.tick(15)
        pygame.display.update()


    # ENTER no Sobre
    if (numero == 7):


        tela.blit(menu, (0, 0))
        text = opcao.render('Desenvolvido por: Caio  ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('Ver: 1.0 ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Pressione 0 para voltar  ', 1, (branco))
        tela.blit(text, (280, 350))

        relogio.tick(15)
        pygame.display.update()

        # ENTER no Controles
    if(numero == 6):
        tela.blit(menu, (0, 0))
        text = opcao.render('MOVER PARA ESQUERDA: "A"  ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('MOVER PARA DIREITA: "D" ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Pressione 0 para voltar  ', 1, (branco))
        tela.blit(text, (280, 350))

        relogio.tick(15)
        pygame.display.update()
    if(numero == 9):
        tela.blit(menu, (0, 0))


        text = opcao.render('> Modo Historia < ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('Modo Arcade ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Modo Desafio ', 1, (branco))
        tela.blit(text, (280, 280))


        text = opcao.render('Pressione 0 para voltar ', 1, (branco))
        tela.blit(text, (280, 350))
        text = opcao.render('Pressione 1 para selecionar ', 1, (branco))
        tela.blit(text, (280, 380))



        relogio.tick(15)
        pygame.display.update()
    if(numero == 10):
        tela.blit(menu, (0, 0))

        text = opcao.render('Modo Historia ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('> Modo Arcade < ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('Modo Desafio ', 1, (branco))
        tela.blit(text, (280, 280))
        text = opcao.render('Pressione 0 para voltar ', 1, (branco))
        tela.blit(text, (280, 350))
        text = opcao.render('Pressione 1 para selecionar ', 1, (branco))
        tela.blit(text, (280, 380))

        relogio.tick(15)
        pygame.display.update()
    if(numero == 11):
        tela.blit(menu, (0, 0))

        text = opcao.render('Modo Historia ', 1, (branco))
        tela.blit(text, (280, 220))
        text = opcao.render('Modo Arcade ', 1, (branco))
        tela.blit(text, (280, 250))
        text = opcao.render('> Modo Desafio < ', 1, (branco))
        tela.blit(text, (280, 280))
        text = opcao.render('Pressione 0 para voltar ', 1, (branco))
        tela.blit(text, (280, 350))
        text = opcao.render('Pressione 1 para selecionar ', 1, (branco))
        tela.blit(text, (280, 380 ))

        relogio.tick(15)
        pygame.display.update()

    if(numero ==13):

        tela.blit(ct1,(0,0))

        tela.blit(m1, (500, 270))
        tela.blit(p1,(100,270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))


        relogio.tick(15)
        pygame.display.update()
    if(numero == 14):
        tela.blit(ct2,(0,0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))


        relogio.tick(15)
        pygame.display.update()
    if(numero == 15):
        tela.blit(ct3, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))


        relogio.tick(15)
        pygame.display.update()

    if(numero == 16):
        tela.blit(ct4,(0,0))
        tela.blit(m1,(500,270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()
    if(numero == 17):
        tela.blit(ct5, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()
    if(numero == 18):
        tela.blit(ct6, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()
    if (numero == 19):
        tela.blit(ct7, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()
    if (numero == 20):
        tela.blit(ct8, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()
    if (numero == 21):
        tela.blit(ct9, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()
    if (numero == 22):
        tela.blit(ct10, (0, 0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))
        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (500, 185))

        relogio.tick(15)
        pygame.display.update()

    if (numero == 23):
        if(menu_selecao == 22):
            menu_selecao = 23
        fase1()

    if(numero == 30):

        tela.blit(contextoArcade,(0,0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))

        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (530, 380))
        relogio.tick(15)
        pygame.display.update()

    if(numero == 31):
        if(menu_selecao == 30):
            menu_selecao = 30
        if(menu_selecao == 32):
            menu_selecao = 31

        arcade()

    if(numero == 40):
        if(menu_selecao == 39):
            menu_selecao = 40

        tela.blit(contextoDesafio,(0,0))
        tela.blit(m1, (500, 270))
        tela.blit(p1, (100, 270))

        text = opcao.render('Seta para baixo> ', 1, (branco))
        tela.blit(text, (530, 380))
        relogio.tick(15)
        pygame.display.update()
    if (numero == 41):
        if(menu_selecao == 42):
            menu_selecao = 41
        desafio()


menu_selecao = 1
menu_historia = 13
n = 1






while sair:
    for event in pygame.event.get():



        if event.type == pygame.QUIT:
                sair = False

    Menu(menu_selecao)

    # ficar preso no menu
    if (menu_selecao == 0):
        menu_selecao = 1
    if (menu_selecao == 5):
        menu_selecao = 4
    if(menu_selecao == 8):
        menu_selecao = 9
    if(menu_selecao == 12):
        menu_selecao = 11

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_UP :

            menu_selecao-=1
            Menu(menu_selecao)


        if event.key == pygame.K_DOWN :

            menu_selecao += 1

            Menu( menu_selecao)


        if event.key == pygame.K_RETURN and menu_selecao == 3:

            menu_selecao = 7
            Menu(menu_selecao)

        if event.key == pygame.K_0:
            menu_selecao = 2
            Menu(menu_selecao)
        if event.key == pygame.K_RETURN and menu_selecao == 3:
            menu_selecao = 6
            Menu(menu_selecao)
        if event.key == pygame.K_RETURN and menu_selecao == 2:
            menu_selecao = 6
            Menu(menu_selecao)

        if event.key == pygame.K_0 and menu_selecao == 6:
            menu_selecao = 2
            Menu(menu_selecao)
        if event.key == pygame.K_0 and menu_selecao == 9:
            menu_selecao = 1
            Menu(menu_selecao)
        if event.key == pygame.K_0 and menu_selecao == 10:
            menu_selecao = 1
            Menu(menu_selecao)
        if event.key == pygame.K_0 and menu_selecao == 11:
            menu_selecao = 1
            Menu(menu_selecao)

        if event.key == pygame.K_RETURN and menu_selecao == 4:
            sair = False
        if event.key == pygame.K_RETURN and menu_selecao ==1:
            menu_selecao = 9
            Menu(menu_selecao)


        if event.key == pygame.K_RETURN and menu_selecao == 13:
            menu_selecao = 14
            Menu(menu_selecao)
        if event.key == pygame.K_1 and menu_selecao ==  9:
            menu_selecao = 13
        if event.key == pygame.K_1 and menu_selecao == 10:
            menu_selecao = 30
            Menu(menu_selecao)
        if event.key == pygame.K_1 and menu_selecao ==11:
            menu_selecao = 40
            Menu(menu_selecao)


                # GAME
                 #fase1()






pygame.quit()