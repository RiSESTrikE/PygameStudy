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

# Class
# Character class
class Character:
    def __init__(self, pos: pygame.Vector2, img: pygame.Surface) -> None:
        self.pos = pos
        self.img = img
        self.dir = "none"

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.img, self.pos)
    
    def move(self, df: int):
        if self.dir == "up":
            self.pos.y -= 10+df
        if self.dir == "down":
            self.pos.y += 10+df
        if self.dir == "left":
            self.pos.x -= 10+df
        if self.dir == "right":
            self.pos.x += 10+df

# Character var
CHARACTER_IMG: pygame.Surface = pygame.image.load("./img/character.png")
CHARACTER_RECT: pygame.rect = CHARACTER_IMG.get_rect()

CHARACTER_WIGHT: int = CHARACTER_RECT.size[0]
CHARACTER_HEIGHT: int = CHARACTER_RECT.size[1]
CHARACTER_POS: pygame.Vector2 = pygame.Vector2(CHARACTER_WIGHT / 2, CHARACTER_HEIGHT - CHARACTER_HEIGHT)
CHARACTER_CLASS: Character = Character(CHARACTER_POS, CHARACTER_IMG)

is_runing = True

while is_runing:
    df = clock.tick(100) / 1000
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runing = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    CHARACTER_CLASS.dir = "up"
                case pygame.K_DOWN:
                    CHARACTER_CLASS.dir = "down"
                case pygame.K_LEFT:
                    CHARACTER_CLASS.dir = "left"
                case pygame.K_RIGHT:
                    CHARACTER_CLASS.dir = "right"
        if event.type == pygame.KEYUP:
            CHARACTER_CLASS.dir = "none"
                

    screen.blit(BACKGROUND, (0, 0))
    CHARACTER_CLASS.draw(screen)
    CHARACTER_CLASS.move(df) 

    pygame.display.update()
pygame.quit()