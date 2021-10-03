import numpy as np
from cpolypy.Polygon import Polygon

def convex_hull_from_points(points):
  chull = Polygon()
  return(chull)

def angle_with_horizontal(p1, p2):
  return np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
