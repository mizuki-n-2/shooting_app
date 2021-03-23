# 各種機能の読み込み
from game import *
from crash import *
import math
import random

# 画像の読み込み
img_player = image("public/assets/img/airplane.png")
img_enemy = image("public/assets/img/ghost.png")
img_shot = image("public/assets/img/shot.png")

# 画面のサイズ
SW, SH = 1, 9 / 16

# 自機の処理
def player(p):

  # 自機の速さ
  v = 0.025

  # 自機の移動
  if key(LEFT):
    p.x -= v
  if key(RIGHT):
    p.x += v
  if key(DOWN):
    p.y -= v
  if key(UP):
    p.y += v

  # 移動可能範囲の制限
  p.x = max(-SW+p.sx, min(SW-p.sx, p.x))
  p.y = max(-SW+p.sy, min(SW-p.sy, p.y))

  # 自機と敵の衝突判定
  for e in group(enemy):

    # 自機と敵の距離
    d = math.dist((p.x, p.y), (e.x, e.y))

    if d < e.sy:

      # 爆発の生成
      new_crash(p.x, p.y, 0.01, 20, 0.98)

      # 自機を消去
      p.life = 0

  # タイムから1を減算する
  p.time -= 1

  if key(Z) and p.time <= 0:
    # ショットの発射
    new_shot(p.x, p.y, 0.05, 0, 3, 0.04)

    # 待ち時間
    p.time = 3
  
  elif key(X):
    # レーザーの発射
    add(laser, img_shot, 0.05, p.x, p.y, 0, 0.07)

# 敵の処理
def enemy(e):
  
  # 敵の移動
  e.x += e.vx
  e.y += e.vy

  # 敵の回転
  e.r = 0.01

  # 敵とショットの衝突判定
  for s in group(shot, laser):

    # 敵とショットの距離
    d = math.dist((e.x, e.y), (s.x, s.y))

    if d < e.sx * 2:
      
      # 敵にダメージ
      e.life -= s.life

      # ショットを消去
      s.life = 0

  # 敵のライフが0以下なら爆発を生成
  if e.life <= 0:

    new_crash(e.x, e.y, 0.01, 20, 0.95)
    score(1)

  # 敵が画面外に出たら消去
  if abs(e.x) > SW + e.sx or abs(e.y) > SH + e.sy:
    
    e.life = 0

# ショットの発射
def new_shot(x, y, v, dir, n, angle):

  for i in range(n):

    # nが1より大きいとき、扇状に発射
    if n > 1:
      r = (dir + angle / (n - 1) * (i - (n - 1) / 2))
    else:
      r = dir
    
    # 方向rをラジアンに変換
    rad = r * math.pi * 2
    
    # ショットの速度
    vx = math.sin(rad)*v
    vy = math.cos(rad) * v
    
    # ショットの生成
    add(shot, img_shot, 0.05, x, y, vx, vy, r=r)

# ショットの処理
def shot(s):

  # ショットの移動
  s.x += s.vx
  s.y += s.vy

  # 画面外に出たら消去
  if abs(s.x) > SW + s.sx or abs(s.y) > SH + s.sy:
    s.life = 0

# レーザーの処理
def laser(l):
    # レーザーの移動
    l.y += l.vy

    # 画面外に出たら消去
    if abs(l.x) > SW+l.sx or abs(l.y) > SH+l.sx:
        l.life = 0

# ステージの処理
def stage(s):
  
  # 敵の生成
  if random.random() < 0.025+0.0005 * score():
    
    # 敵のサイズ
    size = 0.075

    # 敵の座標
    x = random.uniform(-SW + size, SW - size)
    y = SH+size

    # 敵の生成
    add(enemy, img_enemy, size, x, y, 0, -0.005, life=10)

# ゲームの開始
def start():
  # スコア表示
  score()

  # サイズ指定
  size = 0.08

  # 自機の生成
  add(player, img_player, size, 0, -0.5)

  # ステージの作成
  add(stage)

# ゲーム実行
run(start)
