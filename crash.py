from game import *

image_crash = image('public/assets/img/crash.png')

def crash(c):
    c.x += c.vx
    c.y += c.vy
    c.r += 0.02
    c.sx *= c.vs
    c.sy *= c.vs
    if c.sx < 0.01:
        c.life = 0


def new_crash(x, y, v, n, vs):
    for i in range(n):
        rad = i/n*math.pi*2
        vx = math.cos(rad)*v
        vy = math.sin(rad)*v
        add(crash, image_crash, 0.04, x, y, vx, vy, vs=vs)
