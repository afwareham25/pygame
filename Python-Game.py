import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 700
FPS = 60

PLAYER_VELOCITY_X = 100
GRAVITY = 2000

GAME_OVER = False

#smallfont = pygame.font.SysFont('Corbel',35)
#text = smallfont.render("Restart?" , True , WHITE)
##

class Player:
  X = 0
  Y = 0
  RADIUS = 100
  score = 0
  speed = 1.0


def update(p):
  if p.X < 0 + p.RADIUS/2:
    p.X = 0 + p.RADIUS/2
  if p.X > SCREEN_WIDTH - p.RADIUS/2:
    p.X = SCREEN_WIDTH - p.RADIUS/2
  if p.Y < 0 - p.RADIUS/2:
    p.Y = 0 - p.RADIUS/2
  if p.Y > SCREEN_HEIGHT - p.RADIUS * 1.5:
    p.Y = SCREEN_HEIGHT - p.RADIUS * 1.5

  if p == coin:
    if p.X == 0 + p.RADIUS/2:
      coin.speedX = -coin.speedX
    if p.Y == 0 - p.RADIUS/2:
      coin.speedY = -coin.speedY
    if p.X == SCREEN_WIDTH - p.RADIUS/2:
      coin.speedX = -coin.speedX
    if p.Y == SCREEN_HEIGHT - p.RADIUS * 1.5:
      coin.speedY = -coin.speedY
    


def collision(a, b):
  if a.X <= a.RADIUS + b.X and a.X >= -a.RADIUS + b.X:
    if a.Y <= a.RADIUS + b.Y and a.Y >= -a.RADIUS + b.Y:
      return True

  
p1 = Player()
p2 = Player()

p1.colour = (247, 0, 21)
p2.colour = (100, 150 , 60)
p2.X = 700

coin = Player()
coin.colour = "yellow"
coin.X = 400
coin.Y = 300
coin.speedX = 15   
coin.speedY = 20

def show_player(p):
  update(p)
  if GAME_OVER == True:
    return
  
  pygame.draw.circle(screen, p.colour, (p.X, -p.Y + SCREEN_HEIGHT - p.RADIUS), 50)
  if p == coin:
    p.RADIUS = 75
  if p != coin:
    if (p.X <= 75 + coin.X and p.X >= -75 + coin.X and 
        p.Y <= 75 + coin.Y and p.Y >= -75 + coin.Y):
          p.score += 1
          coin.colour = "orange"
          coin.speedX *= 1.001

    font = pygame.font.SysFont(None, 48)
    t = font.render(str(p.score), 1, (255,255,255))
    textx = 100
    if p == p1:
      textx = 500
    screen.blit(t, (textx, SCREEN_HEIGHT/16 - t.get_height()/2))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  coin.X += coin.speedX
  coin.Y += coin.speedY
  coin.colour = "yellow"    
 
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    p1.X -= 20
  if keys[pygame.K_RIGHT]:
    p1.X += 20
  if keys[pygame.K_UP]:
    p1.Y -= -20
  if keys[pygame.K_DOWN]:
    p1.Y += -20
  if keys[pygame.K_a]:
    p2.X -= 20
  if keys[pygame.K_d]:
    p2.X += 20
  if keys[pygame.K_w]:
    p2.Y -= -20
  if keys[pygame.K_s]:
    p2.Y += -20



  screen.fill((100, 100, 100))

  if p1.score >= 150:
    font = pygame.font.SysFont(None, 48)
    t = font.render(str("Player 1 Wins!"), 1, (255,255,255))
    screen.blit(t, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2 - t.get_height()/2))
    GAME_OVER = True

  if p2.score >= 150:
    font = pygame.font.SysFont(None, 48)
    t = font.render(str("Player 2 Wins!"), 1, (255,255,255))
    screen.blit(t, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2 - t.get_height()/2))
    GAME_OVER = True


  show_player(p1)
  show_player(p2)
  show_player(coin)
  collision(p1, p2)
  pygame.display.flip()
  clock.tick(FPS)