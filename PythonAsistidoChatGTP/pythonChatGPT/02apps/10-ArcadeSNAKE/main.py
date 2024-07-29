# main.py

import pygame
import sys
from constants import *
from game_objects import Snake, Food, Score


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    def reset_game(snake, food, score):
        return Snake(), Food(), score

    snake, food, score = Snake(), Food(), Score()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.change_direction((0, -GRID_SIZE))
        elif keys[pygame.K_DOWN]:
            snake.change_direction((0, GRID_SIZE))
        elif keys[pygame.K_LEFT]:
            snake.change_direction((-GRID_SIZE, 0))
        elif keys[pygame.K_RIGHT]:
            snake.change_direction((GRID_SIZE, 0))

        snake.update()

        if snake.check_collision():
            score.lose_life()
            if score.lives <= 0:
                pygame.quit()
                sys.exit()
            else:
                snake, food, score = reset_game(snake, food, score)

        if snake.body[0] == food.position:
            snake.grow_snake()
            score.increase()
            food.randomize_position()

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), 2)
        snake.draw(screen)
        food.draw(screen)
        score.draw(screen)
        pygame.display.flip()

        clock.tick(SNAKE_SPEED)


if __name__ == "__main__":
    main()
