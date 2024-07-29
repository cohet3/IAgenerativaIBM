# game_objects.py
import pygame
from constants import *


class Ball:
    def __init__(self):
        self.pos = [WIDTH // 2, HEIGHT // 2]
        self.vel = [BALL_VEL_X, BALL_VEL_Y]

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, BALL_RADIUS)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # Rebote en los bordes superior e inferior
        if self.pos[1] <= BALL_RADIUS or self.pos[1] >= HEIGHT - BALL_RADIUS:
            self.vel[1] = -self.vel[1]

    def reset(self):
        self.pos = [WIDTH // 2, HEIGHT // 2]
        self.vel = [BALL_VEL_X, BALL_VEL_Y]


class Paddle:
    def __init__(self, x_pos):
        self.rect = pygame.Rect(x_pos, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.vel = 0

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    def update(self):
        self.rect.y += self.vel

        # Limitar el movimiento de las paletas
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def set_velocity(self, vel):
        self.vel = vel


class Score:
    def __init__(self):
        self.player_score = 0
        self.ai_score = 0

    def draw(self, screen):
        font = pygame.font.Font(None, 74)
        player_text = font.render(str(self.player_score), True, WHITE)
        ai_text = font.render(str(self.ai_score), True, WHITE)

        screen.blit(player_text, (WIDTH // 4, 20))
        screen.blit(ai_text, (3 * WIDTH // 4 - ai_text.get_width(), 20))

    def player_point(self):
        self.player_score += 1

    def ai_point(self):
        self.ai_score += 1
