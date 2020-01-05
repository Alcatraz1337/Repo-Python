from pg_engine import *

# the game's variables
myfont_l = pygame.font.SysFont("Arial", 30)
myfont_s = pygame.font.SysFont("Arial", 15)

score = 0 # starts from zero
lives = 3 # the number of lives
balls = 2 # the number of balls

ball_radius = 10
ball_speed_x = 3

temp_ball_speed_x = ball_speed_x
ball_speed_y = 2
ball_speed_boost = 1.1
ball = []
# generates balls
for i in range(0, balls):
    ball.append(MovingSphere(randint(0, screen.get_width()), 0,
                            ball_radius, temp_ball_speed_x, ball_speed_y, random_color()))
    temp_ball_speed_x = -temp_ball_speed_x

# loads the R image (must be saved in the same place as this file)
my_R = pygame.image.load('Rh.jpg')
# generates the paddle
paddle = MovingRectangle(screen.get_width()/2, screen.get_height()-2 *
                        my_R.get_height(), my_R.get_width(), my_R.get_height(), 0, 0, [0, 0, 0])

running = True
# game loop
while running:
    # checks events
    for event in pygame.event.get():
        # checks if you've exited the game
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False

    # controls the paddle
    if event.type == pygame.MOUSEMOTION:
        coordinates = pygame.mouse.get_pos() # gives (x,y) coordinates
        paddle.x = coordinates[0]
        # if the paddle is off the left side brings it back
        if paddle.x < paddle.width/2:
            paddle.x = paddle.width/2
        # if the paddle is off the right side brings it back
        if paddle.x > screen.get_width() - paddle.width/2:
            paddle.x = screen.get_width() - paddle.width/2

# pauses for 33 milliseconds
pygame.time.delay(33) # 30 FPS

# makes the screen completely black
screen.fill(pygame.color.THECOLORS['black'])

# updates the paddle
paddle.update()

# moves balls
for i in range(0, len(ball)):
    # sees if rectangles overlap
    # the ball and the paddle
    if doRectsOverlap(ball[i].rect, paddle.rect):
        ball[i].speed_x, ball[i].speed_y = compute_ball_velocity(ball[i], paddle.rect)
        # only scores and boosts the ball speed when the ball bounces up
        if ball[i].speed_y < 0:
            ball[i].speed_x = ball[i].speed_x * ball_speed_boost
            ball[i].speed_y = ball[i].speed_y * ball_speed_boost
            score = score + 1

    # checks if the ball is off the bottom of the screen
    if ball[i].y > screen.get_height() + ball[i].radius:
        ball[i].y = 0
        lives = lives - 1
        # resets the ball speed
        ball[i].speed_x = ball_speed_x*ball[i].speed_x/abs(ball[i].speed_x)
        ball[i].speed_y = ball_speed_y
    # checks if the ball hit the top of the screen
    elif ball[i].y < ball[i].radius:
        ball[i].speed_y = abs(ball[i].speed_y)
    # checks if the ball hit the left side of the screen
    elif ball[i].x < ball[i].radius:
        ball[i].speed_x = abs(ball[i].speed_x)
    # checks if the ball hit the right side of the screen
    elif ball[i].x > screen.get_width() - ball[i].radius:
        ball[i].speed_x = -abs(ball[i].speed_x)

    # updates the ball
    ball[i].update()

# draws everything on the screen
# score
score_label = myfont_l.render("Your Score: {0}".format(
    str(score)), 1, pygame.color.THECOLORS['white'])
screen.blit(score_label, (10, screen.get_height()-30))
# lives
lives_label = myfont_l.render("Your Lives: {0}".format(
    str(lives)), 1, pygame.color.THECOLORS['white'])
screen.blit(lives_label, (screen.get_width() -
    175, screen.get_height()-30))
# the paddle
screen.blit(my_R, [paddle.rect.x, paddle.rect.y])
# the paddle's hitbox for demonstration
pygame.draw.rect(screen, pygame.color.THECOLORS['white'], (
    paddle.rect.x, paddle.rect.y, paddle.rect.width, paddle.rect.height), 3)
# balls
for i in range(0, len(ball)):
    # each ball
    pygame.draw.circle(screen, ball[i].color, [
        int(ball[i].x), int(ball[i].y)], ball[i].radius, 0)
    # each ball's hitbox for demonstration
    pygame.draw.rect(screen, pygame.color.THECOLORS['green'], (
        ball[i].rect.x, ball[i].rect.y, ball[i].rect.width, ball[i].rect.height), 3)

# updates the relevant portions in the display
pygame.display.update()

# checks if the game ends
if lives <= 0:
    running = False

pygame.quit()