try:
    import pygame
    import pendulum_movement as pm
    from math import pi, radians
except Exception:
    print("You are either missing one or more files or they are not in same directory")

pygame.init()
a1, a2 = 1440, 1280                     #PROVIDE THE DISPLAY CONFIGURATION HERE
x_offset, y_offset = a1 // 2, a2 // 2
p_c = dict()
running = True


def run(p):
    #PROVIDE THE PENDULUM ROD COLOR IN THE SECOND ARGUEMENT IN RGB[R, G, B] FORM
    pygame.draw.line(screen, (255, 255, 255), (x_offset, y_offset), (x_offset + (x1:=p.movement()[0]), y_offset - (y1:=p.movement()[1])))
    #PROVIDE THE PENDULUM BOB COLOR IN THE SECOND ARGUEMENT IN RGB{R, G, B} FORM
    pygame.draw.circle(screen, (255, 255, 255), (x_offset + x1, y_offset - y1), p.mass * 3)

try:
        
    n = int(input("number of pendulums: "))

    for i in range(n):
        print(f"\nFor pendulum {i + 1}\n")
        theta = radians(float(input("enter start angle[in degrees]: ")))
        mass = float(input("enter mass[in kg and try to keep it small within 5]: "))
        length = float(input("enter length[in m and same thing try keeping small < 3.5]: ")) * 100
        p_c[i] = pm.pendulum(length, mass, theta)
    print("to quit just close the window or press ESC.")

    screen = pygame.display.set_mode([a1, a2])
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    running = False
        screen.fill((0, 0, 0)) #PROVIDE SCREEN BACKGROUND COLOR HERE IN RGB[R, G, B} FORM
        pygame.display.set_caption('Simple Pendulum')
        for i in p_c:
            run(p_c[i])
        pygame.display.update()
        pygame.time.delay(13)

    print("Thank You for trying out my Simple Pendulum project... Will upload double pendulum too so stay tuned")
except Exception as e:
        print(e)
        pygame.display.quit()
        pygame.quit()
        running = False    

