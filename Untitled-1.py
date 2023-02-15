from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_width, player_height, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.width = player_width
        self.height = player_height
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


win_width = 700
win_height = 500



window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")

backgroud = transform.scale(image.load('fon.jpg'), (window_width, window_height))
rnaketka = transform.scale(image.load('raketka.jpg'), (10, 120))
raketka2 = transform.scale(image.load('raketka.jpg'), (235, 120))
ball = transform.scale(image.load('ball.jpg'), (win_width, win_height))


def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
        self.rect.y -= self.speed

def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed

FPS = 60
clock = time.Clock()

while game:
    window.blit(backgroud, (0, 0))

    display.update()
    clock.tick(FPS)