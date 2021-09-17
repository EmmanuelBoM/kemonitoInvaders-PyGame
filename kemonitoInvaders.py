import pygame, random


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("D:/Users/emman/Documents/Trabajos ITESM/5°/Semana TEC 1/kemonitoInvaders-PyGame/platano.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('D:/Users/emman/Documents/Trabajos ITESM/5°/Semana TEC 1/kemonitoInvaders-PyGame/mascarita.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('D:/Users/emman/Documents/Trabajos ITESM/5°/Semana TEC 1/kemonitoInvaders-PyGame/kemonito.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def  update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = 450

    
negro = 0,0,0
blanco = 255,255,255
pygame.init()
pygame.mixer.music.load('D:/Users/emman/Documents/Trabajos ITESM/5°/Semana TEC 1/kemonitoInvaders-PyGame/luchadores2.mp3')
pygame.mixer.music.play(1)
def main():
    
    pygame.init()
    screen = pygame.display.set_mode([1140,600])

    clock = pygame.time.Clock()
    run = True
    score = 0
    
    width = 1140
    height = 600
    i = 0

    fondo = pygame.image.load('D:/Users/emman/Documents/Trabajos ITESM/5°/Semana TEC 1/kemonitoInvaders-PyGame/RingSolo.jpg')
    fondorect = fondo.get_rect();
    bg = pygame.transform.scale(fondo, (1140,600) )
    
    all_sprite_list = pygame.sprite.Group()
    meteor_list = pygame.sprite.Group()
    laser_list = pygame.sprite.Group()

    for i in range(20):
        meteor = Meteor()
        meteor.rect.x = random.randrange(1000)
        meteor.rect.y = random.randrange(200)
        #mov=meteor.rect()
        
        meteor_list.add(meteor)
        all_sprite_list.add(meteor)

    player = Player()
    all_sprite_list.add(player)
    fuente = pygame.font.Font(None, 50) #Tipo de fuente por default
    texto = fuente.render("Jugador 1", 0, (100,100,0)) #el segundo parametro es el borde y la ultima es el color

    speed=[1,1]
    
    sound = pygame.mixer.Sound('D:/Users/emman/Documents/Trabajos ITESM/5°/Semana TEC 1/kemonitoInvaders-PyGame/bonk2.mp3')
    #pygame.mixer.music.load('C:/Users/edgar/OneDrive/Escritorio/luchadores2.mp3')
    #pygame.mixer.music.play(1)

    while run:
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = player.rect.x + 50
                laser.rect.y = player.rect.y - 20

                all_sprite_list.add(laser)
                laser_list.add(laser)
                sound.play()
    
        all_sprite_list.update()
        
        for meteor in meteor_list:
            meteor.rect.y+=random.randrange(4)
            if(meteor.rect.y>600):
                meteor_list.remove(meteor)
                all_sprite_list.remove(meteor)
            
            
        for laser in laser_list:
            meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True) # el true es para que desaparezcan
            #para eliminar el laser en las colisiones
            
            for meteor in meteor_hit_list:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
                score += 1
                print(score)
                
            if laser.rect.y < 0:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
        
        screen.fill((0,0,0))
        screen.blit(bg, (i,0))
        #screen.blit(bg, (0,i))
        screen.blit(bg, (width+i,0))
        #screen.blit(bg, (0,height+i))

        if i == -width:
        #if i == -height:
            screen.blit(bg, (width+i, 0))
            #screen.blit(bg, (0, height+i))
            i = 0

        i -= 3
        
        
        if(score==20 or len(meteor_list)==0):
            main()
        
        #screen.fill(blanco)
        #screen.blit(fondo, fondorect)
        marcador1 = fuente.render("Score:"+str(score), 0, (100,100,0))
        screen.blit(marcador1, (950, 40))
        all_sprite_list.draw(screen) #se pintan todos los sprites


        pygame.display.flip()
        clock.tick(60)
    pygame.quit()



if __name__ == "__main__":
    main()
