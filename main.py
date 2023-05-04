# moduels
import pygame

pygame.init()

# Constant variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BACKGROUND = pygame.image.load("img/surface_background.png")

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))

# pygame display setup
pygame.display.set_caption("PygameStudy")

# Character var
CHARACTER_IMG: pygame.Surface = pygame.image.load("img\character.png")
CHARACTER_RECT: pygame.rect = CHARACTER_IMG.get_rect()

CHARACTER_WIGHT: int = CHARACTER_RECT.size[0]
CHARACTER_HEIGHT: int = CHARACTER_RECT.size[1]
CHARACTER_POS: pygame.Vector2 = pygame.Vector2(CHARACTER_WIGHT / 2, CHARACTER_HEIGHT - CHARACTER_HEIGHT)

is_runing = True

while is_runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_t:
                    print("test")

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(CHARACTER_IMG, CHARACTER_POS) 

    pygame.display.update()
    
pygame.quit()