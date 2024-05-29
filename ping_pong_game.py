import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle settings
paddle_width = 10
paddle_height = 100
paddle_speed = 10

# Ball settings
ball_size = 10
ball_speed_x = 5
ball_speed_y = 5

# Paddle positions
player1_x = 50
player1_y = screen_height // 2 - paddle_height // 2

player2_x = screen_width - 50 - paddle_width
player2_y = screen_height // 2 - paddle_height // 2

# Ball position
ball_x = screen_width // 2
ball_y = screen_height // 2

# Scores
player1_score = 0
player2_score = 0

# Font settings
font = pygame.font.SysFont(None, 55)

def draw_paddle(x, y):
    pygame.draw.rect(screen, white, [x, y, paddle_width, paddle_height])

def draw_ball(x, y):
    pygame.draw.rect(screen, white, [x, y, ball_size, ball_size])

def show_score(player1_score, player2_score):
    score = font.render(f"{player1_score} : {player2_score}", True, white)
    screen.blit(score, [screen_width // 2 - score.get_width() // 2, 20])

def game_loop():
    global player1_y, player2_y, ball_x, ball_y, ball_speed_x, ball_speed_y, player1_score, player2_score

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= paddle_speed
        if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
            player1_y += paddle_speed
        if keys[pygame.K_UP] and player2_y > 0:
            player2_y -= paddle_speed
        if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
            player2_y += paddle_speed

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0 or ball_y >= screen_height - ball_size:
            ball_speed_y *= -1

        if ball_x <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height:
            ball_speed_x *= -1
        elif ball_x >= player2_x - ball_size and player2_y < ball_y < player2_y + paddle_height:
            ball_speed_x *= -1

        if ball_x <= 0:
            player2_score += 1
            ball_x, ball_y = screen_width // 2, screen_height // 2
            ball_speed_x *= random.choice([1, -1])
            ball_speed_y *= random.choice([1, -1])

        if ball_x >= screen_width - ball_size:
            player1_score += 1
            ball_x, ball_y = screen_width // 2, screen_height // 2
            ball_speed_x *= random.choice([1, -1])
            ball_speed_y *= random.choice([1, -1])

        screen.fill(black)
        draw_paddle(player1_x, player1_y)
        draw_paddle(player2_x, player2_y)
        draw_ball(ball_x, ball_y)
        show_score(player1_score, player2_score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
