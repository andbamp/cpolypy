import numpy as np

def angle_with_horizontal(p1, p2):
  return np.arctan2(p2[1] - p1[1], p2[0] - p1[0])

def clockwise_turn(p1, p2, p3):
  return np.cross(p2-p1, p3-p1) < 0
