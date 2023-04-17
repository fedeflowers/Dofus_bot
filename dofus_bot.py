import pyautogui as pg
import time
import random


#mappa corn -52,8

path = './immagini/'

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

def find_image(img, conf = 0.8):
  try:
    pos = pg.locateOnScreen(img, confidence=conf)
    if pos:
      return (True, pos)
    else:
      return (False, pos)
  except:
    pass

def click_pos(pos, pause = 1.5, y_offset = 0, x_offset = 0, imageOffset =25):
  pg.moveTo((pos[0]+imageOffset) + x_offset,(pos[1]+imageOffset)+y_offset)
  pg.click()
  time.sleep(pause)

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


def checkRice(conf = 0.75):
  try:
    t, pos = find_image(path + 'rice_1.png', conf = conf)
    if t:
      #click_pos(pos, pause=pause, y_offset=25, x_offset = 2, imageOffset= 18)
      return (True, pos)
    t, pos = find_image(path + 'rice_2.png', conf = conf)
    if t:
      #click_pos(pos, pause=pause, y_offset=25, x_offset = 2, imageOffset= 18)
      return (True, pos)
    t, pos = find_image(path + 'rice_3.png', conf = conf)
    if t:
      #click_pos(pos, pause=pause, y_offset=25, x_offset = 2, imageOffset= 18)
      return (True, pos)
    t, pos = find_image(path + 'rice_4.png', conf = conf)
    if t:
      #click_pos(pos, pause=pause, y_offset=25, x_offset = 2, imageOffset= 18)
      return (True, pos)
    
    return(False, None)
  except:
    pass

def checkhop(conf = 0.6, pause = 1.5):
  try:
    checkImage(path + 'hop_1.png', conf, pause=pause)
    checkImage(path + 'hop_2.png', conf, pause=pause)
    checkImage(path + 'hop_3.png', conf, pause=pause)
    checkImage(path + 'hop_4.png', conf, pause=pause)
  except:
    pass


def checkbarley(conf = 0.6, pause = 1.5):
  try:
    checkImage(path + 'barley_1.png', conf, pause=pause)
    checkImage(path + 'barley_2.png', conf, pause=pause)
    checkImage(path + 'barley_3.png', conf, pause=pause)
    checkImage(path + 'barley_4.png', conf, pause=pause)
  except:
    pass


def checkoat(conf = 0.6, pause = 1.5):
  try:
    checkImage(path + 'oat_1.png', conf, pause=pause)
    checkImage(path + 'oat_2.png', conf, pause=pause)
    checkImage(path + 'oat_3.png', conf, pause=pause)
  except:
    pass

def checkrye(conf = 0.6, pause = 1.5):
  try:
    checkImage(path + 'rye_1.png', conf, pause=pause)
    checkImage(path + 'rye_2.png', conf, pause=pause)
    checkImage(path + 'rye_3.png', conf, pause=pause)
  except:
    pass

def checkflax(conf = 0.6, pause = 1.5):
  try:
    checkImage(path + 'flax_1.png', conf, pause=pause)
    checkImage(path + 'flax_2.png', conf, pause=pause)
    checkImage(path + 'flax_3.png', conf, pause=pause)
    checkImage(path + 'flax_4.png', conf, pause=pause)
    checkImage(path + 'flax_5.png', conf, pause=pause)
  except:
    pass

    

def checkhemp(conf = 0.6, pause = 1.5):
  try:
    checkImage(path + 'hemp_1.png', conf, pause=pause)
    checkImage(path + 'hemp_2.png', conf, pause=pause)
    checkImage(path + 'hemp_3.png', conf, pause=pause)
    checkImage(path + 'hemp_4.png', conf, pause=pause)
    checkImage(path + 'hemp_5.png', conf, pause=pause)
  except:
      pass
  
  #un pò lento
def checkcorn(conf = 0.6):
  try:
    t, pos = find_image(path + 'corn_1.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_2.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_3.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_4.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_5.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_6.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_7.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_8.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_9.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_10.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_11.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_12.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_13.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_14.png', conf = conf)
    if t:
      return (True, pos)
    t, pos = find_image(path + 'corn_15.png', conf = conf)
    if t:
      return (True, pos)
    return(False, None)
  except:
    pass




#al posto di mettere comandi up down ecc, cecheckare le coord con immagini e poi spostarsi di conseguenza.
def rice_dinamic_routine():
  start = time.time()
  seconds = 0
  save_pos = []
  while True:
    seconds += time.time()- start
    t, pos = checkRice(conf=0.85)
    if (not t) and seconds > random.uniform(1, 3) and find_image(path + 'rice_right.png',conf=0.95)[0]:
      move_right()
      start = time.time()
      seconds = 0
    elif (not t) and seconds > random.uniform(1, 3) and find_image(path + 'rice_down.png',conf=0.95)[0]:
      move_down()
      start = time.time()
      seconds = 0
    elif(not t) and seconds > random.uniform(1, 3) and find_image(path + 'rice_left.png',conf=0.95)[0]:
      move_left()
      start = time.time()
      seconds = 0
    elif(not t) and seconds > random.uniform(1, 3) and find_image(path + 'rice_up.png',conf=0.95)[0]:
      move_up()
      start = time.time()
      seconds = 0
    else:
      if t: #se lo trova stai nella mappa
        start = time.time()
        seconds = 0
        if pos not in save_pos:
          click_pos(pos, pause=1.9, y_offset=25, x_offset = 2, imageOffset= 18)
          save_pos.append(pos)
          #print(save_pos)
          if len(save_pos) > 3:
            save_pos.pop(0)

def static_routine( middle_img, check_resource, pause = 1.5, y_offset = 0, x_offset = 0, imageOffset = 25): #perfetto per [20, -26]
  start = time.time()
  save_pos = []
  seconds = 0
  while True:
    seconds += time.time()- start
    t, pos = check_resource(conf=0.85)
    if (not t) and seconds > random.uniform(120, 160):
      bool, pos = find_image(path + middle_img, conf=0.95)
      if bool:
        click_pos(pos)
      start = time.time()
      seconds = 0
    elif pos is not None:
      if pos not in save_pos:
        click_pos(pos, pause=pause, y_offset=y_offset, x_offset = x_offset, imageOffset= imageOffset)
        save_pos.append(pos)
        #print(save_pos)
        if len(save_pos) > 4:
          save_pos.pop(0)



      

#rice_dinamic_routine()
static_routine('middle_rice.png', checkRice, y_offset=25, x_offset=2, imageOffset=18) #rice
#static_routine('middle_corn.png', checkcorn, y_offset=0, x_offset=0, imageOffset=25) # ottimo su mappa con i due campi [-52, 8]
#rice_dinamic_routine()
#checkhemp()
#checkhop()
#checkoat()
#checkrye()
#checkflax()
#checkbarley()
#checkRice()
