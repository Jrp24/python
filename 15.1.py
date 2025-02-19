from __future__ import print_function, division

import copy
from Point1 import Point, Rectangle, print_point
from Point1_soln import distance_between_points


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary)."""
    d = distance_between_points(point, circle.center)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the rectangle is entirely within the circle."""
    p = copy.copy(rect.corner)

    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corner of a rectangle falls inside a circle."""
    p = copy.copy(rect.corner)

    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle(Point(150.0, 100.0), 75.0)

    print("Point in Circle:", point_in_circle(box.corner, circle))
    print("Rectangle in Circle:", rect_in_circle(box, circle))
    print("Rectangle overlaps Circle:", rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
