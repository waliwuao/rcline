# rcline/collide.py
import numpy as np
from .entity import Entity

class Collide:
    @staticmethod
    def check_collision(entity1, entity2):
        if not isinstance(entity1, Entity) or not isinstance(entity2, Entity):
            return False

        type1 = getattr(entity1, 'type', None)
        type2 = getattr(entity2, 'type', None)

        if type1 == 'line' and type2 == 'line':
            return Collide._line_line_collision(entity1, entity2)        
        if (type1 == 'cat' and type2 == 'line'):
            return Collide._circle_line_collision(entity1, entity2)
        if (type1 == 'line' and type2 == 'cat'):
            return Collide._circle_line_collision(entity2, entity1)
        if type1 == 'cat' and type2 == 'cat':
            return Collide._circle_circle_collision(entity1, entity2)
        
        return False

    @staticmethod
    def _circle_circle_collision(circle1, circle2):
        dx = circle1.x - circle2.x
        dy = circle1.y - circle2.y
        distance = np.hypot(dx, dy)
        return distance <= (circle1.radius + circle2.radius)

    @staticmethod
    def _line_line_collision(line1, line2):
        (x1, y1), (x2, y2) = line1.get_points()
        (x3, y3), (x4, y4) = line2.get_points()

        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

        def on_segment(p, q, r):
            return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

        o1 = cross((x1, y1), (x2, y2), (x3, y3))
        o2 = cross((x1, y1), (x2, y2), (x4, y4))
        o3 = cross((x3, y3), (x4, y4), (x1, y1))
        o4 = cross((x3, y3), (x4, y4), (x2, y2))

        if (o1 * o2 < 0) and (o3 * o4 < 0):
            return True
        if o1 == 0 and on_segment((x1, y1), (x3, y3), (x2, y2)):
            return True
        if o2 == 0 and on_segment((x1, y1), (x4, y4), (x2, y2)):
            return True
        if o3 == 0 and on_segment((x3, y3), (x1, y1), (x4, y4)):
            return True
        if o4 == 0 and on_segment((x3, y3), (x2, y2), (x4, y4)):
            return True

        return False

    @staticmethod
    def _circle_line_collision(circle, line):
        if not line.solid:
            return False

        (x1, y1), (x2, y2) = line.get_points()
        
        if x1 == x2 and y1 == y2:
            distance = np.hypot(circle.x - x1, circle.y - y1)
            return distance <= circle.radius

        dx = x2 - x1
        dy = y2 - y1
        
        t = ((circle.x - x1) * dx + (circle.y - y1) * dy) / (dx * dx + dy * dy)
        t = max(0, min(1, t))
        
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        
        distance = np.hypot(circle.x - proj_x, circle.y - proj_y)
        
        return distance <= circle.radius