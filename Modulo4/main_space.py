import pygame
import math
from pygame import mixer

def player(x, y, screen, playerImg): 
    screen.blit(playerImg, (x, y))


def game_over(screen, over_font): 
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (150, 250))

def win(screen, over_font): 
    font = pygame.font.Font('freesansbold.ttf', 20)
    win_text = over_font.render('VICTORY!', True, (255,255,255))
    salir_text = font.render('PRESS ESC TO EXIT', True, (255,255,255))
    reiniciar_text =font.render('PRESS UP KEY TO PLAY AGAIN', True, (255,255,255))
    screen.blit(win_text, (200, 250))
    screen.blit(salir_text, (300, 350))
    screen.blit(reiniciar_text, (250, 400))

    

def show_score(x, y, score, over_font, screen, font):
    score_t = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_t, (x,y))
    if score == 12:
        win(screen, over_font) 


#Enemy 1
enemyImg_1 = []


def create_enemies(num_enemies, enemyX, enemyY):
    for i in range(num_enemies): 
        enemyImg_1.append(pygame.image.load('img/alien.png'))
        enemyX.append(30+(i*30))
        enemyY.append(60)

def enemy(x, y, screen): 
    screen.blit(enemyImg_1[0], (x, y))
    # Bullet 



bulletImg = pygame.image.load('img/bullet.png')
def bullet(x, y, bullet_state, screen): 
    bullet_state = False
    screen.blit(bulletImg, (x,y+5))
    return bullet_state

# Collision
def isCollision(bulletX, bulletY, enemyX, enemyY):
    distance = math.sqrt(math.pow((enemyX-bulletX), 2) + math.pow((enemyY-bulletY), 2))
    if distance < 27: 
        return True
    else: 
        return False
        
def game_loop():
    # Game loop
    pygame.init()

    playerX = 370
    playerY = 480
    enemyX_change = 0.7
    num_enemies = 12
    bulletX, bulletY = 0, 0
    bullet_state = True
    score = 0
    enemyX = []
    enemyY = []
    playerImg = pygame.image.load('img/nave.png')
    screen = pygame.display.set_mode((800, 550))
    background = pygame.image.load('img/background.jpeg')
    bullet_sound = mixer.Sound('sounds/laser.wav')
    hit_sound = mixer.Sound('sounds/hit.wav')
    gameover_sound = mixer.Sound('sounds/gameover.wav')
    
    mixer.music.load('sounds/background.wav')
    mixer.music.play(-1)
    #Title and icon
    pygame.display.set_caption("Space Invaders")

    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10
    #game over 
    over_font = pygame.font.Font('freesansbold.ttf', 80)

    
    create_enemies(num_enemies, enemyX, enemyY)
    running = True 
    while running: 
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        # para mover la nave 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                print("Pressed left")
                playerX -= 4
            if event.key == pygame.K_RIGHT: 
                print("Pressed right")
                playerX += 4
            if event.key == pygame.K_BACKSPACE:
                bulletX = playerX
                bulletY = playerY 
                bullet_sound.play()
                bullet_state = bullet(bulletX, bulletY, bullet_state, screen)
            if event.key == pygame.K_ESCAPE: 
                pygame.quit()
            if event.key ==pygame.K_UP: 
                game_loop()
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE: 
                    pass

        if playerX < 0: 
            playerX = 0
        elif playerX > 770: 
            playerX = 770

        for i in range(num_enemies): 
            enemyX[i] += enemyX_change

            if enemyX[i] < 10: 
                enemyX_change = 0.7
                for j in range(num_enemies):
                    enemyY[j] += 10
            
            elif enemyX[i] > 760: 
                enemyX_change = -0.7
                for j in range(num_enemies):
                    enemyY[j] += 10 
            if enemyY[i] == playerY - 20: 
                gameover_sound.play()
                game_over(screen, over_font)
                break

            collision = isCollision(bulletX=bulletX, bulletY=bulletY, enemyX=enemyX[i], enemyY=enemyY[i])
            if collision: 
                hit_sound.play()
                bulletY = 480
                bullet_state = True
                score += 1 
                num_enemies -= 1
                hit_sound.play()
            enemy(enemyX[i], enemyY[i], screen)

        if bullet_state == False: 
            bullet_state = bullet(bulletX, bulletY, bullet_state, screen)
            bulletY -= 4
        player(playerX, playerY, screen, playerImg)
        show_score(textX, textY, score, over_font, screen, font)  

        pygame.display.update()

if __name__ == '__main__': 
    game_loop()