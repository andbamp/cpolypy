from cpolypy import do_intersect, Polygon
import numpy as np

def test_do_intersect():
  cpoly_1 = Polygon(np.array([[4,0], [5,2], [2,6], [1,1]]))
  cpoly_2 = Polygon(np.array([[5.5,1], [6,4], [5,5], [4,2]]))
  intersection = do_intersect(cpoly_1, cpoly_2)
  assert intersection == True

def test_do_intersect_not():
  cpoly_1 = Polygon(np.array([[4,0], [5,2], [2,6], [1,1]]))
  cpoly_2 = Polygon(np.array([[5.5,11], [6,14], [5,15], [4,12]]))
  intersection = do_intersect(cpoly_1, cpoly_2)
  assert intersection == False

def test_do_intersect_in():
  cpoly_1 = Polygon(np.array([[4,0], [5,2], [2,6], [1,1]]))
  cpoly_2 = Polygon(np.array([[3,1], [3.5,1.5], [2.5,4], [2,2]]))
  intersection = do_intersect(cpoly_1, cpoly_2)
  assert intersection == True
