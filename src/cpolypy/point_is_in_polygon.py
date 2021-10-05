from cpolypy.utils import clockwise_turn
import numpy as np

def point_is_in_polygon(point, cpoly):
  points = np.array([*cpoly.points, cpoly.points[0]])
  for i in range(len(cpoly.points)):
    if(clockwise_turn(points[i], points[i+1], point)):
      return False
  return True
