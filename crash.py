from game import *

img_crash = image('public/assets/img/crash.png')

def crash(c):
    c.x += c.vx
    c.y += c.vy
    c.r += 0.02
    c.sx *= c.vs
    c.sy *= c.vs
    if c.sy < 0.01:
        c.life = 0


def new_crash(x, y, v, n, vs):
    for i in range(n):
        rad = i/n*math.pi*2
        vx = math.sin(rad)*v
        vy = math.cos(rad)*v
        add(crash, img_crash, 0.04, x, y, vx, vy, vs=vs)
