from pygame import *




class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.imagee = player_image
       self.speed_x = player_speed
       self.speed_y = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    def move(self):
        if self.rect.x > 0 and self.rect.x != 650:
            self.rect.x += self.speed_x
            self.rect.y -= self.speed_y
        if self.rect.y == 0:
            self.speed_x *= 1
            self.speed_y *= -1
        if self.rect.y == 450:
            self.speed_x *= 1
            self.speed_y *= -1
               
        if sprite.collide_rect(myach, rock1):
            self.speed_x *= -1
        if sprite.collide_rect(myach, rock2):
            self.speed_x *= -1

class Rocket(GameSprite):
    def move(self, k1, k2):
        keys_pressed = key.get_pressed()
        if keys_pressed[k1] and self.rect.y < 400 :
            self.rect.y += self.speed_y
        if keys_pressed[k2] and  self.rect.y > 0:
            self.rect.y -= self.speed_y

myach = Ball('zelya.png', 350, 250, 50, 50, 5)
rock1 = Rocket('rus.png', 650, 250, 20, 100, 6)
rock2 = Rocket('nato.png', 50, 250, 20, 100, 6)
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("Krym.jpg"), (win_width, win_height))
FPS = 24
clock = time.Clock()
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       
    if finish != True:
        window.blit(background,(0, 0))
        myach.reset()
        myach.move()
        rock1.reset()
        rock1.move(K_DOWN, K_UP)
        rock2.reset()
        rock2.move(K_s, K_w)
        clock.tick(FPS)
        display.update()