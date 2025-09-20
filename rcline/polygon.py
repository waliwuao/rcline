# rcline/polygon.py
from .entity import Entity
from .line import Line
from .colors import ENTITY_COLORS


class Polygon(Entity):
    def __init__(self, points, color=None, solid=False, close=True):
        color = color or (ENTITY_COLORS['solid_line'] if solid else ENTITY_COLORS['line'])
        super().__init__(color)
        self.x = points[0][0]
        self.y = points[0][1]
        self.vector = self._create_vector(points)
        self.points = points
        self.solid = solid
        self.close = close
        self.type = 'polygon'

        self.lines = self._create_lines()

    def _create_vector(self, points):
        vector = []
        if len(points) < 2:
            raise ValueError("多边形至少需要2个点")
        for i in range(len(points) - 1):
            vector.append([points[i + 1][0] - points[i][0], points[i + 1][1] - points[i][1]])
        return vector
        

    def _create_lines(self):
        lines = []
        num_points = len(self.points)

        if num_points < 2:
            raise ValueError("多边形至少需要2个点")

        for i in range(num_points - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            lines.append(Line([(x1, y1), (x2, y2)], self.color, self.solid))

        if self.close and num_points > 2:
            x1, y1 = self.points[-1]
            x2, y2 = self.points[0]
            lines.append(Line([(x1, y1), (x2, y2)], self.color, self.solid))

        return lines

    def update(self, dt, entity_list):
        for i in range(len(self.points)-1):
            self.points[i+1] = (self.points[i][0] + self.vector[i][0], self.points[i][1] + self.vector[i][1])
        self.lines = self._create_lines()

    def draw(self, ax):
        for line in self.lines:
            line.draw(ax)

    def get_lines(self):
        return self.lines

    def get_points(self):
        return self.points
