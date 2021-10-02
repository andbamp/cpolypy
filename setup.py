from setuptools import setup, find_packages

setup(
  name = 'cpolypy',
  version = '0.0.1',
  description = 'Simple methods for handling convex polygons',
  package_dir = {'': 'src'},
  packages = find_packages(where = "src"),
)
