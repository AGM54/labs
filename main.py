import pygame
from pygame.locals import *
import glm
from gl import Renderer
from model import Model
from shaders import *
from obj import Obj

width = 500
height = 400

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShader(vertex_shader, fragmet_shader)
actualvertex=vertex_shader
actualfragment=fragmet_shader
obj = Obj("cat.obj")
gato = Model(obj.assemble())
gato.loadTexture("Cat.jpg")
gato.position.z = -10
gato.scale = glm.vec3(0.17,0.17,0.17)
gato.rotation = glm.vec3(0,0,0)

rend.scene.append(gato)
rend.target = gato.position

isRunning = True
while isRunning:
    deltaTime = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_SPACE:
                rend.toggleFilledMode()
            elif event.key == pygame.K_1:
                rend.setShader(vertex_shader, fragmet_shader)
                actualvertex=vertex_shader1
                rend.setShader(vertex_shader1, actualfragment)
            elif event.key == pygame.K_2:
                rend.setShader(vertex_shader2, fragmet_shader)
                actualvertex=vertex_shader2
                rend.setShader(vertex_shader2, actualfragment)

            elif event.key == pygame.K_3:
                rend.setShader(vertex_shader, fragmet_shader)
                actualvertex=vertex_shader3
                rend.setShader(vertex_shader3, actualfragment)
            elif event.key == pygame.K_4:
                rend.setShader(vertex_shader, fragmet_shader)
                actualvertex=vertex_shader4
                rend.setShader(vertex_shader4, actualfragment)   
            elif event.key == pygame.K_5:
                rend.setShader(vertex_shader, fragmet_shader)
                actualfragment=fragmet_shader1
                rend.setShader(actualvertex, fragmet_shader1) 
            elif event.key == pygame.K_6:
                rend.setShader(vertex_shader, fragmet_shader)
                actualfragment=fragmet_shader2
                rend.setShader(actualvertex, fragmet_shader2) 
            elif event.key == pygame.K_7:
                rend.setShader(vertex_shader, fragmet_shader)
                actualfragment=fragmet_shader3
                rend.setShader(actualvertex, fragmet_shader3)    
            elif event.key == pygame.K_8:
                rend.setShader(vertex_shader, fragmet_shader)
                actualfragment=fragmet_shader4
                rend.setShader(actualvertex, fragmet_shader4)      

    if keys[K_a]:
        rend.camPosition.x += 5 * deltaTime
    elif keys[K_d]:
        rend.camPosition.x -= 5 * deltaTime

    if keys[K_w]:
        rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        rend.camPosition.y -= 5 * deltaTime

    if keys[K_q]:
        rend.camPosition.z += 5 * deltaTime
    elif keys[K_e]:
        rend.camPosition.z -= 5 * deltaTime


    rend.elapsedTime += deltaTime

    rend.update()
    rend.render()

    pygame.display.flip()

pygame.quit()
