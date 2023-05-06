import pygame
import time

# Inicializar pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Tamaño de la ventana
WINDOW_SIZE = (600, 400)

# Crear la ventana
screen = pygame.display.set_mode(WINDOW_SIZE)

# Establecer el título de la ventana
pygame.display.set_caption("Gatito Pou")

# Clase gatito
class Gatito:
    def __init__(self, color):
        self.color = color
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = (WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)
        self.hunger = 100
        self.hearts = 5
        self.sleepiness = 0
        self.sleeping = False
        self.menu_active = True

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def update(self):
        if not self.menu_active:
            self.hunger -= 1
            if self.hunger == 0:
                self.hearts -= 1
                self.hunger = 100
                if self.hearts == 0:
                    self.menu_active = True
                    self.color = RED
                    self.hearts = 5
                    self.hunger = 100
                    self.sleepiness = 0
                    self.sleeping = False
                    pygame.time.wait(2000)
                    self.color = ORANGE

            if self.sleeping:
                self.sleepiness -= 1
                if self.sleepiness == 0:
                    self.sleeping = False
                    self.color = ORANGE
                    pygame.time.wait(2000)

    def feed(self):
        self.hunger += 50
        if self.hunger > 100:
            self.hunger = 100
        self.color = GREEN

    def sleep(self):
        self.sleeping = True
        self.sleepiness = 100
        self.color = PURPLE

    def click(self, pos):
        if self.rect.collidepoint(pos):
            if self.menu_active:
                self.menu_active = False
            else:
                self.feed()

    def draw_hearts(self):
        for i in range(self.hearts):
            x = 30 + i * 50
            pygame.draw.polygon(screen, RED, [(x, 20), (x+20, 40), (x+40, 20)])
            pygame.draw.polygon(screen, BLACK, [(x, 20), (x+20, 40), (x+40, 20)], 2)

    def draw_sleepiness(self):
        pygame.draw.rect(screen, BLUE, (WINDOW_SIZE[0]-100, 10, 90, 20))
        pygame.draw.rect(screen, self.color, (WINDOW_SIZE[0]-100, 10, 90*self.sleepiness/100, 20))


# Instanciar el gatito
g = Gatito(ORANGE)

# Bucle principal
running = True
while running:

    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            g.click(pos)

    # Actualizar estado del gatito
    g.update()

    # Dibujar elementos en la pantalla
    screen.fill(WHITE)
    g.draw()
    g.draw_hearts()
    g.draw_sleepiness()

    # Actualizar pantalla
    pygame.display.flip()

    # Esperar un poco
    time.sleep(0.01)

# Salir de pygame
pygame.quit()

