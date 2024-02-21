import pygame 
import pyArrow
import random
screenWidth, screenHeight = 500, 500
res = (screenWidth, screenHeight)
dt = 0
sc = pygame.display.set_mode(res)
clock = pygame.time.Clock()
pSize = 10
x, y = screenWidth/2, screenHeight/2
vx, vy = 0, 0 
ax, ay = 0, 0 


class Planet:
    def __init__(self, x, y, vx, vy, ax, ay, pSize, color, weight):
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
        self.weight = weight
        self.font = pygame.font.SysFont(None, 36)
        self.aVector = (0, 0)
        self.avec = pyArrow.draw_arrow(sc, pygame.Vector2(x, y), pygame.Vector2((x+ax)*(1000*(1/self.weight)), (y+ay)*(1000*(1/weight))), "blue")
        
    def draw(self):
        pygame.draw.circle(sc, self.color, (self.x, self.y), self.pSize)

    def update(self, dt):
        self.tx, self.ty = self.x, self.y
        for planet in solarSystem:
            if planet != self:  # Avoid calculating acceleration due to self
                dx = planet.x - self.x
                dy = planet.y - self.y
                r = max(1, (dx ** 2 + dy ** 2) ** 0.5)  # Distance between the two planets
                force = planet.weight / r ** 2  # Gravitational force
                self.ax += force * dx / r  # Acceleration components
                self.ay += force * dy / r
        
        for i, ob in enumerate(self.stack):
            pygame.draw.circle(sc, f"#88{i}cd0", ob, self.pSize)

        if len(self.stack) > 9:
            self.stack.pop(0)





        if mouseCoords[0] == 0 or mouseCoords[1] == 0 or mouseCoords[0] == screenWidth-1 or mouseCoords[1] == screenHeight-1:
            mouseCoords[0] = self.x
            mouseCoords[1] = self.y

        # mVec = pyArrow.draw_arrow(sc, pygame.Vector2(x,y), pygame.Vector2(mouseCoords[0], mouseCoords[1]), "red")
        self.aVector = ((self.x-mouseCoords[0])*(1/self.weight), (self.y-mouseCoords[1])*(1/self.weight))
        self.aVectorDistance = (self.aVector[0]**2 + self.aVector[1]**2)**0.5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.ay > 0: self.ay = 0
            else: self.ay = -self.accCon * dt
        elif keys[pygame.K_s]:
            if self.ay < 0: self.ay = 0
            else: self.ay = self.accCon * dt
        elif keys[pygame.K_a]:
            if self.ax > 0: self.ax = 0
            else: self.ax = -self.accCon * dt
        elif keys[pygame.K_d]:
            if self.ax < 0: self.ax = 0
            else: self.ax = self.accCon * dt


        if (self.aVector[1] < self.y):
            self.ay = -self.accCon * 1/100 * self.aVector[1] * dt
        if (self.aVector[1] > self.y):
            self.ay = self.accCon * 1/100 *  self.aVector[1] * dt
        if (self.aVector[0] < self.x):
            self.ax = -self.accCon * 1/100 * self.aVector[0] * dt
        if (self.aVector[0] > self.x):
            self.ax = self.accCon * 1/100 * self.aVector[0] * dt


        self.vx = self.vx - self.vx*0.01
        self.vy = self.vy - self.vy*0.01

        
        
        
        self.vx = self.vx + self.ax
        self.x = self.x + self.vx

        self.vy = self.vy + self.ay
        self.y = self.y + self.vy

        if self.x >= screenWidth-self.pSize:
            self.x = self.tx
            self.vx = -self.vx
            self.ax = -self.ax
        if self.x <= self.pSize:
            self.x = self.tx
            self.vx = -self.vx
            self.ax = -self.ax
        if self.y >= screenHeight-self.pSize:
            self.y = self.ty
            self.vy = -self.vy
            self.ay = -self.ay
        if self.y <= self.pSize:
            self.y = self.ty
            self.vy = -self.vy
            self.ay = -self.ay
        
        print(self.x)
        self.draw()
        self.avec = pyArrow.draw_arrow(sc, pygame.Vector2(self.x, self.y), pygame.Vector2(self.x+self.ax*1000, self.y+self.ay*1000), "white")
        

        




pygame.font.init()
solarSystem = []

# for i in range(10):
#     solarSystem.append(Planet(random.randint(0, screenWidth), random.randint(0, screenHeight), 0, 0, 0, 0, pSize, random.choice(["red", "blue", "green", "yellow"])))


pygame.font.init()
solarSystem = []

def dist(x, y, x2, y2):
    return ((x2-x)**2 + (y2-y)**2)**0.5


font = pygame.font.SysFont(None, 36)
stack = []
m = 5
accCon = 3


colors = [
    'red',
    'green',
    'blue',
    'cyan',
    'magenta',
    'yellow',
    'orange',
    'purple',
    'brown',
    'pink',
]


for i in range(10):
    solarSystem.append(Planet(random.randint(0, screenWidth), random.randint(0, screenHeight), 0, 0, 0, 0, pSize, random.choice(colors), random.randint(1,3)))
    
while True:

    sc.fill("#2e3440")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    

    

    mouseCoords = list(pygame.mouse.get_pos())


    if mouseCoords[0] == 0 or mouseCoords[1] == 0 or mouseCoords[0] == screenWidth-1 or mouseCoords[1] == screenHeight-1:
        mouseCoords[0] = x
        mouseCoords[1] = y

    # mVec = pyArrow.draw_arrow(sc, pygame.Vector2(x,y), pygame.Vector2(mouseCoords[0], mouseCoords[1]), "red")
    
    for i in solarSystem:
        i.update(dt)



    texts = [
        # font.render(f"pos: {x:.1f},{y:.1f}", True, "#cedee9"),
        # font.render(f"vel: {vx:.1f}, {vy:.1f}", True, "#cedee9"),
        # font.render(f"acc: {ax:.2f}, {ay:.2f}", True, "#cedee9"),
        # font.render(f"dst: {(aVector[0]):.1f}, {(aVector[1]):.1f}", True, "#cedee9"),
        # # font.render(f"crd: {round(mouseCoords[0])}, {round(mouseCoords[1])}", True, "white"),
    ]
    for index, t in enumerate(texts):
        sc.blit(t, (10, 20*index))    
    
    pygame.display.flip()


    dt = clock.tick(60)/1000  
    