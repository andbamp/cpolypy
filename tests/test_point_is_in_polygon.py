from cpolypy import point_is_in_polygon, Polygon
import numpy as np

def test_point_is_in_polygon_inside():
  points = np.array([[-1,-2], [1,-1], [0,2], [-2, -1]])
  cpoly = Polygon(points)
  point = np.array([0, 0.5])
  assert point_is_in_polygon(point, cpoly) == True

def test_point_is_in_polygon_outside():
  points = np.array([[-1,-2], [1,-1], [0,2], [-2, -1]])
  cpoly = Polygon(points)
  point = np.array([1000, 1000])
  assert point_is_in_polygon(point, cpoly) == False

def test_point_is_in_polygon_on():
  points = np.array([[-1,-2], [1,-1], [0,2], [-2, -1]])
  cpoly = Polygon(points)
  point = np.array([-1, -2])
  assert point_is_in_polygon(point, cpoly) == True

def test_point_is_in_polygon_colinear():
  points = np.array([[-1,-2], [1,-1], [0,2], [-2, -1]])
  cpoly = Polygon(points)
  point = np.array([-1.5, -1.5])
  assert point_is_in_polygon(point, cpoly) == True
