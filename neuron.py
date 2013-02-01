
import random


class Neuron(object):
  """
    Simulates a simple neural network.
    
    Attributes:
    self.threshold  : when total input exceeds threshold, output is on
    self.inputs     : a list of inputs
    self.weights    : a list of weights
    self.output     : the float representation of the output
    self.l_rate     : learning rate
    self.err_margin : amount of allowable error
  """
  
  def __init__(self, width):
    self.threshold = 1
    self.inputs = [0] * width
    self.weights = [1] * width
    self.l_rate = 0.1
    self.err_margin = 0.1
  
  def __str__(self):
    out = "Weights: " + str(self.weights) + "\n"
    out += "Inputs: " + str(self.inputs) + "\n"
    out += "Threshold: " + str(self.threshold) + "\n"
    out += "Learning rate: " + str(self.l_rate) + "\n"
    out += "Error margin: " + str(self.err_margin) + "\n"
    return out
  
  def append(self, i, w):
    self.inputs.append(i)
    self.weights.append(w) 
  
  def set_input(self, x, i): self.inputs[x] = i
  def get_input(self, x): return self.inputs[x]
  
  def set_weight(self, x, w): self.weights[x] = w
  def get_weight(self, x): return self.weights[x]
  
  def get_value(self, x): return self.weights[x] * self.inputs[x]
  
  def set_threshold(self, t): self.threshold = t
  def get_threshold(self): return self.threshold
  
  def set_rate(self, r): self.l_rate = r
  def get_rate(self): return self.l_rate
  
  def set_margin(self, em): self.err_margin = em
  def get_margin(self): return self.err_margin
  
  def activate(self):
    """
      sets self.output
      returns error
    """
    i_sum = 0.0
    for x in range(len(self.inputs)):
      i_sum += self.inputs[x] * self.weights[x]
    if i_sum > self.threshold:
      self.output = 1.0
    else:
      self.output = 0.0
    
    
    
  def get_output(self):
    return self.output
  
  def print_output(self):
    print "Output: %.1f" %self.output

  def train_step(self, ins, exp_out):
    """
      Neuron will adjust its weights according to the test data
      PARAMS :
        ins     : list of inputs (will only accept enough to fill input layer)
        exp_out : expected output
      RETURN :
        0 : no errors
        1 : error found
    """
    # feed inputs
    for x in range(len(self.inputs)):
      self.inputs[x] = ins[x]
      print "Taking input %i: %.1f" %(x+1, ins[x])
      print "Value: %f" %self.get_value(x)
    
    
    # perform activation
    self.activate()
    det_out = self.output # determined output
    print "My guess: %.1f" %det_out
    print "The expected output: %.1f" %exp_out
    
    # if output is not correct, calculate error
    error = 0
    error_rate = 0
    if det_out != exp_out:
      error = exp_out - det_out
      print "Error: %f" %error
      # adjust weights
      for x in range(len(self.inputs)):
        self.weights[x] += self.l_rate * error * self.inputs[x]
        print "New weight %i: %f" %(x+1,self.weights[x])
      
      self.threshold -= self.l_rate * error
      print "New threshold: %f" %self.threshold
      return 1 # return 1 for error
    else:
      print "Correct!"
      return 0 # return 0 for no errors
