from pygame import *




class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.imagee = player_image
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Ball(GameSprite):
    def move(self):
        if self.rect.x < 650:    
            if self.rect.x > 0 and self.rect.y > 0:
                self.rect.x += self.speed
                self.rect.y -= self.speed
            if self.rect.x > 0 and self.rect.y == 0:
                self.rect.x += self.speed
                self.rect.y += self.speed
        


myach = Ball('zelya.png', 350, 250, 50, 50, 5)


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



        clock.tick(FPS)
        display.update()