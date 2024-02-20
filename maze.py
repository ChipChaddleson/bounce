import pygame 
screenWidth, screenHeight = 500, 500
res = (screenWidth, screenHeight)
dt = 0
sc = pygame.display.set_mode(res)
clock = pygame.time.Clock()
pSize = 10
x, y = screenWidth/2, screenHeight/2
vx, vy = 0, 0 
ax, ay = 0, 0 
pygame.font.init()


font = pygame.font.SysFont(None, 36)
stack = []
m = 5
colors = ["red", "blue", "green", "yellow"]
while True:

    sc.fill("#2e3440")

    tx, ty = x, y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    

    for i, ob in enumerate(stack):
        pygame.draw.circle(sc, f"#88{i}cd0", ob, pSize)
    
    if len(stack) > 9:
        stack.pop(0)
    


    pygame.draw.circle(sc, "#88c0d0", (x, y), pSize)


    mouseCoords = list(pygame.mouse.get_pos())
    if mouseCoords[0] == 0 or mouseCoords[1] == 0 or mouseCoords[0] == screenWidth-1 or mouseCoords[1] == screenHeight-1:
        mouseCoords[0] = x
        mouseCoords[1] = y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or (mouseCoords[1] < y):
        ay -= 0.3 * dt
    if keys[pygame.K_s] or (mouseCoords[1] > y):
        ay += 0.3 * dt
    if keys[pygame.K_a] or (mouseCoords[0] < x):
        ax -= 0.3 * dt
    if keys[pygame.K_d] or (mouseCoords[0] > x):
        ax += 0.3 * dt

    
    # if ax >= m*dt:
    #     ax = m*dt
    # if ax <= -m*dt:
    #     ax = -m*dt
    # if ay >= m*dt:
    #     ay = m*dt
    # if ay <= -m*dt:
    #     ay = -m*dt

    # friction
    ax = ax - ax*0.04
    ay = ay - ay*0.04
    vx = vx - vx*0.04
    vy = vy - vy*0.04
    
    
    
    vx = vx + ax
    x = x + vx

    vy = vy + ay
    y = y + vy

    if x >= screenWidth-pSize:
        x = tx
        vx = -vx
        ax = -ax
    if x <= pSize:
        x = tx
        vx = -vx
        ax = -ax
    if y >= screenHeight-pSize:
        y = ty
        vy = -vy
        ay = -ay
    if y <= pSize:
        y = ty
        vy = -vy
        ay = -ay

    texts = [
        font.render(f"pos: {x:.1f},{y:.1f}", True, "#cedee9"),
        font.render(f"vel: {vx:.1f}, {vy:.1f}", True, "#cedee9"),
        font.render(f"acc: {ax:.2f}, {ay:.2f}", True, "#cedee9"),
        # font.render(f"crd: {round(mouseCoords[0])}, {round(mouseCoords[1])}", True, "white"),
    ]
    for index, t in enumerate(texts):
        sc.blit(t, (10, 20*index))    
    
    pygame.display.flip()
    stack.append((x,y))


    dt = clock.tick(60)/1000  
    