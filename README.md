# UIL Mathematics Project

This project provides a set of mathematical tools implemented in Python. The tools include functions for solving quadratic equations, calculating angles between lines, performing geometric calculations for spheres and cones, and more. The project is designed to be used with the TI system for input and output.

## Files

- uil_math.py: The main script containing all the mathematical functions and the menu-driven interface.
- uil_dev.py: A development version of the script with similar functionality.
- .gitignore: Specifies files to be ignored by Git.

## Functions

### Quadratic Equation Solver

Solves quadratic equations of the form `ax^2 + bx + c = 0`.

```python
def quad(a, b, c):
    """Quadratic formula solver"""
    ...
```

### Angle Between Lines

Calculates the angle between two lines given their slopes.

```python
def ang_lines(m1, m2):
    """Angle between lines in degrees"""
    ...
```

### Sphere Calculations

Performs volume, surface area, and circumference calculations for a sphere.

```python
def sphere(r):
    """Sphere calculations"""
    ...
```

### Cone Calculations

Performs volume, surface area, and slant height calculations for a cone.

```python
def cone(r, h):
    """Cone calculations"""
    ...
```

### Arithmetic Sequence

Calculates the sum and nth term of an arithmetic sequence.

```python
def seq_arith(a1, d, n):
    """Arithmetic sequence"""
    ...
```

### Geometric Sequence

Calculates the sum and nth term of a geometric sequence.

```python
def seq_geom(a1, r, n):
    """Geometric sequence"""
    ...
```

### Regular Polygon

Calculates the area and apothem of a regular polygon.

```python
def polygon(s, n):
    """Regular polygon"""
    ...
```

### Shoelace Theorem

Calculates the area and perimeter of a polygon using the Shoelace theorem.

```python
def shoelace():
    """Shoelace theorem using L1, L2 lists"""
    ...
```

### Point to Plane Distance

Calculates the distance from a point to a plane.

```python
def plane_dist(x, y, z, a, b, c, d):
    """Point to plane distance"""
    ...
```

## Usage

Run the uil_math.py script to access the menu-driven interface. The script will display a menu with various mathematical tools. Select an option by entering the corresponding number and follow the prompts to input the required values.

```sh
python uil_math.py
```

## Contact

For any questions or issues, please open an issue on GitHub.
