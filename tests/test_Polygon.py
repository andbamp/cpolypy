from cpolypy import Polygon
from numpy import genfromtxt

def test_Polygon_no_params():
  poly = Polygon()
  assert poly.__str__() == "Polygon composed of points: []"

def test_Polygon_with_points_array():
  chull_points = genfromtxt('tests/data/chull_points.csv', delimiter=',')
  poly = Polygon(chull_points)
  assert poly.__str__() == \
    'Polygon composed of points: [[-1.19, -2.08], [1.53, -1.53], '\
    '[0.88, 1.53], [0.44, 1.88], [-2.49, -0.55]]'
