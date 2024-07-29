# main.py
import pygame
import sys
from constants import *
from game_objects import Ball, Paddle, Score


def main():
    # Inicializar Pygame
    pygame.init()

    # Configuración de la pantalla
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    # Crear objetos del juego
    ball = Ball()
    player_paddle = Paddle(20)  # Paleta del jugador
    ai_paddle = Paddle(WIDTH - PADDLE_WIDTH - 20)  # Paleta de la IA
    score = Score()

    clock = pygame.time.Clock()

    while True:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Manejar controles del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_paddle.set_velocity(-PADDLE_VEL)
        elif keys[pygame.K_DOWN]:
            player_paddle.set_velocity(PADDLE_VEL)
        else:
            player_paddle.set_velocity(0)

        # Movimiento de la paleta de la IA
        if ai_paddle.rect.centery < ball.pos[1]:
            ai_paddle.set_velocity(PADDLE_VEL)
        elif ai_paddle.rect.centery > ball.pos[1]:
            ai_paddle.set_velocity(-PADDLE_VEL)
        else:
            ai_paddle.set_velocity(0)

        # Actualizar objetos
        ball.update()
        player_paddle.update()
        ai_paddle.update()

        # Comprobar colisiones con las paletas
        if (ball.pos[0] <= PADDLE_WIDTH + BALL_RADIUS and
                player_paddle.rect.top < ball.pos[1] < player_paddle.rect.bottom):
            ball.vel[0] = -ball.vel[0]

        if (ball.pos[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and
                ai_paddle.rect.top < ball.pos[1] < ai_paddle.rect.bottom):
            ball.vel[0] = -ball.vel[0]

        # Comprobar si la pelota se sale de los límites
        if ball.pos[0] < BALL_RADIUS:
            score.ai_point()
            ball.reset()
            player_paddle.rect.centery = HEIGHT // 2 - PADDLE_HEIGHT // 2
            ai_paddle.rect.centery = HEIGHT // 2 - PADDLE_HEIGHT // 2

        if ball.pos[0] > WIDTH - BALL_RADIUS:
            score.player_point()
            ball.reset()
            player_paddle.rect.centery = HEIGHT // 2 - PADDLE_HEIGHT // 2
            ai_paddle.rect.centery = HEIGHT // 2 - PADDLE_HEIGHT // 2

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar objetos
        ball.draw(screen)
        player_paddle.draw(screen)
        ai_paddle.draw(screen)
        score.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar los FPS
        clock.tick(FPS)


if __name__ == "__main__":
    main()

# hazme un ejemplo de videojuego PONG utilizando el módulo de PyGame, donde juegues contra una IA muy simple utilizando la
# flechas arriba y abajo del teclado, y que tenga un marcador de puntos en la parte superior donde se sumen los puntos para el jugador
# o la IA de pendiendo de quien gane cada ronda. Hazlo utilizando programación orientada a objetos separando cada clase en un propio fichero,
# las constantes y el proceso principal también en sus propio fichero, las constantes y el proceso principal también en sus propios ficheros,
# Todo debe estar documentado y programado siguiendo buenas práticas.
