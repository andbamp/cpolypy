# cpolypy

This is an example Python project implementing a few simple methods for handling convex polygons.

## Installation

To install the library, please download the repository's code and run the following commands in the project's directory.

```bash
python setup.py bdist_wheel
pip install -e .
```

## Usage

The library can be imported as shown below.

```python
import cpolypy
```

- Finding the convex hull:

```python
import numpy as np
import cpolypy as cp

point_cloud = np.array([[0,0], [1,2], [1,3], [2,1], [2,2], [3,1]])
chull = cp.convex_hull_from_points(point_cloud)
```

- Testing whether a point lies inside a convex polygon:

```python
import numpy as np
import cpolypy as cp

points = np.array([[-1,-2], [1,-1], [0,2], [-2, -1]])
cpoly = cp.Polygon(points)
point = np.array([0, 0.5])
pip = cp.point_is_in_polygon(point, cpoly)
```

- Testing if two convex polygons intersect:

```python
import numpy as np
import cpolypy as cp

cpoly_1 = cp.Polygon(np.array([[4,0], [5,2], [2,6], [1,1]]))
cpoly_2 = cp.Polygon(np.array([[5.5,1], [6,4], [5,5], [4,2]]))
intersection = cp.do_intersect(cpoly_1, cpoly_2)
```

## Development

To build and test the library, use the following commands after changing the respective source files.

```bash
python setup.py bdist_wheel
pip install -e .'[dev]'
pytest
```
