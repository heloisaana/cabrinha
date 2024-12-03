import pygame
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Definindo o tamanho da tela
WIDTH = 600
HEIGHT = 400
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o relógio para controle de FPS
clock = pygame.time.Clock()

# Definindo o tamanho do bloco da cobrinha
SNAKE_BLOCK = 10
SNAKE_SPEED = 15  # A velocidade da cobra (inicial)

# Fonte para o texto
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Função para desenhar a cobrinha
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(DISPLAYSURF, GREEN, [x[0], x[1], snake_block, snake_block])

# Função para mostrar o placar
def Your_score(score):
    value = score_font.render("Pontuação: " + str(score), True, BLACK)
    DISPLAYSURF.blit(value, [0, 0])

# Função para exibir a mensagem de fim de jogo
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DISPLAYSURF.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Função para exibir a fase atual
def show_level(level):
    level_text = font_style.render("Fase: " + str(level), True, BLACK)
    DISPLAYSURF.blit(level_text, [WIDTH - 100, 0])

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    # Posições iniciais da cobrinha
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    # Lista para armazenar o corpo da cobra
    snake_List = []
    Length_of_snake = 1

    # Posições iniciais da comida
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    # Definir o nível e a meta de comida para passar de fase
    level = 1
    food_to_advance = 5

    while not game_over:

        while game_close:
            DISPLAYSURF.fill(BLUE)
            message("Você Perdeu! Pressione Q para sair ou C para jogar novamente", RED)
            Your_score(Length_of_snake - 1)
            show_level(level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Verificando se a cobra colidiu com as paredes
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DISPLAYSURF.fill(BLUE)

        # Desenhando a comida
        pygame.draw.rect(DISPLAYSURF, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Atualizando a lista da cobrinha
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Verificando colisões com o próprio corpo
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        Your_score(Length_of_snake - 1)
        show_level(level)

        pygame.display.update()

        # Comida comida pela cobrinha
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

            # Verificar se a cobra comeu comida suficiente para avançar de fase
            if (Length_of_snake - 1) >= food_to_advance:
                level += 1
                SNAKE_SPEED += 2  # Aumenta a velocidade da cobra
                food_to_advance += 5  # Aumenta a quantidade de comida necessária para avançar para o próximo nível

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Rodando o jogo
gameLoop()
