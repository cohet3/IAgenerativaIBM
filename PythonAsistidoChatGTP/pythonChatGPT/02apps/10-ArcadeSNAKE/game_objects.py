# game_objects.py

import pygame
import random
from constants import *


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -GRID_SIZE)
        self.grow = False

    def update(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]
        if self.grow:
            self.body.append(self.body[-1])
            self.grow = False

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] and
                new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (*segment, GRID_SIZE, GRID_SIZE))

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        return False


class Food:
    def __init__(self):
        self.position = (random.randrange(0, WIDTH, GRID_SIZE),
                         random.randrange(0, HEIGHT, GRID_SIZE))

    def randomize_position(self):
        self.position = (random.randrange(0, WIDTH, GRID_SIZE),
                         random.randrange(0, HEIGHT, GRID_SIZE))

    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, (*self.position, GRID_SIZE, GRID_SIZE))


class Score:
    def __init__(self):
        self.score = 0
        self.lives = INITIAL_LIVES

    def increase(self):
        self.score += 1

    def lose_life(self):
        self.lives -= 1

    def draw(self, screen):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        lives_text = font.render(f"Lives: {self.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))
