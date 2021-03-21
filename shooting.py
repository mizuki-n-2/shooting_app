from game import *

img_player = image('public/assets/img/airplane.png')
img_shot = image('public/assets/img/shot.png')

SW, SH = 1, 9/16

def player(p):
  v = 0.025
  if key(LEFT):
    p.x -= v
  if key(RIGHT):
    p.x += v
  if key(UP):
    p.y += v
  if key(DOWN):
    p.y -= v
  p.x = max(-SW+p.sx, min(SW-p.sx, p.x))
  p.y = max(-SH + p.sy, min(SH - p.sy, p.y))

  if key(X):
    new_shot(p.x, p.y, 0.05)

def new_shot(x, y, v):  
  add(shot, img_shot, 0.05, x, y, 0, v)

def shot(s):
  s.x += s.vx
  s.y += s.vy

def start():
  print("Hello World")

  score()
  size = 0.1
  add(player, img_player, size, 0, -9 / 16)

run(start)
