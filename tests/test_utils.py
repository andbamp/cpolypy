from cpolypy import angle_with_horizontal
import numpy as np

def test_angle_with_horizontal_q1():
  p1 = np.array([0,0])
  p2 = np.array([1,1])
  angle = np.degrees(angle_with_horizontal(p1, p2))
  assert angle == 45

def test_angle_with_horizontal_q2():
  p1 = np.array([0,0])
  p2 = np.array([-1,1])
  angle = np.degrees(angle_with_horizontal(p1, p2))
  assert angle == 135

def test_angle_with_horizontal_q3():
  p1 = np.array([0,0])
  p2 = np.array([-1,-1])
  angle = np.degrees(angle_with_horizontal(p1, p2))
  assert angle == -135

def test_angle_with_horizontal_q4():
  p1 = np.array([0,0])
  p2 = np.array([1,-1])
  angle = np.degrees(angle_with_horizontal(p1, p2))
  assert angle == -45

def test_angle_with_horizontal_0():
  p1 = np.array([0,0])
  p2 = np.array([0,0])
  angle = np.degrees(angle_with_horizontal(p1, p2))
  assert angle == 0
