import sys
import pygame
import time
from PIL import Image
from pygame.locals import *

import tppflush as tf

running = True

pygame.display.init()
pygame.init()
surface = pygame.display.set_mode((1280, 720))

picture = Image.open("keybord.bmp")

picture = picture.resize((int(320*1.5),int(240*1.5)))

picture.save("Screen.jpg")

del picture

picture = pygame.image.load("Screen.jpg")

mode = 0 #0 touch_controle_mode, 1 keybord_controle_mode; 2 keybord_keyboard_mode, gamepad_controle_mode 




#while pygame.display.get_init:
#	pass
clock = pygame.time.Clock()
surfrect = surface.get_rect()



DPAD_POS = (192,552)
DPAD_SIZE = 96

ABYX_POS = (1080,360)
ABYX_SIZE = 128

CONTROL_BUTTONS_SIZE = (128,32)
CONTROL_BUTTONS_POS = (640,720-(CONTROL_BUTTONS_SIZE[1]/2))

SHOULDER_BUTTENS_SIZE = (80,32)

TOUCHSCREEN_POS = (600,360)
TOUCHSCREEN_SIZE = (320*1.5,240*1.5)

Touchscreen = pygame.Rect((0,0),TOUCHSCREEN_SIZE)
Touchscreen.center = TOUCHSCREEN_POS


#define keys
A_button = pygame.Rect((0, 0), (ABYX_SIZE, ABYX_SIZE))
A_button.center = (ABYX_POS[0] +ABYX_SIZE, ABYX_POS[1])
A_button_state = False

B_button = pygame.Rect((0, 0), (ABYX_SIZE, ABYX_SIZE))
B_button.center = (ABYX_POS[0], ABYX_POS[1]+ABYX_SIZE)
B_button_state = False

Y_button = pygame.Rect((0, 0), (ABYX_SIZE, ABYX_SIZE))
Y_button.center = (ABYX_POS[0]-ABYX_SIZE, ABYX_POS[1])
Y_button_state = False

X_button = pygame.Rect((0, 0), (ABYX_SIZE, ABYX_SIZE))
X_button.center = (ABYX_POS[0],ABYX_POS[1]-ABYX_SIZE)
X_button_state = False

UP_button = pygame.Rect((0, 0), (DPAD_SIZE, DPAD_SIZE))
UP_button.center = (DPAD_POS[0], DPAD_POS[1]-DPAD_SIZE)
UP_button_state = False

LEFT_button = pygame.Rect((0, 0), (DPAD_SIZE, DPAD_SIZE))
LEFT_button.center = (DPAD_POS[0]-DPAD_SIZE, DPAD_POS[1])
LEFT_button_state = False

DOWN_button = pygame.Rect((0, 0), (DPAD_SIZE, DPAD_SIZE))
DOWN_button.center = (DPAD_POS[0], DPAD_POS[1]+DPAD_SIZE)
DOWN_button_state = False

RIGHT_button = pygame.Rect((0, 0), (DPAD_SIZE, DPAD_SIZE))
RIGHT_button.center = (DPAD_POS[0]+DPAD_SIZE,DPAD_POS[1])
RIGHT_button_state = False

SELECT_button = pygame.Rect((0,  0), CONTROL_BUTTONS_SIZE)
SELECT_button.center = (CONTROL_BUTTONS_POS[0]-CONTROL_BUTTONS_SIZE[0]-10,CONTROL_BUTTONS_POS[1])
SELECT_button_state = False

HOME_button = pygame.Rect((0,  0), CONTROL_BUTTONS_SIZE)
HOME_button.center = (CONTROL_BUTTONS_POS)
HOME_button_state = False

START_button = pygame.Rect((0,  0), CONTROL_BUTTONS_SIZE)
START_button.center = (CONTROL_BUTTONS_POS[0]+CONTROL_BUTTONS_SIZE[0]+10,CONTROL_BUTTONS_POS[1])
START_button_state = False

L_button = pygame.Rect((0,  0), CONTROL_BUTTONS_SIZE)
L_button.center = (SHOULDER_BUTTENS_SIZE[0]/2,SHOULDER_BUTTENS_SIZE[1]/2)
L_button_state = False

R_button = pygame.Rect((0,  0), CONTROL_BUTTONS_SIZE)
R_button.center = (1280-(SHOULDER_BUTTENS_SIZE[0]/2),(SHOULDER_BUTTENS_SIZE[1]/2))
R_button_state = False
    
