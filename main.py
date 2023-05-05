# moduels
import pygame

pygame.init()

# Constant variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BACKGROUND = pygame.image.load("img/surface_background.png")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))

# pygame display setup
pygame.display.set_caption("PygameStudy")

# Character var
CHARACTER_IMG: pygame.Surface = pygame.image.load("./img/character.png")
CHARACTER_RECT: pygame.rect = CHARACTER_IMG.get_rect()

CHARACTER_WIGHT: int = CHARACTER_RECT.size[0]
CHARACTER_HEIGHT: int = CHARACTER_RECT.size[1]
CHARACTER_POS: pygame.Vector2 = pygame.Vector2(CHARACTER_WIGHT / 2, CHARACTER_HEIGHT - CHARACTER_HEIGHT)

is_runing = True

while is_runing:
    df = clock.tick(100) / 1000
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runing = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP: # up 키를 눌렀을때
                    CHARACTER_POS.y -= df+10 # 캐릭터의 y 좌표를 10만큼 빼준다
                case pygame.K_DOWN: # down 키를 눌렀을때
                    CHARACTER_POS.y += df+10 # 캐릭터의 y 좌표를 10만큼 더해준다
                case pygame.K_LEFT: # left 키를 눌렀을때
                    CHARACTER_POS.x -= df+10 # 캐릭터의 x 좌표를 10만큼 빼준다
                case pygame.K_RIGHT: # right 키를 눌렀을때
                    CHARACTER_POS.x += df+10 # 캐릭터의 x 좌표를 10만큼 더해준다
                

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(CHARACTER_IMG, CHARACTER_POS) 

    pygame.display.update()
pygame.quit()