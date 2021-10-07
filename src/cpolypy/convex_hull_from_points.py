import numpy as np
from cpolypy.Polygon import Polygon
from cpolypy.utils import angle_with_horizontal, clockwise_turn

def convex_hull_from_points(points):
  lowest_pt = points[np.argmin(points[:,1]),]
  angles = angle_with_horizontal(lowest_pt, points.transpose())
  ind_order = np.argsort(angles)
  chull_ind = ind_order[0:3].tolist()
  
  for pt in ind_order[3:]:
    point = points[pt,]
    while(
      clockwise_turn(points[chull_ind[-2],], points[chull_ind[-1],], point) and\
      len(chull_ind) > 2
    ):
      chull_ind.pop()
    chull_ind.append(pt)
  
  chull = Polygon(points[chull_ind])
  return(chull)