def drawTouchControls():
    pygame.draw.rect(surface,(20,20,20), Touchscreen)
    pygame.draw.rect(surface, (255,   0,   0),A_button) #draws the button red
    pygame.draw.rect(surface, (255,208,0),B_button)
    pygame.draw.rect(surface, (99,204,66),Y_button)
    pygame.draw.rect(surface, (0.,128,255),X_button)
    pygame.draw.rect(surface, (255,255,255),UP_button)
    pygame.draw.rect(surface, (255,0,255),DOWN_button)
    pygame.draw.rect(surface, (255,255,0),RIGHT_button)
    pygame.draw.rect(surface, (255,255,0),LEFT_button)
    pygame.draw.rect(surface, (255,255,255),SELECT_button)
    pygame.draw.rect(surface, (255,255,255),HOME_button)
    pygame.draw.rect(surface, (255,255,255),START_button)
    pygame.draw.rect(surface, (255,255,255),L_button)
    pygame.draw.rect(surface, (255,255,255),R_button)
    pygame.display.flip()



pygame.display.flip()
while False:
    for ev in pygame.event.get():
        if (ev.type == QUIT):
            pygame.quit()
        elif pygame.mouse.get_pressed(3)[0] == 1:
            pos = pygame.mouse.get_pos()
            if Touchscreen.collidepoint(pos):
                pygame.mouse.get_rel()
                Server.touch(int((pos[0]-(360,180)[0])/1.5),int((pos[1]-(360,180)[1])/1.5))

Server = tf.LumaInputServer("Nintendo-3DS.fritz.box")




def interfaceChek():
    for ev in pygame.event.get():
        if (ev.type == QUIT):
            pygame.quit()
        if (pygame.mouse.get_pressed(3)[0] == 1):
            pos = pygame.mouse.get_pos()
            if Touchscreen.collidepoint(pos):
                pygame.mouse.get_rel()
                Server.touch(int((pos[0]-(360,180)[0])/1.5),int((pos[1]-(360,180)[1])/1.5))
        else:
            Server.clear_touch()
            
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if A_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.A)
            if B_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.B)
            if Y_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.Y)
            if X_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.X)
            if UP_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.DPADUP)
            if DOWN_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.DPADDOWN) 
            if LEFT_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.DPADLEFT)
            if RIGHT_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.DPADRIGHT)
            if START_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.START)
            if SELECT_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.SELECT)
            if L_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.L)
            if R_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.R)
            if HOME_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.Special_Buttons.HOME)
        
        
        elif ev.type == pygame.MOUSEBUTTONUP:
            
            if A_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.A)
            if B_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.B)
            if Y_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.Y)
            if X_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.X)
            if UP_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.DPADUP)
            if DOWN_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.DPADDOWN) 
            if LEFT_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.DPADLEFT)
            if RIGHT_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.DPADRIGHT)
            if START_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.START)
            if SELECT_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.press(tf.HIDButtons.SELECT)
            if L_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.L)
            if R_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.HIDButtons.R)
            if HOME_button.collidepoint(ev.pos):
                pygame.mouse.get_rel()
                Server.unpress(tf.Special_Buttons.HOME)
        Server.send()
            
if mode == 0:
    drawTouchControls()
    surface.blit(picture,(TOUCHSCREEN_POS[0]-(TOUCHSCREEN_SIZE[0]/2),(TOUCHSCREEN_POS[1]-(TOUCHSCREEN_SIZE[1]/2))))
    pygame.display.flip()
while running:
    interfaceChek()
#   for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             
#         if event.type == pygame.KEYDOWN:
#             keys = pygame.key.get_re()
#             if keys[pygame.key.key_code("d")]:
#                 pass
#             elif keys[pygame.key.key_code("A")]:
#                 pass
#             elif keys[pygame.key.key_code("W")]:
#                 pass
#             elif keys[pygame.key.key_code("S")]:
#                 pass
#         if event.type == pygame.KEYUP:
#             keys = pygame.key.get_re()
#             if keys[pygame.key.key_code("d")]:
#                 pass
#             elif keys[pygame.key.key_code("A")]:
#                 pass
#             elif keys[pygame.key.key_code("W")]:
#                 pass
#             elif keys[pygame.key.key_code("S")]:
#                 pass
                
        
pygame.quit()
