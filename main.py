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
             
                rend.setShader(vertex_shader1, fragmet_shader)
            elif event.key == pygame.K_2:
                
                pass

            elif event.key == pygame.K_3:
                
                pass

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

    # Actualiza la rotación del modelo si se desea
    # gato.rotation.y += 45 * deltaTime

    rend.elapsedTime += deltaTime

    rend.update()
    rend.render()

    pygame.display.flip()

pygame.quit()
