
from PIL import Image
import math
from random import shuffle

BLACK = (0,0,0)
BLUE  = (0,0,255)
RED   = (255,0,0)


def main(d1, d2, c1, c2, ext):
  #torus generation
  img_width = 150
  img_height = 150
  rad = 42  # radius
  thi = 8   # thickness
  den = d1  # density
  dist = d2 # distance between half-moons in pixels. up to 50
  top_color = c1
  bot_color = c2
  out_filename = "dm"
  ext_filename = ext
  
  torus = list()
  
  # generate coordinate list of all points within torus
  for x in range(img_width):
    for y in range(img_height):
      c_sqr = (x - rad - thi)**2 + (y - rad - thi)**2 # hypotenuse squared
      if (rad - thi)**2 <= c_sqr and c_sqr <= (rad + thi)**2:
        torus.append((x,y))
    
  # randomly select amount of points based on density value: den
  shuffle(torus)
  torus = torus[:int(len(torus)*den)]
  
  # create img and pixel map
  img = Image.new( 'RGB', (img_height,img_width), "white")
  pixels = img.load()
  
  for i, j in torus:
    color = top_color
    if j > rad + thi:
      i += rad
      j += dist
      color = bot_color
    
    pixels[i,j] = color
    
  img.save(out_filename + str(dist) + ext_filename + ".png", "PNG")
  print "Image saved as " + out_filename + str(dist) + ext_filename + ".png"
  
  
  
  
  
  
if __name__ == "__main__":
  d1 = d2 = c1 = c2 = ext = 0
  
  while True:
    usr = raw_input("Pixel density [float between 0 and 1]: ")
    try:
      d1 = float(usr)
      break
    except ValueError:
      print "Error: Input a float between 0 and 1."
  while True:
    usr = raw_input("Distance [int between 0 and 50]: ")
    try:
      d2 = int(usr)
      break
    except ValueError:
      print "Error: Input an integer between 0 and 50."
  while True:
    usr = raw_input("Coloring ([s]olution / [b]lack): ")
    if usr == 's':
      c1 = RED
      c2 = BLUE
      ext = "_solution"
      print ext
      break
    elif usr == 'b':
      c1 = BLACK
      c2 = BLACK
      ext = ""
      break
    else:
      print "Error: Input either 's' or 'b'."
      
  main(d1,d2,c1,c2,ext)
  
