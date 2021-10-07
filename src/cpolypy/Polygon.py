import numpy as np

class Polygon():
  
  def __init__(self, vertices = None):
    if vertices is None:
      self.vertices = np.empty(shape = 0)
    else:
      self.vertices = vertices
  
  def __str__(self):
    return "Polygon composed of points: {}".format(self.vertices.tolist())
  
  def edges(self):
    return((vertices[:-1] - vertices[1:]).T)
