import pyautogui as pg
import time
import random


#mappa corn -52,8



def checkImage(img, conf=0.8, pause = 1.5, y_offset = 25, imageOffset =18): #25,18 riso per il risoa ggiungere anche +2 alle x, 0, 25 il resto
  try:
    pos = pg.locateOnScreen(img, confidence=conf)
    if pos:
      pg.moveTo(pos[0]+imageOffset + 2,(pos[1]+imageOffset)+y_offset)
      pg.click()
      time.sleep(pause)
      return True
    else:
      return False
  except:
    pass

def move_middle(res_x = 1900, res_y = 1000):
  pg.moveTo(res_x/2 + random.uniform(0,60), res_y/2 + random.uniform(0,80))
  pg.click()

def move_up(res_x = 1900):
  pg.moveTo(res_x/2 + random.uniform(0,300), random.uniform(0,2))
  pg.click()

def move_right(res_x = 1900, res_y = 1000):
  pg.moveTo(res_x - random.uniform(10,100), res_y/2 + random.uniform(0,200))
  pg.click()

def move_left(res_x = 1900, res_y = 1000):
  pg.moveTo(random.uniform(10,100), res_y/2 + random.uniform(0,200))
  pg.click()

def move_down(res_x = 1900, res_y = 1080, bar = 125):
  grandezza_barra = bar
  #add random
  bar += random.uniform(0,2.5)
  pg.moveTo(res_x/2 + random.uniform(0,300), res_y-grandezza_barra)
  pg.click()


def checkRice(conf = 0.75, pause = 1.5):
  try:
    if checkImage('./rice_1.png', conf = conf, pause=pause):
      return True
    if checkImage('./rice_2.png', conf = conf, pause=pause):
      return True
    checkImage('./rice_3.png', conf = conf, pause=pause)
  except:
    pass

def checkhop(conf = 0.6, pause = 1.5):
  try:
    checkImage('./hop_1.png', conf, pause=pause)
    checkImage('./hop_2.png', conf, pause=pause)
    checkImage('./hop_3.png', conf, pause=pause)
    checkImage('./hop_4.png', conf, pause=pause)
  except:
    pass


def checkbarley(conf = 0.6, pause = 1.5):
  try:
    checkImage('./barley_1.png', conf, pause=pause)
    checkImage('./barley_2.png', conf, pause=pause)
    checkImage('./barley_3.png', conf, pause=pause)
    checkImage('./barley_4.png', conf, pause=pause)
  except:
    pass


def checkoat(conf = 0.6, pause = 1.5):
  try:
    checkImage('./oat_1.png', conf, pause=pause)
    checkImage('./oat_2.png', conf, pause=pause)
    checkImage('./oat_3.png', conf, pause=pause)
  except:
    pass

def checkrye(conf = 0.6, pause = 1.5):
  try:
    checkImage('./rye_1.png', conf, pause=pause)
    checkImage('./rye_2.png', conf, pause=pause)
    checkImage('./rye_3.png', conf, pause=pause)
  except:
    pass

def checkflax(conf = 0.6, pause = 1.5):
  try:
    checkImage('./flax_1.png', conf, pause=pause)
    checkImage('./flax_2.png', conf, pause=pause)
    checkImage('./flax_3.png', conf, pause=pause)
    checkImage('./flax_4.png', conf, pause=pause)
    checkImage('./flax_5.png', conf, pause=pause)
  except:
    pass

    

def checkhemp(conf = 0.6, pause = 1.5):
  try:
    checkImage('./hemp_1.png', conf, pause=pause)
    checkImage('./hemp_2.png', conf, pause=pause)
    checkImage('./hemp_3.png', conf, pause=pause)
    checkImage('./hemp_4.png', conf, pause=pause)
    checkImage('./hemp_5.png', conf, pause=pause)
  except:
      pass
  
def checkcorn(conf = 0.6, pause = 1.2):
  try:
    checkImage('./corn_1.png', conf, pause=pause)
    checkImage('./corn_2.png', conf, pause=pause)
    checkImage('./corn_3.png', conf, pause=pause)
    checkImage('./corn_4.png', conf, pause=pause)
    checkImage('./corn_5.png', conf, pause=pause)
    checkImage('./corn_6.png', conf, pause=pause)
    checkImage('./corn_7.png', conf, pause=pause)
    checkImage('./corn_8.png', conf, pause=pause)
    checkImage('./corn_9.png', conf, pause=pause)
    checkImage('./corn_10.png', conf, pause=pause)
    checkImage('./corn_11.png', conf, pause=pause)
    checkImage('./corn_12.png', conf, pause=pause)
    checkImage('./corn_13.png', conf, pause=pause)
    checkImage('./corn_14.png', conf, pause=pause)
    checkImage('./corn_15.png', conf, pause=pause)

  except:
      pass


def corn_routine():
  while True:
    checkcorn(conf = 0.7) # ottimo su mappa con i due campi [-52, 8]

#al posto di mettere comandi up down ecc, cecheckare le coord con immagini e poi spostarsi di conseguenza.
def rice_dinamic_routine():
  indication = 'right'
  start = time.time()
  seconds = 0
  while True:
    seconds += time.time()- start
    if (not checkRice()) and seconds > random.uniform(1, 5) and indication == 'right':
      move_right()
      start = time.time()
      seconds = 0
      indication = 'down'
    elif (not checkRice()) and seconds > random.uniform(1, 5) and indication == 'down':
      move_down()
      start = time.time()
      seconds = 0
      indication = 'left'
    elif(not checkRice()) and seconds > random.uniform(1, 5) and indication == 'left':
      move_left()
      start = time.time()
      seconds = 0
      indication = 'up'
    elif(not checkRice()) and seconds > random.uniform(1, 5) and indication == 'up':
      move_up()
      start = time.time()
      seconds = 0
      indication = 'right'
    else:
      if checkRice(): #se lo trova stai nella mappa
        start = time.time()
        seconds = 0

def rice_static_routine(): #perfetto per [20, -26]
  start = time.time()
  seconds = 0
  while True:
    seconds += time.time()- start
    if (not checkRice()) and seconds > random.uniform(120, 160):
      checkImage('middle_rice.png', conf=0.95)
      start = time.time()
      seconds = 0
    else:
      checkRice()

#rice_dinamic_routine()
rice_static_routine()
#corn_routine
  
#checkhemp()
#checkhop()
#checkoat()
#checkrye()
#checkflax()
#checkbarley()
#checkRice()