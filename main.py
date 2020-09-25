import pygame
from Colores import Colores

pygame.init()
dimensiones=[730,730]
pantalla = pygame.display.set_mode(dimensiones)

correrPrograma=True

# Jugador
peonImg=pygame.image.load('img/peon.png')
peonX = dimensiones[0]//2.2
peonY = 15
peonX_cambio = 0
peonY_cambio = 0

#RECUADROS
casillaAncho=80
casillaAlto=80
#LINEAY
lineaYAncho=80
lineaYAlto=10
#LINEAX
lineaXAncho=10
lineaXAlto=80
#PosicionMouse
posicionMouse=0
#MURO
muroX=0
muroY=0
muroAncho=80
muroAlto=80
muroRec=pygame.Rect(muroX,muroY,muroAncho,muroAlto)
def Peon(X,Y):
    pantalla.blit(peonImg, (X, Y))

while correrPrograma:
   pantalla.fill(Colores.gris)
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
          correrPrograma=False
       if evento.type == pygame.MOUSEBUTTONUP:
          posicionMouse = pygame.mouse.get_pos()
       #if evento.type == pygame.KEYDOWN:


   SaltolineaY=0
   SaltolineaX=0

   for i in range(0,dimensiones[0],casillaAncho):
        for j in range(0,dimensiones[1],casillaAlto):
            pygame.draw.rect(pantalla, Colores.negro, [i, j, lineaYAncho, lineaYAlto], 0)
            pygame.draw.rect(pantalla, Colores.negro, [i, j, lineaXAncho, lineaXAlto], 0)

   
   Peon(peonX,peonY)
   pygame.display.update()  # actualiza la pantalla





