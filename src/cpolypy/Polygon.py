class Polygon():
  
  def __init__(self, points_array = None):
    if points_array is None:
      self.points = []
    else:
      self.points = points_array.tolist()
  
  def __str__(self):
    return "Polygon composed of points: {}".format(self.points)
