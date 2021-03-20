from game import *

img_player = image('public/assets/img/airplane.png')

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
  p.y = max(-SH+p.sy, min(SH-p.sy, p.y))

def start():
  print("Hello World")
  add(player, img_player)

run(start)
