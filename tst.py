import pygame 
import pyArrow
import random

screenWidth, screenHeight = 500, 500
res = (screenWidth, screenHeight)
sc = pygame.display.set_mode(res)
clock = pygame.time.Clock()
pSize = 10
dt = 0

class Planet:
    def __init__(self, x, y, vx, vy, ax, ay, pSize, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.pSize = pSize
        self.color = color
        self.m = 5
        self.stack = []
        self.accCon = 3
        self.font = pygame.font.SysFont(None, 36)
        self.colors = ["red", "blue", "green", "yellow"]
        self.mVec = pyArrow.draw_arrow(sc, pygame.Vector2(x, y), pygame.Vector2(x+ax*1000, y+ay*1000), "red")
        self.aVector = (x-mouseCoords[0], y-mouseCoords[1])
        self.avec = pyArrow.draw_arrow(sc, pygame.Vector2(x, y), pygame.Vector2(x+ax*1000, y+ay*1000), "blue")

    def draw(self):
        pygame.draw.circle(sc, self.color, (self.x, self.y), self.pSize)

    def update(self, dt):
        self.vx = self.vx + self.ax * dt
        self.x = self.x + self.vx
        self.vy = self.vy + self.ay * dt
        self.y = self.y + self.vy

        if self.x >= screenWidth - self.pSize or self.x <= self.pSize:
            self.vx = -self.vx
            self.ax = -self.ax
        if self.y >= screenHeight - self.pSize or self.y <= self.pSize:
            self.vy = -self.vy
            self.ay = -self.ay


pygame.font.init()
solarSystem = [Planet(random.randint(0, screenWidth), random.randint(0, screenHeight), 0, 0, 0, 0, pSize, random.choice(["red", "blue", "green", "yellow"])) for _ in range(10)]

while True:
    sc.fill("#2e3440")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for planet in solarSystem:
        planet.draw()
        planet.update(dt)

    pygame.display.flip()

    dt = clock.tick(60) / 1000
