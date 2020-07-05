from pg_engine import *
from Controller import * #new import
#from EMG import * #new import
from Keyboard import * #new import

paddle_speed = 5 #a new variable for the paddle speed
#Controller = EMG(threshold_left=0.7, threshold_right=0.7, frequency=50 * 30) #new 
Controller = Keyboard() #new 

# the game's variables
myfont_l = pygame.font.SysFont("Arial", 30)
myfont_s = pygame.font.SysFont("Arial", 15)

clock = pygame.time.Clock()

score = 0  # starts from zero
lives = 100  # the number of lives
balls = 2  # the number of balls

# Parameters about bullets
bullet = []
bullet_speed = 10
fire_rate = 450
last_fire_time = pygame.time.get_ticks()

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
my_R = pygame.image.load('Ritsumei_Project\sample\sample\Rh.jpg')
# generates the paddle
paddle = MovingRectangle(screen.get_width()/2, screen.get_height()-2 *
                         my_R.get_height(), my_R.get_width(), my_R.get_height(), 0, 0, [0, 0, 0])
block = []
blocks = 5
block_speed_x = 1
block_speed_y = 0
temp_block_speed_x = block_speed_x
for i in range(0, blocks):
    block.append(MovingRectangle(randint(0, screen.get_width()), randint(0, 1/2 * screen.get_height()), my_R.get_width(), my_R.get_height(),  temp_block_speed_x, block_speed_y, [0, 0, 0]))
    temp_block_speed_x = -temp_block_speed_x

running = True
temp_speed = 0
# game loop
while running:
    clock.tick(60)
    # checks events
    for event in pygame.event.get():
        # checks if you've exited the game
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False

    # controls the paddle
    input = Controller.get_input()
    if input == Controller.Input.Left:
        paddle.x += -paddle_speed
        temp_speed = -paddle_speed
    elif input == Controller.Input.Right:
        paddle.x += paddle_speed
        temp_speed = paddle_speed
    #if Player press Left and Right at the same time, shoot the bullet
    elif input == Controller.Input.Launch:
        if pygame.time.get_ticks() - last_fire_time >= fire_rate:
            bullet.append(MovingSphere(paddle.x, paddle.y + 1/2 * paddle.height, 1, 0, -bullet_speed, (255,255,255)))
            last_fire_time = pygame.time.get_ticks()
    else:
        paddle.x += 0
        
    # if the paddle is off the left side brings it back
    if paddle.x < paddle.width/2:
        paddle.x = paddle.width/2
    # if the paddle is off the right side brings it back
    if paddle.x > screen.get_width() - paddle.width/2:
        paddle.x = screen.get_width() - paddle.width/2

    # pauses for 33 milliseconds
    pygame.time.delay(33)  # 30 FPS

    # makes the screen completely black
    screen.fill(pygame.color.THECOLORS['black'])

    # updates the paddle
    paddle.update()

    # moves bullets
    for i in range(0, len(bullet)):
        bullet[i].update()

    # moves blocks
    for i in range(0, len(block)):
        if block[i].x < block[i].width/2:
            block[i].speed_x = abs(block[i].speed_x)
        elif block[i].x > screen.get_width() - block[i].width/2:
            block[i].speed_x = -abs(block[i].speed_x)
        # updates the block
        block[i].update()

    # moves balls
    for i in range(0, len(ball)):
        # sees if rectangles overlap
        # the ball and blocks
        for j in range(0, len(block)):
            ball[i].speed_x, ball[i].speed_y = compute_ball_velocity(ball[i], block[j].rect)
            
        # the ball and the paddle
        if doRectsOverlap(ball[i].rect, paddle.rect):
            ball[i].speed_x, ball[i].speed_y = compute_ball_velocity(
                ball[i], paddle.rect)
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
    # blocks
    for i in range(0, len(block)):
        screen.blit(my_R, [block[i].rect.x, block[i].rect.y])
    # balls
    for i in range(0, len(ball)):
        # each ball
        pygame.draw.circle(screen, ball[i].color, [
            int(ball[i].x), int(ball[i].y)], ball[i].radius, 0)
        # each ball's hitbox for demonstration
        pygame.draw.rect(screen, pygame.color.THECOLORS['green'], (
            ball[i].rect.x, ball[i].rect.y, ball[i].rect.width, ball[i].rect.height), 3)
    #bullets
    for i in range(0, len(bullet)):
        pygame.draw.circle(screen, bullet[i].color, [int(bullet[i].x), int(bullet[i].y)], bullet[i].radius, 0)

    # updates the relevant portions in the display
    pygame.display.update()

    # checks if the game ends
    if lives <= 0:
        running = False

Controller.close()
pygame.quit()




