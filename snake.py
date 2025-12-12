import pygame
import random

# Настройки окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Snake:
    def __init__(self):
        self.positions = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'RIGHT'
    
    def draw(self, screen):
        for position in self.positions:
            rect = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
    
    def move(self):
        head_x, head_y = self.positions[0]
        
        if self.direction == 'UP':
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + CELL_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head_x - CELL_SIZE, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + CELL_SIZE, head_y)
        
        self.positions.insert(0, new_head)
        self.positions.pop()
    
    def grow(self):
        last_pos = self.positions[-1]
        x, y = last_pos
        if self.direction == 'UP':
            self.positions.append((x, y + CELL_SIZE))
        elif self.direction == 'DOWN':
            self.positions.append((x, y - CELL_SIZE))
        elif self.direction == 'LEFT':
            self.positions.append((x + CELL_SIZE, y))
        elif self.direction == 'RIGHT':
            self.positions.append((x - CELL_SIZE, y))
    
    def collide_with_self(self):
        head_x, head_y = self.positions[0]
        return (head_x, head_y) in self.positions[1:]

class Food:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE
        self.y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE
    
    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

def main():
    # Инициализация Pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')

    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'

        # Движение змеи
        snake.move()

        # Проверка столкновения со своим телом
        if snake.collide_with_self():
            running = False

        # Проверка поедания еды
        head_x, head_y = snake.positions[0]
        if head_x == food.x and head_y == food.y:
            snake.grow()
            food = Food()

        # Очистка экрана
        screen.fill(BLACK)

        # Отображение объектов
        snake.draw(screen)
        food.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
    input()