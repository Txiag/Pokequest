import pygame
import os
import sys
import random
res = 2

playerg = 'FB'
def resoluçao(objeto):
    global res
    if objeto == 'tela':
        return (400 * res, 300 * res)
    if objeto == 'retrato':
        if res == 1:
            return (100, 67)
        if res == 2:
            return (199, 135)
        if res == 3:
            return (298, 203)
    if objeto == 'mostrarret1':
        if res == 1:
            return 140
        if res == 2:
            return 217
        if res == 3:
            return 412
    if objeto == 'mostrarret2':
        if res == 1:
            return 110
        if res == 2:
            return 219
        if res == 3:
            return 328
    if objeto == 'baseinimiga':
        if res == 1:
            return (225, 55)
        if res == 2:
            return (262, 64)
        if res == 3:
            return (423, 104)
            return (423, 104)
    if objeto == 'basealiada':
        if res == 1:
            return (250, 30)
        if res == 2:
            return (418, 49)
        if res == 3:
            return (700, 80)
    if objeto == 'principal1':
        if res == 1:
            return (250, 30)
        if res == 2:
            return (altura // 2)
        if res == 3:
            return (700, 80)


APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))  # Pasta origem
fundo_batalha = pygame.image.load("fundo_batalha.png")
pygame.mixer.init()
os.chdir(APP_FOLDER+'/Sons')
pygame.mixer.music.load('main_music.mp3')
pygame.init()
beep = pygame.mixer.Sound('beep.wav')
os.chdir(APP_FOLDER)
font = pygame.font.Font('gamefont.ttf', 40)
font2 = pygame.font.Font('gamefont.ttf', 15)
sec = 50
size = largura, altura = resoluçao('tela')  # Definir tamanho da tela
fator_tamanho = 3
display = pygame.display.set_mode(size)
pygame.display.set_caption("Pokéquest")
icon_janela = pygame.image.load('icon.png')
pygame.display.set_icon(icon_janela)
os.chdir(APP_FOLDER + "/pkmns")
os.chdir(APP_FOLDER + '/animaçoes')
barra_branca = pygame.image.load('ponto_branco.png')
barra = pygame.image.load('barra.png')
os.chdir(APP_FOLDER)
barra = pygame.transform.scale(barra, size)
barra_branca = pygame.transform.scale(barra_branca, (25 * fator_tamanho, 2 * fator_tamanho))
inimigos_derrotados = 0
permitido_andar = False
text_box = pygame.image.load('text_box.png')
text_box = pygame.transform.scale(text_box, (largura * res, altura * res))
tela_sel_pokemon = pygame.image.load('tela_sel_pokemon.png')
os.chdir(APP_FOLDER + "/pkmns")
# POKEMONS                                                                                                                                                                                                                    ]
ids = [["1b.png", "1bw.png", 'VENOSAURO', 'GRAMA', 'VENENO', ['RAIO SOLAR', 'FOLHA NAVALHA', 'TERREMOTO', 'ESFERA DE ENERGIA'], 200, 200],
       ["2b.png", "2bw.png", 'CHARIZARD', 'FOGO', 'LUTADOR', ['LANÇA-CHAMAS', 'CÍRCULO DE FOGO', 'INFERNO', 'TERREMOTO'], 200, 200],
       ["3b.png", "3bw.png", 'BLASTOISE','ÁGUA', 'NENHUM', ['JATO D\'ÁGUA', 'BOLHAS', 'MORDIDA', 'TERREMOTO'], 200, 200],
       ["4b.png", "4bw.png", 'PIKACHU', 'ELÉTRICO', 'NENHUM', ['INVESTIDA', 'RAIO', 'CHOQUE DO TROVÃO', 'INVESTIDA RELÂMPAGO'], 200, 200],
       ["5b.png", "5bw.png", 'NIDOQUEEN', 'VENENO', 'TERRA', ['BOLHA VENENOSA', 'MORDIDA', 'TERREMOTO', 'ARRANHAR'], 200, 200],
       ["6b.png", "6bw.png", 'NIDOKING', 'VENENO', 'TERRA', ['BOLHA VENENOSA', 'MORDIDA', 'TERREMOTO', 'ARRANHAR'],200, 200],
       ["7b.png", "7bw.png", 'ARCANINE', 'FOGO', 'NENHUM', ['LANÇA-CHAMAS', 'INFERNO', 'MORDIDA', 'INVESTIDA'], 200, 200],
       ["8b.png","8bw.png", 'MACHAMP', 'LUTADOR', 'NENHUM', ['GOLPE BAIXO', 'TERREMOTO', 'HIPER RAIO', 'DESABAMENTO'], 200, 200],
       ["9b.png", "9bw.png", 'GASTLY','FANTASMA', 'VENENO', ['ASSOMBRAR', 'MORDIDA', 'PESADELO', 'ESFERA NEGRA'], 200, 200],
       ["10b.png", "10bw.png", 'GENGAR', 'FANTASMA', 'VENENO', ['BOLHA VENENOSA', 'MORDIDA', 'ARRANHAR', 'PESADELO'], 200, 200],
       ["11b.png", "11bw.png", 'ELECTABUZZ', 'ELÉTRICO','NENHUM', ['RAIO', 'ATAQUE RÁPIDO', 'INVESTIDA RELÂMPAGO', 'ESFERA DE RAIOS'], 200, 200],
       ["12b.png", "12bw.png", 'SNORLAX', 'NORMAL', 'NENHUM', ['INVESTIDA', 'ARRANHAR', 'MORDIDA', 'TERREMOTO'], 200, 200],
       ["13b.png", "13bw.png", 'DRAGONITE', 'DRAGÃO', 'VOADOR', ['HIPER RAIO', 'LANÇA-CHAMAS', 'TERREMOTO', 'ESFERA DE ENERGIA'], 200, 200],
       ["14b.png", "14bw.png", 'MEGANIUM', 'GRAMA', 'NENHUM',['RAIO SOLAR', 'FOLHA NAVALHA', 'INVESTIDA', 'BOLHA VENENOSA'], 200, 200],
       ["15b.png", "15bw.png", 'TYPHLOSION', 'FOGO', 'NENHUM', ['CÍRCULO DE FOGO', 'LANÇA-CHAMAS', 'MORDIDA', 'TERREMOTO'], 200, 200],
       ["16b.png", "16bw.png", 'FERALIGATR', 'ÁGUA', 'NENHUM', ['JATO D\'ÁGUA', 'BOLHAS', 'MORDIDA', 'TERREMOTO'], 200, 200],
       ["17b.png", "17bw.png", 'CROBAT', 'VOADOR','VENENO', ['BOLHA VENENOSA', 'FOLHA NAVALHA', 'TERREMOTO', 'ESFERA DE ENERGIA'],200, 200],
       ["18b.png", "18bw.png", 'ESPEON', 'PSIQUÍCO', 'NENHUM', ['CONFUSÃO', 'GOLPE PSIQUÍCO', 'ESFERA DE ENERGIA', 'GOLPE ESTRELADO'], 200, 200],
       ["19b.png", "19bw.png", 'UMBREON', 'TREVAS', 'NENHUM', ['ATORMENTAR', 'PESADELO', 'ESFERA NEGRA', 'DEVORADOR DE SONHOS'], 200, 200],
       ["20b.png", "20bw.png", 'STEELIX', 'METAL', 'TERRA', ['TERREMOTO', 'INVESTIDA', 'MORDIDA', 'DESABAMENTO'],200,200],
       ["21b.png", "21bw.png", 'HOUNDOOM', 'FOGO','TREVAS', ['PESADELO', 'LANÇA-CHAMAS', 'TERREMOTO', 'ESFERA DE ENERGIA'],200,200],
       ["22b.png", "22bw.png", 'TYRANITAR', 'PEDRA','TREVAS', ['MORDIDA', 'HIPER RAIO', 'DESABAMENTO', 'TERREMOTO'],200,200],
       ["23b.png", "23bw.png", 'SCEPTILE', 'GRAMA', 'NENHUM',['ARRANHAR', 'RAIO SOLAR', 'MORDIDA', 'TERREMOTO'],200,200],
       ["24b.png", "24bw.png", 'BLAZIKEN', 'FOGO', 'LUTADOR', ['GOLPE BAIXO', 'LABAREDA', 'BICADA', 'INFERNO'],200,200],
       ["25b.png", "25bw.png", 'SWAMPERT', 'ÁGUA','TERRA', ['JATO D\'ÁGUA', 'BOLHAS', 'TERREMOTO', 'MORDIDA'],200,200],
       ["26b.png", "26bw.png", 'GARDEVOIR', 'PSIQUÍCO', 'FADA', ['CONFUSÃO', 'GOLPE PSIQUÍCO', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200],
       ["27b.png", "27bw.png", 'AGGRON', 'METAL','PEDRA', ['DESABAMENTO', 'ATAQUE RÁPIDO', 'HIPER RAIO', 'TERREMOTO'],200,200],
       ["28b.png", "28bw.png", 'FLYGON', 'TERRA','DRAGÃO', ['GOLPE AÉREO', 'HIPER RAIO', 'GARRAS DE DRAGÃO', 'TERREMOTO'],200,200],
       ["29b.png", "29bw.png", 'MILOTIC', 'ÁGUA','NENHUM', ['NEVASCA', 'JATO D\'ÁGUA', 'CABEÇADA', 'QUEDA LIVRE'], 200,200],
       ["30b.png", "30bw.png", 'SALAMENCE', 'DRAGÃO', 'VOADOR', ['MORDIDA', 'GOLPE AÉREO', 'CABEÇADA', 'TERREMOTO'],200,200],
       ["31b.png", "31bw.png", 'LATIOS', 'DRAGÃO','PSIQUÍCO', ['GOLPE AÉREO', 'CABEÇADA', 'GOLPE PSIQUÍCO', 'HIPER RAIO'],200,200],
       ["32b.png", "32bw.png", 'TORTERRA', 'GRAMA', 'TERRA', ['TERREMOTO', 'FOLHA NAVALHA', 'ABSORVER', 'TERREMOTO'], 200,200],
       ["33b.png", "33bw.png", 'INFERNAPE', 'FOGO','LUTADOR', ['SOCO DE FOGO', 'LABAREDA', 'INFERNO', 'GOLPE BAIXO'], 200,200],
       ["34b.png", "34bw.png", 'EMPOLEON', 'ÁGUA', 'METAL', ['BOLHAS', 'JATO D\'ÁGUA', 'BICADA', 'GARRA DE METAL'],200,200],
       ["35b.png", "35bw.png", 'LUXRAY', 'ELÉTRICO','NENHUM', ['INVESTIDA TROVÃO', 'TROVÃO SELVAGEM', 'MORDIDA', 'MORDIDA RELÂMPAGO'],200,200],
       ["36b.png", "36bw.png", 'RAMPARDOS', 'PEDRA','NENHUM', ['CABEÇADA', 'BOLHA VENENOSA', 'DESABAMENTO', 'TERREMOTO'],200,200],
       ["37b.png", "37bw.png", 'PACHIRISU', 'ELÉTRICO','NENHUM', ['ATAQUE RÁPIDO', 'INVESTIDA RELÂMPAGO', 'RAIO', 'CHOQUE DO TROVÃO'],200,200],
       ["38b.png", "38bw.png", 'GASTRODON', 'ÁGUA', 'TERRA', ['BOLHA VENENOSA', 'JATO D\'ÁGUA', 'ATAQUE RÁPIDO', 'TERREMOTO'],200,200],
       ["39b.png", "39bw.png", 'GARCHOMP', 'DRAGÃO', 'TERRA', ['GARRAS DE DRAGÃO', 'DESABAMENTO', 'HIPER RAIO', 'TERREMOTO'],200,200],
       ["40b.png", "40bw.png", 'LUCARIO', 'LUTADOR','METAL',['ESFERA DE ENERGIA', 'DESABAMENTO', 'GOLPE KARATE', 'GOLPE BAIXO'],200,200],
       ["41b.png", "41bw.png", 'GLISCOR', 'TERRA', 'VOADOR', ['CORTE CRUZADO', 'MORDIDA', 'INVESTIDA AÉREA', 'ATAQUE RÁPIDO'],200,200],
       ["42b.png", "42bw.png", 'LEAFEON', 'GRAMA','NENHUM', ['FOLHA NAVALHA', 'ABSORVER', 'ESFERA DE ENERGIA', 'ARRANHAR'],200,200],
       ["43b.png", "43bw.png", 'GLACEON', 'GELO', 'NENHUM',['MORDIDA GLACIAL', 'NEVASCA', 'RAIO DE GELO', 'INVESTIDA'],200,200],
       ["44b.png", "44bw.png", 'PORYGON-Z ', 'NORMAL','NENHUM', ['CHOQUE DO TROVÃO', 'INVESTIDA', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200],
       ["45b.png", "45bw.png", 'GALLADE','PSIQUÍCO', 'LUTADOR', ['CORTE CRUZADO', 'ATAQUE RÁPIDO', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200]]


def multiplicador(tipoa, tipo1i, tipo2i, teste):
    if teste == False:
        m1 = multiplicador(tipoa, tipo2i, tipo1i, True)
        tipoa = get_type_txt(tipoa)
    m1 = 1
    m = 1
    if tipo1i != 'NENHUM':
        if tipoa == tipo1i and tipoa != 'DRAGÃO' and tipoa != 'FANTASMA':
            m = 1
        elif tipoa == tipo1i and tipoa == 'DRAGÃO':
            m = 2
        elif tipoa == 'ÁGUA' and (tipo1i == 'DRAGÃO' or tipo1i == 'GRAMA'):
            m = 0.5
        elif tipoa == 'ÁGUA' and (tipo1i == 'FOGO' or tipo1i == 'PEDRA' or tipo1i == 'TERRA'):
            m = 2
        elif tipoa == 'DRAGÃO' and (tipo1i == 'DRAGÃO' or tipo1i == 'GRAMA'):
            m = 0.5
        elif tipoa == 'ÁGUA' and (tipo1i == 'FOGO' or tipo1i == 'PEDRA' or tipo1i == 'TERRA'):
            m = 2
        elif tipoa == 'LUTADOR' and (tipo1i == 'NORMAL' or tipo1i == 'PEDRA' or tipo1i == 'AÇO' or tipo1i == 'GELO' or tipo1i == 'TREVAS'):
            m = 2
        elif tipoa == 'LUTADOR' and (tipo1i == 'VOADOR' or tipo1i == 'VENENO' or tipo1i == 'FADA' or tipo1i == 'PSIQUÍCO'):
            m = 0.5
        elif tipoa == 'LUTADOR' and (tipo1i == 'GHOST'):
            m = 0
        elif tipoa == 'VOADOR' and (tipo1i == 'LUTADOR' or tipo1i == 'GRAMA'):
            m = 2
        elif tipoa == 'VOADOR' and (tipo1i == 'PEDRA' or tipo1i == 'AÇO' or tipoli == 'ELÉTRICO'):
            m = 0.5
        elif tipoa == 'VENENO' and (tipo1i == 'VENENO' or tipo1i == 'TERRA' or tipo1i == 'PEDRA' or tipo1i == 'FANTASMA'):
            m = 0.5
        elif tipoa == 'VENENO' and (tipo1i == 'AÇO'):
            m = 0
        elif tipoa == 'VENENO' and (tipo1i == 'GRAMA' or tipo1i == 'FADA'):
            m = 2
        elif tipoa == 'TERRA' and (tipo1i == 'VOADOR'):
            m = 0.5
        elif tipoa == 'TERRA' and (tipo1i == 'VENENO' or tipo1i == 'PEDRA' or tipo1i == 'AÇO' or tipo1i == 'FOGO' or tipo1i == 'ELÉTRICO'):
            m = 2
        elif tipoa == 'TERRA' and (tipo1i == 'VOADOR'):
            m = 0
        elif tipoa == 'FANTASMA' and (tipo1i == tipoa or tipo1i == 'PSIQUÍCO'):
            m = 2
        elif tipoa == 'FANTASMA' and tipo1i == 'NORMAL':
            m = 0
        elif tipoa == 'FANTASMA' and tipo1i == 'TREVAS':
            m = 0.5
        elif tipoa == 'AÇO' and (tipo1i == 'PEDRA' or tipo1i == 'GELO' or tipo1i == 'FADA'):
            m = 2
        elif tipoa == 'AÇO' and (tipo1i == 'FOGO' or tipo1i == 'ÁGUA' or tipo1i == 'ELÉTRICO'):
            m = 0.5
        elif tipoa == 'FOGO' and (tipo1i == 'PEDRA' or tipo1i == 'ÁGUA' or tipo1i == 'DRAGÃO'):
            m = 0.5
        elif tipoa == 'FOGO' and (tipo1i == 'GRAMA' or tipo1i == 'GELO' or tipo1i == 'AÇO'):
            m = 2
        elif tipoa == 'GRAMA' and (tipo1i == 'VOADOR' or tipo1i == 'VENENO' or tipo1i == 'AÇO' or tipo1i == 'FOGO' or tipo1i == 'DRAGÃO'):
            m = 0.5
        elif tipoa == 'GRAMA' and (tipo1i == 'TERRA' or tipo1i == 'PEDRA' or tipo1i == 'ÁGUA'):
            m = 2
        elif tipoa == 'ELÉTRICO' and (tipo1i == 'VOADOR' or tipo1i == 'ÁGUA'):
            m = 2
        elif tipoa == 'ELÉTRICO' and (tipo1i == 'TERRA' or tipo1i == 'PEDRA'):
            m = 0
        elif tipoa == 'ELÉTRICO' and (tipo1i == 'GRAMA' or tipo1i == 'DRAGÃO'):
            m = 0.5
        elif tipoa == 'PSIQUÍCO' and (tipo1i == 'LUTADOR' or tipo1i == 'VENENO'):
            m = 2
        elif tipoa == 'PSIQUÍCO' and tipo1i == 'TREVAS':
            m = 0
        elif tipoa == 'PSIQUÍCO' and tipo1i == 'AÇO':
            m = 0.5
        elif tipoa == 'GELO' and (tipo1i == 'VOADOR' or tipo1i == 'TERRA' or tipo1i == 'GRAMA' or tipo1i == 'DRAGÃO'):
            m = 2
        elif tipoa == 'GELO' and (tipo1i == 'FOGO' or tipo1i == 'AÇO' or tipo1i == 'ÁGUA'):
            m = 0.5
        else:
            m = 1
    elif tipo1i == 'NENHUM':
        m = 1
    return m * m1

icons = []
pkmn_astro = [[pygame.image.load("13f1.png"), pygame.image.load("13f2.png"), 'DRAGONITE', 'DRAGÃO',
               'VOADOR', ['HIPER RAIO', 'LANÇA-CHAMAS', 'TERREMOTO', 'ESFERA DE ENERGIA'], 200, 200],
              [pygame.image.load("43f1.png"), pygame.image.load("43f2.png"), 'GLACEON', 'GELO',
               'NENHUM',['MORDIDA GLACIAL', 'NEVASCA', 'RAIO DE GELO', 'INVESTIDA'],200,200],
              [pygame.image.load("40f1.png"), pygame.image.load("40f2.png"), 'LUCARIO', 'LUTADOR',
               'METAL',['ESFERA DE ENERGIA', 'DESABAMENTO', 'GOLPE KARATE', 'GOLPE BAIXO'],200,200]]

pkmn_clara = [[pygame.image.load("26f1.png"), pygame.image.load("26f2.png"), 'GARDEVOIR', 'PSIQUÍCO',
               'FADA', ['CONFUSÃO', 'GOLPE PSIQUÍCO', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200],
              [pygame.image.load("43f1.png"), pygame.image.load("43f2.png"), 'GLACEON', 'GELO',
               'NENHUM',['MORDIDA GLACIAL', 'NEVASCA', 'RAIO DE GELO', 'INVESTIDA'],200,200],
              [pygame.image.load("10f1.png"), pygame.image.load("10f2.png"), 'GENGAR', 'FANTASMA',
               'VENENO', ['BOLHA VENENOSA', 'MORDIDA', 'ARRANHAR', 'PESADELO'], 200, 200]]

pkmn_ale = [[pygame.image.load("41f1.png"), pygame.image.load("41f2.png"), 'GLISCOR', 'TERRA', 'VOADOR', ['CORTE CRUZADO', 'MORDIDA', 'INVESTIDA AÉREA', 'ATAQUE RÁPIDO'],200,200],
              [pygame.image.load("43f1.png"), pygame.image.load("43f2.png"), 'GLACEON', 'GELO', 'NENHUM',['MORDIDA GLACIAL', 'NEVASCA', 'RAIO DE GELO', 'INVESTIDA'],200,200],
              [pygame.image.load("40f1.png"), pygame.image.load("40f2.png"), 'LUCARIO', 'LUTADOR','METAL',['ESFERA DE ENERGIA', 'DESABAMENTO', 'GOLPE KARATE', 'GOLPE BAIXO'],200,200]]

pkmn_luciana = [[pygame.image.load("35f1.png"), pygame.image.load("35f2.png"), 'LUXRAY', 'ELÉTRICO','NENHUM', ['INVESTIDA TROVÃO', 'TROVÃO SELVAGEM', 'MORDIDA', 'MORDIDA RELÂMPAGO'],200,200],
              [pygame.image.load("26f1.png"), pygame.image.load("26f2.png"), 'GARDEVOIR', 'PSIQUÍCO', 'FADA', ['CONFUSÃO', 'GOLPE PSIQUÍCO', 'ESFERA DE ENERGIA', 'TERREMOTO'],200,200],
              [pygame.image.load("12f1.png"), pygame.image.load("12f2.png"), 'SNORLAX', 'NORMAL', 'NENHUM', ['INVESTIDA', 'ARRANHAR', 'MORDIDA', 'TERREMOTO'], 200, 200]]

for i in range(1, 46):
    icons.append(pygame.image.load(str(i) + 'icon.png'))
#  FIM
os.chdir(APP_FOLDER + "/Sprites")
npc_icon = pygame.image.load('npcicon.png')
hp = [pygame.image.load('hp_high.png'), pygame.image.load('hp_med.png'), pygame.image.load('hp_low.png')]
base_inimiga = pygame.image.load('baseinimiga.png')
base_inimiga = pygame.transform.scale(base_inimiga, (resoluçao('baseinimiga')))
base_aliada = pygame.image.load('basealiada.png')
base_aliada = pygame.transform.scale(base_aliada, (resoluçao('basealiada')))

astro = ['Astro', 421, 367, pygame.image.load('Looking_Left_Astro.png'), pygame.image.load('Walking_Left_1_Astro.png'),
         pygame.image.load('Walking_Left_2_Astro.png'), pygame.image.load('astro_retrato.png'),
         pygame.image.load('astro_corpo1.png'), pygame.image.load('astro_corpo2.png'), pygame.image.load('astro_corpo3.png')]

clara = ['Clara', 421, 190, pygame.image.load('Looking_Left_Clara.png'), pygame.image.load('Walking_Left_1_Clara.png'),
         pygame.image.load('Walking_Left_2_Clara.png'), pygame.image.load('clara_retrato.png'),
         pygame.image.load('clara_corpo1.png'), pygame.image.load('clara_corpo2.png'),
         pygame.image.load('clara_corpo3.png')]

luciana = ['Luciana', 421, 131, pygame.image.load('Looking_Left_Luciana.png'),
           pygame.image.load('Walking_Left_1_Luciana.png'),pygame.image.load('Walking_Left_2_Luciana.png'),
           pygame.image.load('luciana_retrato.png'), pygame.image.load('luciana_corpo1.png'),
           pygame.image.load('luciana_corpo2.png'), pygame.image.load('luciana_corpo3.png')]

ale = ['Ale', 421, 264, pygame.image.load('Looking_Left_Ale.png'), pygame.image.load('Walking_Left_1_Ale.png'),
       pygame.image.load('Walking_Left_2_Ale.png'), pygame.image.load('ale_retrato.png'),
       pygame.image.load('ale_corpo1.png'), pygame.image.load('ale_corpo2.png'), pygame.image.load('ale_corpo3.png')]


def animainimigo(npc):
    global display, clock, base_inimiga, base_aliada, fundo_batalha, estado
    textos = ['VOCÊ NÃO VAI CONSEGUIR PASSAR DAQUI', 'MELHOR DIZER ADEUS PARA SUA NOTA!', 'EU NÃO VOU SER REPROVADA', 'EU QUASE MORRI FAZENDO AQUELA UL!A']
    for i in range(7, 10):
        clock.tick(5)
        posm = posx, posy = pygame.mouse.get_pos()
        display.blit(fundo_batalha, (0,0))
        display.blit(base_inimiga, (495, 134))
        display.blit(base_aliada, (3, 354))
        x = npc[i]
        x = pygame.transform.scale(x, (200, 200))
        display.blit(x, (522, 0))
        pygame.display.update()
    mostrar_texto('{}: {}'.format(npc[0], textos[(random.randrange(0, len(textos)))]))
    for i in range(522, 740, 5):
        clock.tick(100)
        x = npc[9]
        x = pygame.transform.scale(x, (200, 200))
        display.blit(fundo_batalha, (0, 0))
        display.blit(base_inimiga, (495, 134))
        display.blit(x, (i, 0))
        pygame.display.flip()

os.chdir(APP_FOLDER)
barratime = pygame.image.load('seu_time.png')
os.chdir(APP_FOLDER + "/animaçao1")  # Entrar na pasta de sprites
xD = []
xD2 = []
clock = pygame.time.Clock()
# receber animação de transição
for i in range(30, 83):
    c = pygame.image.load('00' + str(i) + '.png')
    c = (pygame.transform.scale(c, size))
    xD.append(c)
for i in range(83, 92):
    c = pygame.image.load('00' + str(i) + '.png')
    c = (pygame.transform.scale(c, size))
    xD2.append(c)
golpes = []
os.chdir(APP_FOLDER + "/Sons")
sonsgolpes = [pygame.mixer.Sound('golpe_karate.wav')]
os.chdir(APP_FOLDER + "/animaçoes/ataques/golpe_karate")
golpesaux = []
for i in range(6, 10):
    x = pygame.image.load("000" + str(i) + '.png')
    x = pygame.transform.scale(x, (800, 600))
    golpesaux.append(x)
for i in range(10, 58):
    x = pygame.image.load("00" + str(i) + '.png')
    x = pygame.transform.scale(x, (800, 600))
    golpesaux.append(x)
golpes.append(golpesaux)
del golpesaux
os.chdir(APP_FOLDER)

# fim

def golpe_karate():
    global display, golpes, fundo, sonsgolpes, clock
    sonsgolpes[0].play()
    for i in range(len(golpes[0])):
        display.blit(fundo, (0, 0))
        display.blit(golpes[0][i], (0, 0))
        pygame.display.flip()
        clock.tick(25)
luta = ''
def em_npc():
    global permitido_andar, x, y, player, APP_FOLDER, display, estado, luta, telaprincipal
    posx, posy = pygame.mouse.get_pos()
    if y >= 364 and y<= 370 and inimigos_derrotados == 0:
        permitido_andar = False
        y = 367
        telaprincipal[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in telaprincipal:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 356))
        pygame.display.flip()
        pygame.time.wait(350)
        estado = 'prepara'
        luta = 'astro'
    elif y >= 262 and y<= 268 and inimigos_derrotados == 1:
        permitido_andar = False
        y = 265
        telaprincipal[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in telaprincipal:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 254))
        pygame.display.flip()
        pygame.time.wait(350)
        estado = 'prepara'
        luta = 'ale'
    elif y >= 186 and y<= 193  and inimigos_derrotados == 2:
        permitido_andar = False
        y = 190
        telaprincipal[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in telaprincipal:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 180))
        pygame.display.flip()
        pygame.time.wait(350)
        estado = 'prepara'
        luta = 'clara'
    elif y >= 126 and y<= 134  and inimigos_derrotados == 3:
        permitido_andar = False
        y = 131
        telaprincipal[1] = player, (x, y)
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load("Looking_"+ pos +"_" + playerg + ".png")
        for i in telaprincipal:
            display.blit(i[0], (i[1]))
        display.blit(npc_icon, (429, 121))
        pygame.display.flip()
        pygame.time.wait(350)
        estado = 'prepara'
        luta = 'luciana'

def andarnpc(npc):
    global astro, clara, ale, luciana, display, x, y, clock, display, principal_fundo, player, estado, APP_FOLDER
    if npc == 'astro':
        for i in range(astro[1], x+20, -2):
            telaprincipal = [[principal_fundo, (0, 0)], [player, (x, y)], [astro[3], (astro[1], astro[2])],
                         [ale[3], (ale[1], ale[2])], [luciana[3], (luciana[1], luciana[2])],
                         [clara[3], (clara[1], clara[2])]]
            astro[1] = i
            astro[3], astro[4] = astro[4], astro[3]
            display.fill((0,0,0))
            for i1 in telaprincipal:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        astro[3] = pygame.image.load('Looking_Left_Astro.png')
        os.chdir(APP_FOLDER)
        mostrar_texto('Astro: Vamos batalhar!')
        estado = 'batalhaini'
    if npc == 'ale':
        for i in range(ale[1], x + 20, -2):
            telaprincipal = [[principal_fundo, (0, 0)], [player, (x, y)], [ale[3], (ale[1], ale[2])],
                             [luciana[3], (luciana[1], luciana[2])],
                             [clara[3], (clara[1], clara[2])]]
            ale[1] = i
            ale[3], ale[4] = ale[4], ale[3]
            display.fill((0, 0, 0))
            for i1 in telaprincipal:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        ale[3] = pygame.image.load('Looking_Left_Ale.png')
        os.chdir(APP_FOLDER)
        mostrar_texto('Ale: Meus pokémon vão te derrotar!')
        estado = 'batalhaini'
    if npc == 'clara':
        for i in range(clara[1], x + 20, -2):
            telaprincipal = [[principal_fundo, (0, 0)], [player, (x, y)], [luciana[3], (luciana[1], luciana[2])], [clara[3], (clara[1], clara[2])]]
            clara[1] = i
            clara[3], clara[4] = clara[4], clara[3]
            display.fill((0, 0, 0))
            for i1 in telaprincipal:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        clara[3] = pygame.image.load('Looking_Left_Clara.png')
        os.chdir(APP_FOLDER)
        mostrar_texto('Clara: Você não vai passar daqui!')
        estado = 'batalhaini'
    if npc == 'luciana':
        for i in range(luciana[1], x + 20, -2):
            telaprincipal = [[principal_fundo, (0, 0)], [player, (x, y)], [luciana[3], (luciana[1], luciana[2])],]
            luciana[1] = i
            luciana[3], luciana[4] = luciana[4], luciana[3]
            display.fill((0, 0, 0))
            for i1 in telaprincipal:
                display.blit(i1[0], i1[1])
            pygame.display.flip()
            clock.tick(15)
        os.chdir(APP_FOLDER + '/Sprites')
        luciana[3] = pygame.image.load('Looking_Left_Luciana.png')
        os.chdir(APP_FOLDER)
        mostrar_texto('Luciana: Não tem como eu perder isso aqui')
        estado = 'batalhaini'


walkleft = []
walkup = []
walkdown = []
walkright = []
runleft = []
runup = []
rundown = []
runright = []
launchpkb = []

# Genero e cor do personagem
os.chdir(APP_FOLDER)
os.chdir(APP_FOLDER + "/Sprites")
player = pygame.image.load("Looking_Down_" + playerg + ".png")  # Carregar imagem do personagem
feandar = 1  # Qual passo o personagem deu
pos = 'Down'  # Qual a últimap posição que o personagem andou
os.chdir(APP_FOLDER)  # Voltar para pasta origem
personagem_coordenadas = x, y = 50, 50  # Coordenados do personagem
fundo = pygame.image.load("fundo_batalha.png")  # Fundo
os.chdir(APP_FOLDER + '/pkmns')
pk1 = pygame.image.load('1b.png')
os.chdir(APP_FOLDER)
meutime = []
tela_nome = pygame.image.load('tela nome.png')
tela_sel = pygame.image.load('tela_sel.png')
# animaçoes


def animatransição(sprite):
    global barra, display, clock, barra_branca, xD, xD2
    sprite = pygame.transform.scale(sprite, (199, 135))
    for i in range(0, 20):
        clock.tick(12)
        display.blit(barra, (0, 0))
        display.blit(barra_branca, (100 + i, altura // 2))
        display.blit(barra_branca, (76 + i, altura // 2 - 25 * 2))
        display.blit(barra_branca, (500 - i, altura // 2 - 20 * 2))
        display.blit(barra_branca, (300 + i, altura // 2 - 25 * 2))
        display.blit(barra_branca, (450 + i, altura // 2))
        display.blit(barra_branca, (280 + i, altura // 2 - 40 * 2))
        display.blit(barra_branca, (265 + i, altura // 2))
        display.blit(sprite, ((largura // 2 - 50 * res)+i, 219))
        pygame.display.flip()



# fim
text_box = pygame.transform.scale(text_box, (800, 600))


def mostrar_texto(texto):
    frases = []
    if len(texto) >= 50:
        texto = texto.split()
        texto_pass = ''
        for i in texto:
            if (len(texto_pass) + len(i)) <= 50:
                texto_pass += i + ' '
            else:
                frases.append(texto_pass)
                texto_pass = i + ' '
    else:
        frases.append(texto)
    atualizar_texto(frases)

def atualizar_texto(frases):
    global display, text_box, telaatual, clock
    ultimo = ''
    cima = False
    for count in range(len(frases)):
        for i in range(len(frases[count])):
            ultimo = font.render(frases[count-1], True, [0, 0, 0])
            text = font.render(frases[count][0:i+1], True, [0, 0, 0])
            display.blit(text_box, (0, 0))
            if not(cima):
                display.blit(text, (35, 475))
                pygame.display.update((0, 452, 800, 148))
            if cima:
                display.blit(ultimo, (35, 475))
                display.blit(text, (35, 520))
                pygame.display.update((0, 452, 800, 148))
            clock.tick(60)
        if not(cima):
            cima = True
        else:
            cima = False
    clock.tick(2)


def andar():  # Função para andar
    global feandar, pos, x, y, APP_FOLDER, player, display, clock
    if x >= 405:
        x = 405
    if x <= 324:
        x = 324
    if y >= 575:
        y = 575
    feandar += 1
    feandar %= 4
    clocks = 15
    if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT] == 0:
        x += 2
        player = walkright[feandar]
        clock.tick(clocks)
        pos = 'Right'
    elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT] == 0:
        x -= 2
        player = walkleft[feandar]
        clock.tick(clocks)
        pos = 'Left'
    elif keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT] == 0:
        player = walkdown[feandar]
        y += 2
        clock.tick(clocks)
        pos = 'Down'
    elif keys[pygame.K_UP] and keys[pygame.K_LSHIFT] == 0:
        player = walkup[feandar]
        y -= 2
        clock.tick(clocks)
        pos = 'Up'

    # CORRIDA
    elif keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT] == 1:
        player = runright[feandar]
        x += 2 * fator_tamanho
        clock.tick(clocks)
        pos = 'Right'
    elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT] == 1:
        player = runleft[feandar]
        x -= 2 * fator_tamanho
        clock.tick(clocks)
        pos = 'Left'
    elif keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT] == 1:
        player = rundown[feandar]
        y += 2 * fator_tamanho
        clock.tick(clocks)
        pos = 'Down'
    elif keys[pygame.K_UP] and keys[pygame.K_LSHIFT] == 1:
        player = runup[feandar]
        y -= 2 * fator_tamanho
        clock.tick(clocks)
        pos = 'Up'
    else:
        os.chdir(APP_FOLDER + "/Sprites")
        player = pygame.image.load('Looking_' + pos + '_' + playerg + '.png')
        os.chdir(APP_FOLDER)

playername = ''
def escolhernome():
    global display, playername, clock
    caps = False
    if keys[pygame.K_CAPSLOCK] and not(caps):
        caps = True
    elif keys[pygame.K_CAPSLOCK] and caps == True:
        caps = False
    clock.tick(10)
    if keys[pygame.K_a] and not(caps):
        playername += 'a'
    elif keys[pygame.K_a] and caps:
        playername += 'A'
    elif keys[pygame.K_b] and not(caps):
        playername += 'b'
    elif keys[pygame.K_b] and caps:
        playername += 'B'
    elif keys[pygame.K_c] and not(caps):
        playername += 'c'
    elif keys[pygame.K_c] and caps:
        playername += 'C'
    elif keys[pygame.K_d] and not(caps):
        playername += 'd'
    elif keys[pygame.K_d] and caps:
        playername += 'D'
    elif keys[pygame.K_e] and not(caps):
        playername += 'e'
    elif keys[pygame.K_e] and caps:
        playername += 'E'
    elif keys[pygame.K_f] and not(caps):
        playername += 'f'
    elif keys[pygame.K_f] and caps:
        playername += 'F'
    elif keys[pygame.K_g] and not(caps):
        playername += 'g'
    elif keys[pygame.K_g] and caps:
        playername += 'G'
    elif keys[pygame.K_h] and not(caps):
        playername += 'h'
    elif keys[pygame.K_d] and caps:
        playername += 'H'
    elif keys[pygame.K_i] and not(caps):
        playername += 'i'
    elif keys[pygame.K_i] and caps:
        playername += 'I'
    elif keys[pygame.K_j] and not(caps):
        playername += 'j'
    elif keys[pygame.K_j] and caps:
        playername += 'J'
    elif keys[pygame.K_k] and not(caps):
        playername += 'k'
    elif keys[pygame.K_k] and caps:
        playername += 'K'
    elif keys[pygame.K_l] and not(caps):
        playername += 'l'
    elif keys[pygame.K_l] and caps:
        playername += 'L'
    elif keys[pygame.K_m] and not(caps):
        playername += 'm'
    elif keys[pygame.K_m] and caps:
        playername += 'M'
    elif keys[pygame.K_n] and not(caps):
        playername += 'n'
    elif keys[pygame.K_n] and caps:
        playername += 'N'
    elif keys[pygame.K_o] and not(caps):
        playername += 'o'
    elif keys[pygame.K_o] and caps:
        playername += 'O'
    elif keys[pygame.K_p] and not(caps):
        playername += 'p'
    elif keys[pygame.K_p] and caps:
        playername += 'P'
    elif keys[pygame.K_q] and not(caps):
        playername += 'q'
    elif keys[pygame.K_q] and caps:
        playername += 'Q'
    elif keys[pygame.K_r] and not(caps):
        playername += 'r'
    elif keys[pygame.K_r] and caps:
        playername += 'R'
    elif keys[pygame.K_s] and not(caps):
        playername += 's'
    elif keys[pygame.K_s] and caps:
        playername += 'S'
    elif keys[pygame.K_t] and not(caps):
        playername += 't'
    elif keys[pygame.K_t] and caps:
        playername += 'T'
    elif keys[pygame.K_u] and not(caps):
        playername += 'u'
    elif keys[pygame.K_u] and caps:
        playername += 'U'
    elif keys[pygame.K_v] and not(caps):
        playername += 'v'
    elif keys[pygame.K_v] and caps:
        playername += 'V'
    elif keys[pygame.K_w] and not(caps):
        playername += 'w'
    elif keys[pygame.K_w] and caps:
        playername += 'W'
    elif keys[pygame.K_x] and not(caps):
        playername += 'x'
    elif keys[pygame.K_u] and caps:
        playername += 'X'
    elif keys[pygame.K_y] and not(caps):
        playername += 'y'
    elif keys[pygame.K_y] and caps:
        playername += 'Y'
    elif keys[pygame.K_z] and not(caps):
        playername += 'z'
    elif keys[pygame.K_z] and caps:
        playername += 'Z'
    elif keys[pygame.K_BACKSPACE]:
        playername = playername[:len(playername)-1]

    return 0
posicons = []
for i in range(1, 10):
    xz = [icons[i - 1], i * 60, 200]
    posicons.append(xz)
for i in range(10, 19):
    xz = [icons[i - 1], (i - 9) * 60, 250]
    posicons.append(xz)
for i in range(19, 28):
    xz = [icons[i - 1], (i - 18) * 60, 300]
    posicons.append(xz)
for i in range(28, 37):
    xz = [icons[i - 1], (i - 27) * 60, 350]
    posicons.append(xz)
for i in range(37, 46):
    xz = [icons[i - 1], (i - 36) * 60, 400]
    posicons.append(xz)

id = 0
fundo_box = pygame.image.load('fundo_box.png')
fundo_box = pygame.transform.scale(fundo_box, (800, 600))


def mostrar_icons():
    global icons, display, posicons, id, fundo_box, barratime, clock
    display.blit(fundo_box, (0, 0))
    rect_id = posicons[id][0].get_rect(topleft=(posicons[id][1], posicons[id][2]))
    clock.tick(15)
    display.blit(posicons[id][0], (posicons[id][1], posicons[id][2] - 10))
    pygame.display.update(rect_id)
    display.blit(fundo_box, (0, 0))
    for i in range(len(posicons)):
        display.blit(posicons[i][0], (posicons[i][1], posicons[i][2]))
    clock.tick(15)
    display.blit(barratime, (0, 0))
    pygame.display.flip()

def escolher_ataque():
    global clock, idbatalha, keys, meutime, estado
    clock.tick(20)
    if keys[pygame.K_RIGHT]:
        idbatalha += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        idbatalha -= 1
        beep.play()
    elif keys[pygame.K_DOWN]:
        idbatalha += 2
        beep.play()
    elif keys[pygame.K_UP]:
        idbatalha -= 2
        beep.play()
    elif keys[pygame.K_SPACE]:
        atacar(meutime[0][5][idbatalha])
        mostrar_texto('{} usou {}'.format(meutime[0][2], meutime[0][5][idbatalha]))
        pygame.time.wait(200)
        if get_enemy()[0][6] > 0:
            ataque_inimigo()
        estado = 'selbatalha'
    idbatalha %= 4

def receber_pkmn(id):
    x = []
    for i in id:
        x.append(i)
    return x
def escolher_time_1():
    global keys, id, ids, meutime, beep
    if keys[pygame.K_RIGHT]:
        id += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        id -= 1
        beep.play()
    elif keys[pygame.K_DOWN]:
        id += 9
        beep.play()
    elif keys[pygame.K_UP]:
        id -= 9
        beep.play()
    elif keys[pygame.K_SPACE]:
        meutime.append(receber_pkmn(ids[id]))
    clock.tick(25)
    id = id % 45

selecionaicon = pygame.image.load('seleciona.png')
def selprincipal():
    global keys, id, beep, estado
    if keys[pygame.K_RIGHT]:
        id += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        id -= 1
        beep.play()
    elif keys[pygame.K_DOWN]:
        id += 2
        beep.play()
    elif keys[pygame.K_UP]:
        id -= 2
        beep.play()
    elif keys[pygame.K_SPACE]:
        if id == 0:
            estado = 'selataque'
        if id == 1:
            estado = 'selbatalha'
        if id == 2:
            estado = 'selpkmn'
    pygame.time.wait(80)
    clock.tick(15)
    id = id % 3

def blit_seleciona():
    global estado, id, selecionaicon, idbatalha
    posm = posx, posy = pygame.mouse.get_pos()
    posb = 0
    if estado == 'selbatalha':
        if id == 0:
            posb = (388, 409)
        elif id == 1:
            posb = (62,512)
        elif id == 2:
            posb = (721, 512)
    if estado == 'selataque':
        if idbatalha == 0:
            posb = (105, 394)
        elif idbatalha == 1:
            posb = (348, 394)
        elif idbatalha == 2:
            posb = (105, 488)
        elif idbatalha == 3:
            posb = (348, 488)
    return posb
def escolher_personagem_1():
    global keys, id
    if keys[pygame.K_RIGHT]:
        id += 1
    elif keys[pygame.K_LEFT]:
        id -= 1
    elif keys[pygame.K_DOWN]:
        id += 2
    elif keys[pygame.K_UP]:
        id -= 2
    elif keys[pygame.K_SPACE]:
        sel_gen(id)
    id %= 4
    mostrar_personagem()


def get_icon(txt):
    a = ''
    txt = str(txt)
    for i in txt:
        if i.isnumeric(): a += i
    return int(a)-1


def blit_time():
    global display, icons, meutime, ids, barratime
    xpos, ypos = pygame.mouse.get_pos()
    if len(meutime) == 1:
        x = get_icon(meutime[0][0])
        display.blit(icons[x], (20, 20))
        nome = font2.render(meutime[0][2], True, [255,255,255])
        display.blit(nome, (75, 19))
    if len(meutime) == 2:
        x = get_icon(meutime[0][0])
        display.blit(icons[x], (20, 20))
        nome = font2.render(meutime[0][2], True, [255,255,255])
        display.blit(nome, (75, 19))
        x = get_icon(meutime[1][0])
        display.blit(icons[x], (342, 20))
        nome = font2.render(meutime[1][2], True, [255,255,255])
        display.blit(nome, (397, 19))
    if len(meutime) == 3:
        x = get_icon(meutime[0][0])
        display.blit(icons[x], (20, 20))
        nome = font2.render(meutime[0][2], True, [255,255,255])
        display.blit(nome, (75, 19))
        x = get_icon(meutime[1][0])
        display.blit(icons[x], (342, 20))
        nome = font2.render(meutime[1][2], True, [255,255,255])
        display.blit(nome, (397, 19))
        x = get_icon(meutime[2][0])
        display.blit(icons[x], (667, 20))
        nome = font2.render(meutime[2][2], True, [255,255,255])
        display.blit(nome, (722, 19))
    if len(meutime) == 4:
        x = get_icon(meutime[0][0])
        display.blit(icons[x], (20, 20))
        nome = font2.render(meutime[0][2], True, [255,255,255])
        display.blit(nome, (75, 19))
        x = get_icon(meutime[1][0])
        display.blit(icons[x], (342, 20))
        nome = font2.render(meutime[1][2], True, [255,255,255])
        display.blit(nome, (397, 19))
        x = get_icon(meutime[2][0])
        display.blit(icons[x], (667, 20))
        nome = font2.render(meutime[2][2], True, [255,255,255])
        display.blit(nome, (722, 19))
        x = get_icon(meutime[3][0])
        display.blit(icons[x], (20, 78))
        nome = font2.render(meutime[3][2], True, [255, 255, 255])
        display.blit(nome, (75, 73))
    if len(meutime) == 5:
        x = get_icon(meutime[0][0])
        display.blit(icons[x], (20, 20))
        nome = font2.render(meutime[0][2], True, [255, 255, 255])
        display.blit(nome, (75, 19))
        x = get_icon(meutime[1][0])
        display.blit(icons[x], (342, 20))
        nome = font2.render(meutime[1][2], True, [255, 255, 255])
        display.blit(nome, (397, 19))
        x = get_icon(meutime[2][0])
        display.blit(icons[x], (667, 20))
        nome = font2.render(meutime[2][2], True, [255, 255, 255])
        display.blit(nome, (722, 19))
        x = get_icon(meutime[3][0])
        display.blit(icons[x], (20, 78))
        nome = font2.render(meutime[3][2], True, [255, 255, 255])
        display.blit(nome, (75, 73))
        x = get_icon(meutime[4][0])
        display.blit(icons[x], (342, 78))
        nome = font2.render(meutime[4][2], True, [255, 255, 255])
        display.blit(nome, (397, 73))
    if len(meutime) == 6:
        x = get_icon(meutime[0][0])
        display.blit(icons[x], (20, 20))
        nome = font2.render(meutime[0][2], True, [255, 255, 255])
        display.blit(nome, (75, 19))
        x = get_icon(meutime[1][0])
        display.blit(icons[x], (342, 20))
        nome = font2.render(meutime[1][2], True, [255, 255, 255])
        display.blit(nome, (397, 19))
        x = get_icon(meutime[2][0])
        display.blit(icons[x], (667, 20))
        nome = font2.render(meutime[2][2], True, [255, 255, 255])
        display.blit(nome, (722, 19))
        x = get_icon(meutime[3][0])
        display.blit(icons[x], (20, 78))
        nome = font2.render(meutime[3][2], True, [255, 255, 255])
        display.blit(nome, (75, 73))
        x = get_icon(meutime[4][0])
        display.blit(icons[x], (342, 78))
        nome = font2.render(meutime[4][2], True, [255, 255, 255])
        display.blit(nome, (397, 73))
        x = get_icon(meutime[5][0])
        display.blit(icons[x], (667, 78))
        nome = font2.render(meutime[5][2], True, [255, 255, 255])
        display.blit(nome, (722, 73))
def escolher_time():
    global display, icons, id
    escolher_time_1()
    mostrar_icons()


os.chdir(APP_FOLDER + '/Sprites')
principal = [pygame.image.load('Principal_FB.png'), pygame.image.load('Principal_FW.png'),
             pygame.image.load('Principal_MW.png'), pygame.image.load('Principal_MB.png')]

selboxes = []
for i in range(1, 5):
    selboxes.append(pygame.image.load('box_sel{}.png'.format(i)))
principalaux = []
for i in range(len(principal)):
    copy = principal[i]
    copy.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_SUB)
    principalaux.append(copy)
principal = [pygame.image.load('Principal_FB.png'), pygame.image.load('Principal_FW.png'),
             pygame.image.load('Principal_MW.png'), pygame.image.load('Principal_MB.png')]
os.chdir(APP_FOLDER)

idsel = 0
def get_selbox():
    global idsel, selboxes, tela_sel_pokemon
    if idsel == 0:
        x = [[tela_sel_pokemon, (0,0)], [selboxes[2], (177,143)], [selboxes[0], (443, 150)], [selboxes[0], (176, 258)],
             [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif idsel == 1:
        x = [[tela_sel_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[1], (443, 144)],
             [selboxes[0], (176, 258)], [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif idsel == 2:
        x = [[tela_sel_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[1], (176, 252)], [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif idsel == 3:
        x = [[tela_sel_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[0], (176, 258)], [selboxes[1], (443, 252)], [selboxes[0], (174, 374)], [selboxes[0], (443, 374)]]
    elif idsel == 4:
        x = [[tela_sel_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[0], (176, 258)], [selboxes[0], (443, 258)], [selboxes[1], (174, 370)], [selboxes[0], (443, 374)]]
    elif idsel == 5:
        x = [[tela_sel_pokemon, (0, 0)], [selboxes[3], (173, 148)], [selboxes[0], (443, 150)],
             [selboxes[0], (176, 258)], [selboxes[0], (443, 258)], [selboxes[0], (174, 374)], [selboxes[1], (443, 370)]]
    return x
def posicon(i, estado):
    x = 0
    if estado == 'icon':
        if i == 0: x = (215, 171)
        elif i == 1: x = (476, 176)
        elif i == 2: x = (215, 280)
        elif i == 3: x = (476, 283)
        elif i == 4: x = (217, 397)
        elif i == 5: x = (483, 398)
    elif estado == 'nome':
        if i == 0: x = (297, 162)
        elif i == 1: x = (572, 164)
        elif i == 2: x = (297, 273)
        elif i == 3: x = (572, 273)
        elif i == 4: x = (297, 388)
        elif i == 5: x = (572, 388)
    elif estado == 'hp1':
        if i == 0: x = (303, 201)
        elif i == 1: x = (571, 205)
        elif i == 2: x = (303, 312)
        elif i == 3: x = (571, 312)
        elif i == 4: x = (303, 428)
        elif i == 5: x = (571, 428)
    elif estado == 'hp2':
        if i == 0: x = (303+35, 201)
        elif i == 1: x = (571+35, 205)
        elif i == 2: x = (303+35, 312)
        elif i == 3: x = (571+35, 312)
        elif i == 4: x = (303+35, 428)
        elif i == 5: x = (571+35, 428)
    return x
def change_pokemon():
    global tela_sel_pokemon, selboxes, idsel, clock
    global icons, meutime
    x1 = []
    posm = pygame.mouse.get_pos()
    nomes = []
    hp1 = []
    hp2 = []
    for i in range(len(meutime)):
        aux = [icons[get_icon(meutime[i][0])], posicon(i, 'icon')]
        x1.append(aux)
        aux2 = [font2.render(meutime[i][2], True, [255, 255, 255]), posicon(i, 'nome')]
        nomes.append(aux2)
        aux3 = [font2.render(str(meutime[i][6]), True, [255, 255, 255]), posicon(i, 'hp1')]
        hp1.append(aux3)
        aux4 = [font2.render(str(meutime[i][7]), True, [255, 255, 255]), posicon(i, 'hp2')]
        hp2.append(aux4)

    x = get_selbox()
    x = x[0:len(meutime)+1]
    x = x + x1 + nomes + hp1 + hp2
    return x

def change_pokemon_2():
    global idsel, meutime, clock, beep, atualaliado, estado, spritestimen
    if keys[pygame.K_UP]:
        idsel -= 2
        beep.play()
    elif keys[pygame.K_DOWN]:
        idsel += 2
        beep.play()
    elif keys[pygame.K_RIGHT]:
        idsel += 1
        beep.play()
    elif keys[pygame.K_LEFT]:
        idsel -= 1
        beep.play()
    elif keys[pygame.K_SPACE]:
        estado = 'ataqueinimigo'
        meutime[0], meutime[idsel] = meutime[idsel], meutime[0]
        spritestimen[0], spritestimen[idsel] = spritestimen[idsel], spritestimen[0]
        atualaliado = meutime[0]
    idsel %= len(meutime)
    clock.tick(8)

def mostrar_personagem():
    global id, display, principal, fundo, principalaux
    display.blit(fundo, (0, 0))
    if id == 0:
        display.blit(principal[0], (200, 200))
        display.blit(principalaux[1], (400, 200))
        display.blit(principalaux[2], (200, 400))
        display.blit(principalaux[3], (400, 400))
    elif id == 1:
        display.blit(principalaux[0], (200, 200))
        display.blit(principal[1], (400, 200))
        display.blit(principalaux[2], (200, 400))
        display.blit(principalaux[3], (400, 400))
    elif id == 2:
        display.blit(principalaux[0], (200, 200))
        display.blit(principalaux[1], (400, 200))
        display.blit(principal[2], (200, 400))
        display.blit(principalaux[3], (400, 400))
    elif id == 3:
        display.blit(principalaux[0], (200, 200))
        display.blit(principalaux[1], (400, 200))
        display.blit(principalaux[2], (200, 400))
        display.blit(principal[3], (400, 400))
    pygame.time.wait(60)
    pygame.display.flip()


def sel_gen(id):
    global playerg, escolheu_personagem
    if id == 0:
        playerg = 'FB'
    elif id == 1:
        playerg = 'FW'
    elif id == 3:
        playerg = 'MB'
    elif id == 2:
        playerg = 'MW'
    escolheu_personagem = True

def blit_nome():
    global display, playername, font
    pygame.time.wait(40)
    posm = posx, posy = pygame.mouse.get_pos()
    textoa = "DIGITE SEU NOME"
    textoa = font.render(textoa, True, [0, 0, 0])
    display.blit(textoa, (94, 188))
    playernamea = font.render(playername, True, [0, 0, 0])
    display.blit(playernamea, (215, 79))
    font3 = pygame.font.Font('gamefont.ttf', 25)
    display.blit((font3.render('CONFIRMA', True, [0,0,0])), (638, 208))
    display.blit((font3.render('APAGAR', True, [0, 0, 0])), (521, 208))
    pygame.display.flip()

tela_ataque = pygame.image.load('tela ataque.png')
os.chdir(APP_FOLDER + '/Sprites')
barra_aliado = pygame.image.load('barra_aliado.png')
barra_inimigo = pygame.image.load('barra_inimigo.png')
os.chdir(APP_FOLDER)

def get_type(nome):
    global typeboxes
    if nome == 'RAIO SOLAR' or nome == 'FOLHA NAVALHA' or nome == 'ABSORVER':
        ret = 8
    if nome == 'ARRANHAR' or nome == 'HIPER RAIO' or nome == 'MORDIDA' or nome == 'ATAQUE RÁPIDO' or nome == 'CABEÇADA' or nome == 'INVESTIDA' or nome == 'GOLPE ESTRELADO':
        ret = 3
    if nome == 'TERREMOTO':
        ret = 0
    if nome == 'GOLPE KARATE' or nome == 'GOLPE BAIXO' or nome == 'CORTE CRUZADO':
        ret = 1
    if nome == 'JATO D\'ÁGUA' or nome == 'BOLHAS':
        ret = 2
    if nome == 'MORDIDA GLACIAL' or nome == 'RAIO DE GELO' or nome == 'NEVASCA':
        ret = 4
    if nome == 'DEVORADOR DE SONHOS' or nome == 'ATORMENTAR':
        ret = 5
    if nome == 'SOCO DE FOGO' or nome == 'INFERNO' or nome == 'LABAREDA' or nome == 'LANÇA-CHAMAS' or nome == 'CÍRCULO DE FOGO':
        ret = 6
    if nome == 'GARRAS DE DRAGÃO':
        ret = 7
    if nome == 'RAIO' or nome == 'CHOQUE DO TROVÃO' or nome == 'INVESTIDA RELÂMPAGO' or nome == 'ESFERA DE RAIOS' or nome == 'INVESTIDA TROVÃO' or nome == 'MORDIDA RELÂMPAGO' or nome == 'TROVÃO SELVAGEM':
        ret = 9
    if nome == 'GARRA DE METAL':
        ret = 10
    if nome == 'ASSOMBRAR' or nome == 'PESADELO' or nome == 'ESFERA NEGRA':
        ret = 11
    if nome == 'ESFERA DE ENERGIA' or nome == 'CONFUSÃO' or nome == 'GOLPE PSIQUÍCO':
        ret = 12
    if nome == 'BOLHA VENENOSA':
        ret = 13
    if nome == 'INVESTIDA AÉREA' or nome == 'GOLPE AÉREO' or nome == 'QUEDA LIVRE' or nome == 'BICADA':
        ret = 14
    if nome == 'DESABAMENTO':
        ret = 15
    return typeboxes[ret]

def get_type_txt(nome):
    if nome == 'RAIO SOLAR' or nome == 'FOLHA NAVALHA' or nome == 'ABSORVER':
        ret = 'GRAMA'
    if nome == 'ARRANHAR' or nome == 'HIPER RAIO' or nome == 'MORDIDA' or nome == 'ATAQUE RÁPIDO' or nome == 'CABEÇADA' or nome == 'INVESTIDA' or nome == 'GOLPE ESTRELADO':
        ret = 'NORMAL'
    if nome == 'TERREMOTO':
        ret = 'TERRA'
    if nome == 'GOLPE KARATE' or nome == 'GOLPE BAIXO' or nome == 'CORTE CRUZADO':
        ret = 'LUTADOR'
    if nome == 'JATO D\'ÁGUA' or nome == 'BOLHAS':
        ret = 'ÁGUA'
    if nome == 'MORDIDA GLACIAL' or nome == 'RAIO DE GELO' or nome == 'NEVASCA':
        ret = 'GELO'
    if nome == 'DEVORADOR DE SONHOS' or nome == 'ATORMENTAR':
        ret = 'FANTASMA'
    if nome == 'SOCO DE FOGO' or nome == 'INFERNO' or nome == 'LABAREDA' or nome == 'LANÇA-CHAMAS' or nome == 'CÍRCULO DE FOGO':
        ret = 'FOGO'
    if nome == 'GARRAS DE DRAGÃO':
        ret = 'DRAGÃO'
    if nome == 'RAIO' or nome == 'CHOQUE DO TROVÃO' or nome == 'INVESTIDA RELÂMPAGO' or nome == 'ESFERA DE RAIOS' or nome == 'INVESTIDA TROVÃO' or nome == 'MORDIDA RELÂMPAGO' or nome == 'TROVÃO SELVAGEM':
        ret = 'ELÉTRICO'
    if nome == 'GARRA DE METAL':
        ret = 'AÇO'
    if nome == 'ASSOMBRAR' or nome == 'PESADELO' or nome == 'ESFERA NEGRA':
        ret = 'TREVAS'
    if nome == 'ESFERA DE ENERGIA' or nome == 'CONFUSÃO' or nome == 'GOLPE PSIQUÍCO':
        ret = 'PSIQUÍCO'
    if nome == 'BOLHA VENENOSA':
        ret = 'VENENO'
    if nome == 'INVESTIDA AÉREA' or nome == 'GOLPE AÉREO' or nome == 'QUEDA LIVRE' or nome == 'BICADA':
        ret = 'AÉREO'
    if nome == 'DESABAMENTO':
        ret = 'PEDRA'
    return ret

def efetividade(tipoa, tipo1i, tipo21, teste):
    x = multiplicador(tipoa, tipo1i, tipo21, teste)
    if x == 1:
        m = '      EFETIVO'
    elif x>= 2:
        m = 'SUPER EFETIVO'
    elif x == 0.5:
        m = 'POUCO EFETIVO'
    elif x == 0:
        m = '   SEM EFEITO'
    return m
def centralizar(texto):
    while len(texto) < 19:
        texto = ' ' + texto + ' '
    return texto

typeboxes = []

def carregar_sprites():
    global walkdown, walkleft, walkright, walkup, rundown, runleft, runright, runup, playerg, APP_FOLDER, launchpkb, typeboxes
    os.chdir(APP_FOLDER + '/Sprites')
    for i in range(1, 3):
        runup.append(pygame.image.load('Run_Up_0_{}.png'.format(playerg)))
        runup.append(pygame.image.load('Run_Up_{}_{}.png'.format(i, playerg)))
        runleft.append(pygame.image.load('Run_Left_0_{}.png'.format(playerg)))
        runleft.append(pygame.image.load('Run_Left_{}_{}.png'.format(i, playerg)))
        rundown.append(pygame.image.load('Run_Down_0_{}.png'.format(playerg)))
        rundown.append(pygame.image.load('Run_Down_{}_{}.png'.format(i, playerg)))
        runright.append(pygame.image.load('Run_Right_0_{}.png'.format(playerg)))
        runright.append(pygame.image.load('Run_Right_{}_{}.png'.format(i, playerg)))
    for i in range(1, 3):
        walkup.append(pygame.image.load('Looking_Up_{}.png'.format(playerg)))
        walkup.append(pygame.image.load('Walking_Up_{}_{}.png'.format(i, playerg)))
        walkleft.append(pygame.image.load('Looking_Left_{}.png'.format(playerg)))
        walkleft.append(pygame.image.load('Walking_Left_{}_{}.png'.format(i, playerg)))
        walkdown.append(pygame.image.load('Looking_Down_{}.png'.format(playerg)))
        walkdown.append(pygame.image.load('Walking_Down_{}_{}.png'.format(i, playerg)))
        walkright.append(pygame.image.load('Looking_Right_{}.png'.format(playerg)))
        walkright.append(pygame.image.load('Walking_Right_{}_{}.png'.format(i, playerg)))
    for i in range(1, 6):
        launchpkb.append(pygame.image.load('pk{}{}.png'.format(i, playerg)))
    for i in range(1, 17):
        typeboxes.append(pygame.image.load('type_box{}.png'.format(i)))
    os.chdir(APP_FOLDER)

principal_fundo = pygame.image.load('principalfundo.png')
estado = "jogo"
pygame.mixer.music.play()
feandar = 0


idbatalha = 0

def blit_personagem():
    global feandar, clock, display, walkdown
    feandar += 1
    feandar %= 4
    posm = posx, posy = pygame.mouse.get_pos()
    player = walkdown[feandar]
    player = pygame.transform.scale(player, (68, 68))
    display.blit(player, (91, 57))

def atacar(ataque):
    global meutime, pkmn_luciana, pkmn_astro, pkmn_clara, pkmn_ale, playername, estado
    if luta == 'astro':
        m = multiplicador(ataque, pkmn_astro[0][3], pkmn_astro[0][4] ,False)
        pkmn_astro[0][6] -= 50*m
    if luta == 'ale':
        m = multiplicador(ataque, pkmn_ale[0][3], pkmn_ale[0][4] ,False)
        pkmn_ale[0][6] -= 50*m
    if luta == 'clara':
        m = multiplicador(ataque, pkmn_clara[0][3], pkmn_clara[0][4] ,False)
        pkmn_clara[0][6] -= 50*m
    if luta == 'luciana':
        m = multiplicador(ataque, pkmn_luciana[0][3], pkmn_luciana[0][4] ,False)
        pkmn_luciana[0][6] -= 50*m
    estado = 'selbatalha'
def blit_ataques(ataque):
    a = get_type(ataque)
    a = pygame.transform.scale(a, (int(124*1.5), int(55*1.5)))
    return a
def get_enemy2():
    global luta, astro, ale, luciana, clara
    if luta == 'astro':
        return astro
    if luta == 'ale':
        return ale
    if luta == 'clara':
        return clara
    if luta == 'luciana':
        return luciana
def get_enemy():
    global pkmn_astro, pkmn_clara, luta, pkmn_luciana, pkmn_ale
    if luta == 'astro':
        return pkmn_astro
    if luta == 'ale':
        return pkmn_ale
    if luta == 'clara':
        return pkmn_clara
    if luta == 'luciana':
        return pkmn_luciana
def verifica_pokemon():
    global pkmn_ale, pkmn_luciana, pkmn_clara, pkmn_astro, meutime, estado, telaprincipal, inimigos_derrotados, APP_FOLDER, playername, spritestimen
    global atualaliado, mainloop2, clock
    if atualaliado[6] <= 0:
        mostrar_texto('{} foi derrotado.'.format(meutime[0][2]))
        clock.tick(7)
        mostrar_texto('{}: Essa não!'.format(playername))
        if len(meutime) >= 2:
            mostrar_texto('{}: Vai {}'.format(playername, meutime[1][2]))
        else:
            mostrar_texto('{}: Droga, perdi!'.format(playername))
        del meutime[0]
        del spritestimen[0]
    if len(meutime) <= 0:
        mainloop2 = False
    if luta == 'astro':
        if pkmn_astro[0][6] <= 0:
            if len(pkmn_astro) > 1:
                mostrar_texto('Astro: Essa não! {} volte'.format(pkmn_astro[0][2]))
                if len(pkmn_astro) >= 2:
                    mostrar_texto('Astro: Acabe com ele {}!'.format(pkmn_astro[1][2]))
                del pkmn_astro[0]
            else:
                mostrar_texto('Astro: DROGA! Você pode passar!')
                clock.tick(8)
                mostrar_texto('Astro: Mas não ache que vai chegar longe!')
                estado = 'jogo'
                del telaprincipal[2]
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                inimigos_derrotados += 1
    if luta == 'ale':
        if pkmn_ale[0][6] <= 0:
            if len(pkmn_ale) > 1:
                mostrar_texto('Ale: Essa não! {} volte.'.format(pkmn_ale[0][2], pkmn_ale[1][2]))
                clock.tick(10)
                if len(pkmn_ale) >= 2:
                    mostrar_texto('Ale: Acabe com ele {}!'.format(pkmn_ale[1][2]))
                del pkmn_ale[0]
            else:
                mostrar_texto('Ale: Você não vai chegar muito longe')
                estado = 'jogo'
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                del telaprincipal[2]
                inimigos_derrotados += 1
    if luta == 'clara':
        if pkmn_clara[0][6] <= 0:
            if len(pkmn_clara) > 1:
                mostrar_texto('Clara: Essa não! {} volte, acaba com ele {}! Eu preciso passar!'.format(pkmn_clara[0][2], pkmn_clara[1][2]))
                del pkmn_clara[0]
            else:
                mostrar_texto('Clara: DROGA! Você pode passar, mas não ache que vai chegar no fim!')
                estado = 'jogo'
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                del telaprincipal[2]
                inimigos_derrotados += 1
    if luta == 'luciana':
        if pkmn_luciana[0][6] <= 0:
            if len(pkmn_luciana) > 1:
                mostrar_texto('Luciana: Essa não! {} volte, acaba com ele {}! Eu preciso passar!'.format(pkmn_luciana[0][2], pkmn_luciana[1][2]))
                del pkmn_luciana[0]
            else:
                mostrar_texto('Luciana: DROGA! Você pode passar, mas não ache que vai chegar no fim!')
                estado = 'jogo'
                os.chdir(APP_FOLDER + '/Sons')
                pygame.mixer.music.load('main_music.mp3')
                pygame.init()
                pygame.mixer.music.play()
                os.chdir(APP_FOLDER)
                del telaprincipal[2]
                inimigos_derrotados += 1

def ataque_inimigo():
    global pkmn_astro, pkmn_luciana, pkmn_clara, pkmn_ale, meutime, atualaliado
    x = random.randrange(0,4)
    if inimigos_derrotados == 0:
        c = pkmn_astro[0][5][x]
        mostrar_texto('{} usou {}'.format(pkmn_astro[0][2], pkmn_astro[0][5][x]))
        c = multiplicador(c, atualaliado[0][3], atualaliado[0][4], False)
        atualaliado[6] -= 50 * c
    if inimigos_derrotados == 1:
        c = pkmn_ale[0][5][x]
        mostrar_texto('{} usou {}'.format(pkmn_ale[0][2], pkmn_ale[0][5][x]))
        c = multiplicador(c, meutime[0][3], meutime[0][4], False)
        atualaliado[6] -= 50 * c
    if inimigos_derrotados == 2:
        c = pkmn_clara[0][5][x]
        mostrar_texto('{} usou {}'.format(pkmn_clara[0][2], pkmn_clara[0][5][x]))
        c = multiplicador(c, meutime[0][3], meutime[0][4], False)
        atualaliado[6] -= 50 * c
    if inimigos_derrotados == 3:
        c = pkmn_luciana[0][5][x]
        mostrar_texto('{} usou {}'.format(pkmn_luciana[0][2], pkmn_luciana[0][5][x]))
        c = multiplicador(c, meutime[0][3], meutime[0][4], False)
        atualaliado[6] -= 50 * c

def get_hp_bar(tipo):
    global meutime, pkmn_ale, pkmn_astro, pkmn_clara, pkmn_luciana, hpa, luta
    if tipo == 'aliado':
        x = int((meutime[0][6] / meutime[0][7]) * 100)
    else:
        if luta == 'astro':
            x = int((pkmn_astro[0][6] / pkmn_astro[0][7]) * 100)
        if luta == 'ale':
            x = int((pkmn_ale[0][6] / pkmn_ale[0][7]) * 100)
        if luta == 'clara':
            x = int((pkmn_clara[0][6] / pkmn_clara[0][7]) * 100)
        if luta == 'luciana':
            x = int((pkmn_luciana[0][6] / pkmn_luciana[0][7]) * 100)
    if x > 70:
        hpa = pygame.transform.scale(hp[0], (int(x * 0.84), 11))
    if x <= 70:
        hpa = pygame.transform.scale(hp[1], (int(x * 0.84), 11))
    if x <= 30:
        hpa = pygame.transform.scale(hp[2], (int(x * 0.84), 11))
    if x <= 0:
        hpa = pygame.transform.scale(hp[2], (0, 11))
    return hpa
clock = pygame.time.Clock()
feandar = 0
hpa = pygame.transform.scale(hp[0], (84, 11))
playerg = ''
escolheu_nome = False
escolheu_personagem = False
while escolheu_personagem == False:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    display.blit(fundo, (0, 0))  # Mostrar o fundoq
    escolher_personagem_1()
    pygame.display.flip()
carregar_sprites()

while escolheu_nome == False:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_RETURN]:
        escolheu_nome = True
    display.blit(tela_nome, (0,0))
    escolhernome()
    blit_personagem()
    blit_nome()

id = 0

while len(meutime) != 6:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    escolher_time()
    blit_time()
    pygame.display.flip()

escolheu_time = False
permitido_andar = True
id = 0
luta = 'astro'
os.chdir(APP_FOLDER + '/pkmns')
spritestimen = []
spritestimew = []
for i in range(6):
    auxa = pygame.image.load(meutime[i][1])
    auxa = pygame.transform.scale(auxa, (82*5, 82*5))
    spritestimew.append(x)
    auxa = pygame.image.load(meutime[i][0])
    auxa = pygame.transform.scale(auxa, (82*5, 82*5))
    spritestimen.append(pygame.image.load(meutime[i][0]))
os.chdir(APP_FOLDER)
y = 800
mainloop2 = True
x = 400
telaprincipal = [[principal_fundo, (0, 0)], [player, (x, y)], [astro[3], (astro[1], astro[2])],
                 [ale[3], (ale[1], ale[2])],
                 [clara[3], (clara[1], clara[2])], [luciana[3], (luciana[1], luciana[2])]]
while mainloop2:
    telaprincipal[1] = [player, (x, y)]
    posm = posx, posy = pygame.mouse.get_pos()
    telabatalha = [[fundo_batalha, (0,0)], [tela_ataque, (0,0)], [barra_aliado, (596, 302)], [barra_inimigo, (0, 54)],
                   [base_aliada, (3, 354)], [base_inimiga, (495, 134)], [get_hp_bar('aliado'), (700, 335)],
                   [selecionaicon, blit_seleciona()], [get_hp_bar(''), (84, 94)],
                   [pygame.transform.scale2x(spritestimen[0]), (146, 238)],[pygame.transform.scale2x(get_enemy()[0][0]), (564, 20)],
                   [font2.render(str(meutime[0][2]), True, [0, 0, 0]), (714, 313)],[font2.render(str(get_enemy()[0][2]), True, [0,0,0]), (93, 71)],
                   [pygame.transform.scale2x(get_enemy()[0][0]), (564, 20)],
                   [font2.render(str(meutime[0][6]), True, [0,0,0]), (721, 345)],
                   [font2.render(str(meutime[0][7]), True, [0,0,0]), (756, 345)]]
    keys = pygame.key.get_pressed()
    display.fill((0,0,0))
    display.blit(principal_fundo, (0, 0))  # Mostrar o fundo
    if len(meutime) == 0:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    if permitido_andar: andar()
    if estado == 'jogo':
        permitido_andar = True
        em_npc()
        telaatual = telaprincipal
    elif estado == 'prepara':
        andarnpc(luta)
        telaatual = telaprincipal
    elif estado == 'batalhaini':
        os.chdir(APP_FOLDER + '/Sons')
        pygame.mixer.music.load('batalha.mp3')
        pygame.init()
        pygame.mixer.music.play()
        os.chdir(APP_FOLDER)
        estado = 'selbatalha'
        animatransição(get_enemy2()[6])
        animainimigo(get_enemy2())
    elif estado == 'selbatalha':
        tela_ataque = pygame.image.load('tela ataque.png')
        telaatual = telabatalha
        selprincipal()
    elif estado == 'selataque':
        if keys[pygame.K_ESCAPE]:
            estado = 'selbatalha'
        pkmni_atual = get_enemy()
        tela_ataque = pygame.image.load('tela_sel.png')
        efetividadetxt = efetividade(meutime[0][5][idbatalha], pkmni_atual[0][3], pkmni_atual[0][4], False)
        efetividadetxt = font.render(efetividadetxt, True, [0, 0, 0])
        telaescolha = [[fundo_batalha, (0, 0)], [tela_ataque, (0, 0)], [barra_aliado, (596, 302)],
                       [barra_inimigo, (0, 54)], [base_aliada, (3, 354)], [base_inimiga, (495, 134)],
                       [get_hp_bar('aliado'), (700, 335)],
                       [blit_ataques(meutime[0][5][0]), (25, 412)],
                       [font2.render(centralizar(meutime[0][5][0]), True, [0, 0, 0]), (71, 434)],
                       [blit_ataques(meutime[0][5][1]), (264, 411)],
                       [font2.render(centralizar(meutime[0][5][1]), True, [0, 0, 0]), (308, 434)],
                       [blit_ataques(meutime[0][5][2]), (25, 502)],
                       [font2.render((centralizar(meutime[0][5][2])), True, [0, 0, 0]), (73, 529)],
                       [blit_ataques(meutime[0][5][3]), (264, 502)],
                       [font2.render(centralizar(meutime[0][5][3]), True, [0, 0, 0]), (308, 529)],
                       [selecionaicon, blit_seleciona()], [efetividadetxt, (592, 404)],
                       [pygame.transform.scale2x(get_enemy()[0][0]), (564, 20)],
                       [font2.render(str(meutime[0][6]), True, [0,0,0]), (721, 345)],
                       [font2.render(str(meutime[0][7]), True, [0,0,0]), (756, 345)],
                       [font2.render(str(meutime[0][2]), True, [0, 0, 0]), (714, 313)],
                       [pygame.transform.scale2x(spritestimen[0]), (146, 238)], [get_hp_bar(''), (84, 94)],
                       [font2.render(str(get_enemy()[0][2]), True, [0,0,0]), (93, 71)]]
        atualaliado = meutime[0]
        telaatual = telaescolha
        escolher_ataque()
        blit_seleciona()
        verifica_pokemon()
    elif estado == 'selpkmn':
        telaatual = change_pokemon()
        change_pokemon_2()
    elif estado == 'ataqueinimigo':
        ataque_inimigo()
        estado = 'selbatalha'
    for i in telaatual:
        display.blit(i[0], i[1])
    pygame.display.flip()

