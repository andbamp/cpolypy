from cpolypy.utils import perpendicular_unit
import numpy as np

def do_intersect(cpoly_1, cpoly_2):
  axes = perpendicular_unit(np.vstack([cpoly_1.edges(), cpoly_2.edges()]))
  
  for axis in axes:
    proj_1 = np.dot(cpoly_1.vertices, axis.T)
    proj_2 = np.dot(cpoly_2.vertices, axis.T)
    if(np.min(proj_1) > np.max(proj_2) or np.min(proj_2) > np.max(proj_1)):
      return False
  
  return True
