import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


# Función para dibujar la pelota
def draw_ball(ball_pos):
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)


# Función para dibujar las paletas
def draw_paddle(paddle_pos):
    pygame.draw.rect(screen, WHITE, pygame.Rect(paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))


# Función principal del juego
def main():
    # Inicializar variables
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [4, -4]

    paddle1_pos = [20, HEIGHT // 2 - PADDLE_HEIGHT // 2]
    paddle2_pos = [WIDTH - PADDLE_WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2]

    paddle1_vel = 0
    paddle2_vel = 0

    clock = pygame.time.Clock()

    while True:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_vel = -8
                elif event.key == pygame.K_s:
                    paddle1_vel = 8
                elif event.key == pygame.K_UP:
                    paddle2_vel = -8
                elif event.key == pygame.K_DOWN:
                    paddle2_vel = 8
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle1_vel = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle2_vel = 0

        # Actualizar posiciones
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        paddle1_pos[1] += paddle1_vel
        paddle2_pos[1] += paddle2_vel

        # Rebote de la pelota en los bordes
        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]

        # Rebote de la pelota en las paletas
        if (ball_pos[0] <= PADDLE_WIDTH + BALL_RADIUS and
                paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + PADDLE_HEIGHT):
            ball_vel[0] = -ball_vel[0]

        if (ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and
                paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + PADDLE_HEIGHT):
            ball_vel[0] = -ball_vel[0]

        # Limitar el movimiento de las paletas
        if paddle1_pos[1] < 0:
            paddle1_pos[1] = 0
        elif paddle1_pos[1] > HEIGHT - PADDLE_HEIGHT:
            paddle1_pos[1] = HEIGHT - PADDLE_HEIGHT

        if paddle2_pos[1] < 0:
            paddle2_pos[1] = 0
        elif paddle2_pos[1] > HEIGHT - PADDLE_HEIGHT:
            paddle2_pos[1] = HEIGHT - PADDLE_HEIGHT

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar elementos
        draw_ball(ball_pos)
        draw_paddle(paddle1_pos)
        draw_paddle(paddle2_pos)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar los FPS
        clock.tick(FPS)


if __name__ == "__main__":
    main()
