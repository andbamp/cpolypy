import numpy as np

class Polygon():
  
  def __init__(self, vertices):
    self.vertices = vertices
  
  def __str__(self):
    return "Polygon composed of points: {}".format(self.vertices.tolist())
  
  def edges(self):
    return(np.roll(self.vertices, -1, axis = 0) - self.vertices)
