import pygame  
import random  
import time  

pygame.init()  

# Game variables  
WIDTH, HEIGHT = 500, 500  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Snake Game")  

# Snake  
snake = [(100, 100), (90, 100), (80, 100)]  
direction = "RIGHT"  

# Food  
food_x = random.randint(0, WIDTH // 10) * 10  
food_y = random.randint(0, HEIGHT // 10) * 10  

running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP and direction != "DOWN":  
                direction = "UP"  
            elif event.key == pygame.K_DOWN and direction != "UP":  
                direction = "DOWN"  
            elif event.key == pygame.K_LEFT and direction != "RIGHT":  
                direction = "LEFT"  
            elif event.key == pygame.K_RIGHT and direction != "LEFT":  
                direction = "RIGHT"  

    # Move the snake  
    x, y = snake[0]  
    if direction == "UP":  
        y -= 10  
    elif direction == "DOWN":  
        y += 10  
    elif direction == "LEFT":  
        x -= 10  
    elif direction == "RIGHT":  
        x += 10  

    snake.insert(0, (x, y))  
    if (x, y) == (food_x, food_y):  
        food_x = random.randint(0, WIDTH // 10) * 10  
        food_y = random.randint(0, HEIGHT // 10) * 10  
    else:  
        snake.pop()  

    # Check collisions  
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or snake[0] in snake[1:]:  
        running = False  

    # Draw everything  
    screen.fill((0, 0, 0))  
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 10, 10))  
    for block in snake:  
        pygame.draw.rect(screen, (0, 255, 0), (*block, 10, 10))  

    pygame.display.update()  
    time.sleep(0.1)  

pygame.quit()  
