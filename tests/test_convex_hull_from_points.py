from cpolypy import convex_hull_from_points, Polygon
import numpy as np

def test_convex_hull_from_points():
  point_cloud = np.genfromtxt('tests/data/point_cloud.csv', delimiter=',')
  chull = convex_hull_from_points(point_cloud)
  chull_points = np.genfromtxt('tests/data/chull_points.csv', delimiter=',')
  poly = Polygon(chull_points)
  assert chull.__str__() == poly.__str__()

def test_convex_hull_from_points_colinear():
  point_cloud = np.array([[0,0], [1,2], [1,3], [2,1], [2,2], [3,1]])
  chull = convex_hull_from_points(point_cloud)
  chull_points = np.array([[0,0], [3,1], [2,2], [1,3]])
  poly = Polygon(chull_points)
  assert chull.__str__() == poly.__str__()

def test_convex_hull_from_points_triangle():
  point_cloud = points = np.array([[0,-1], [2,1], [1,2]])
  chull = convex_hull_from_points(point_cloud)
  poly = Polygon(point_cloud)
  assert chull.__str__() == poly.__str__()
