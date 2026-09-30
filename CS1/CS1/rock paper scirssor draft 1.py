import pygame
import sys
import math

pygame.init()

# Window
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cool Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 12, 120
PADDLE_SPEED = 0.5       # acceleration
PADDLE_MAX_SPEED = 7

# Ball
BALL_SIZE = 16
BALL_SPEED = 6
BALL_ACCEL = 1.05     # speed increases per paddle hit
BALL_MAX_SPEED = 18

# Rects
left_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2,
                          PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH,
                           HEIGHT//2 - PADDLE_HEIGHT//2,
                           PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE, BALL_SIZE)

# Ball motion
angle = math.radians(0)
vel_x = BALL_SPEED
vel_y = BALL_SPEED / 2

# Paddle Velocities
left_vel = 0
right_vel = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 40)

left_score = 0
right_score = 0

# For trail effect
ball_trail = []


def reset_ball():
    global vel_x, vel_y, BALL_SPEED, angle, ball_trail
    ball.center = (WIDTH//2, HEIGHT//2)
    BALL_SPEED = 6
    angle = math.radians(0)
    vel_x = BALL_SPEED * (1 if pygame.time.get_ticks() % 2 == 0 else -1)
    vel_y = BALL_SPEED / 2
    ball_trail = []


def update_ball():
    global vel_x, vel_y, BALL_SPEED, left_score, right_score

    # Move Ball
    ball.x += vel_x
    ball.y += vel_y

    # Walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        vel_y *= -1

    # Paddle Collision
    if ball.colliderect(left_paddle) and vel_x < 0:
        hit_offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)
        vel_y = hit_offset * BALL_SPEED
        vel_x = abs(vel_x)

        # Increase speed
        BALL_SPEED = min(BALL_SPEED * BALL_ACCEL, BALL_MAX_SPEED)
        vel_x = BALL_SPEED * (vel_x / abs(vel_x))
    if ball.colliderect(right_paddle) and vel_x > 0:
        hit_offset = (ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2)
        vel_y = hit_offset * BALL_SPEED
        vel_x = -abs(vel_x)

        BALL_SPEED = min(BALL_SPEED * BALL_ACCEL, BALL_MAX_SPEED)
        vel_x = BALL_SPEED * (vel_x / abs(vel_x))

    # Scoring
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

    # Add to trail
    ball_trail.append((ball.centerx, ball.centery))
    if len(ball_trail) > 15:
        ball_trail.pop(0)


def draw():
    WIN.fill((0, 0, 0))

    # Middle line
    pygame.draw.aaline(WIN, (70, 70, 70), (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Ball trail (cool glowing effect)
    for i, pos in enumerate(ball_trail):
        alpha = int(255 * (i / len(ball_trail)))
        glow = pygame.Surface((BALL_SIZE*2, BALL_SIZE*2), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 255, 255, alpha),
                           (BALL_SIZE, BALL_SIZE), BALL_SIZE)
        WIN.blit(glow, (pos[0] - BALL_SIZE, pos[1] - BALL_SIZE))

    # Ball
    pygame.draw.ellipse(WIN, WHITE, ball)

    # Paddles
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)

    # Score
    ltxt = font.render(str(left_score), True, WHITE)
    rtxt = font.render(str(right_score), True, WHITE)
    WIN.blit(ltxt, (WIDTH//4, 20))
    WIN.blit(rtxt, (WIDTH*3//4, 20))

    pygame.display.update()


# Game Loop
while True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Left paddle
    if keys[pygame.K_w]:
        left_vel = max(left_vel - PADDLE_SPEED, -PADDLE_MAX_SPEED)
    elif keys[pygame.K_s]:
        left_vel = min(left_vel + PADDLE_SPEED, PADDLE_MAX_SPEED)
    else:
        left_vel *= 0.9

    left_paddle.y += left_vel
    left_paddle.clamp_ip(pygame.Rect(0, 0, WIDTH//2, HEIGHT))

    # Right paddle
    if keys[pygame.K_UP]:
        right_vel = max(right_vel - PADDLE_SPEED, -PADDLE_MAX_SPEED)
    elif keys[pygame.K_DOWN]:
        right_vel = min(right_vel + PADDLE_SPEED, PADDLE_MAX_SPEED)
    else:
        right_vel *= 0.9

    right_paddle.y += right_vel
    right_paddle.clamp_ip(pygame.Rect(WIDTH//2, 0, WIDTH, HEIGHT))

    update_ball()
    draw()
