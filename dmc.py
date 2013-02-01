
from PIL import Image
from neuron import Neuron

BLACK = (0,0,0)
BLUE  = (0,0,255)
RED   = (255,0,0)

TOP = 1
BOT = 0


def main(train, test, out):
  
  TRAIN_FILE = train
  TEST_FILE  = test
  OUT_FILE   = out
  
  img = Image.open(TRAIN_FILE) # read double moons image from .png file
  pixels = img.load()          # generate pixel map
  width = img.size[0]
  height = img.size[1]
  
  training_set = dict()
  
  for i in range(width):
    for j in range(height):
      if pixels[i,j] == BLUE:   # if pixel is blue
        training_set[i,j] = BOT # set value to bottom
      elif pixels[i,j] == RED:  # if pixel is red
        training_set[i,j] = TOP # set value to top
  
  
  # create neuron with 2 input nodes
  n = Neuron(2) # x-input, y-input
  print "Neuron created."
  # training
  print "Training..."
  counter = 0
  while True:
    errors = 0
    for p in training_set:
      errors += n.train_step(p, training_set[p])
      counter += 1
      print "====="
      
    if errors < n.get_margin() * len(training_set):
      break
  
  print "Length of training set: " + str(len(training_set))
  print "Iterations: " + str(counter)
  
  # test cases
  img = Image.open(TEST_FILE)
  pixels = img.load()
  width = img.size[0]
  height = img.size[1]
  
  for i in range(width):
    for j in range(height):
      if pixels[i,j] == BLACK:
        n.set_input(0, i)
        n.set_input(1, j)
        n.activate()
        ans = n.get_output()
        if ans == TOP:
          pixels[i,j] = RED
        elif ans == BOT:
          pixels[i,j] = BLUE
  
  img.save(OUT_FILE, "PNG")
  
  
  
  
  
if __name__ == "__main__":
  main(raw_input("Training filename : "),
       raw_input("Test filename (black) : "),
       raw_input("Output filename (to be created) : "))
