from cpolypy import Polygon
import numpy as np

def test_Polygon_with_points_array():
  chull_points = np.genfromtxt('tests/data/chull_points.csv', delimiter=',')
  poly = Polygon(chull_points)
  assert poly.__str__() == \
    'Polygon composed of points: [[-1.19, -2.08], [1.53, -1.53], '\
    '[0.88, 1.53], [0.44, 1.88], [-2.49, -0.55]]'

def test_Polygon_edges():
  points = np.array([[-1,-2], [1,-1], [0,2], [-2, -1]])
  poly = Polygon(points)
  assert np.array_equal(poly.edges(), np.array([[2,1], [-1,3], [-2,-3], [1, -1]]))
