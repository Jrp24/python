class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius


def point_in_circle(circle, x, y):
    distance_squared = (x - circle.center_x) ** 2 + (y - circle.center_y) ** 2
    return distance_squared <= circle.radius ** 2


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height


def rect_in_circle(circle, rect):
    corners = [
        (rect.x, rect.y),
        (rect.x + rect.width, rect.y),
        (rect.x, rect.y + rect.height),
        (rect.x + rect.width, rect.y + rect.height)
    ]
    return all(point_in_circle(circle, x, y) for x, y in corners)


def rect_circle_overlap(circle, rect):
    corners = [
        (rect.x, rect.y),
        (rect.x + rect.width, rect.y),
        (rect.x, rect.y + rect.height),
        (rect.x + rect.width, rect.y + rect.height)
    ]

    if any(point_in_circle(circle, x, y) for x, y in corners):
        return True
     return False


circle = Circle(150, 100, 75)
rectangle = Rectangle(110, 80, 40, 20)
point_x, point_y = 140, 110

print(point_in_circle(circle, point_x, point_y))  
print(rect_in_circle(circle, rectangle))  
print(rect_circle_overlap(circle, rectangle))
