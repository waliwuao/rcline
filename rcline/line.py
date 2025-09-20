# rcline/line.py
import matplotlib.pyplot as plt
from .entity import Entity
from .colors import ENTITY_COLORS

class Line(Entity):
    def __init__(self, points, color=None, solid=False):
        if solid:
            color = color or ENTITY_COLORS['solid_line']
        else:
            color = color or ENTITY_COLORS['line']
        super().__init__(color)
        self.x = points[0][0]
        self.y = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]
        self.vector = [self.x2 - self.x, self.y2 - self.y]
        self.solid = solid
        self.type = 'line'
        self.hover = False

    def update(self, dt, entity_list):
        self.x2 = self.x + self.vector[0]
        self.y2 = self.y + self.vector[1]

    def draw(self, ax):
        line_width = 2.0 if self.solid else 1.0
        line_style = '-' if self.solid else '--'
        alpha = 1.0 if self.hover else 0.85

        if self.solid:
            ax.plot(
                [self.x, self.x2], 
                [self.y - 0.03, self.y2 - 0.03],
                color='black', 
                linewidth=line_width + 1,
                linestyle=line_style,
                alpha=0.15
            )
        
        ax.plot(
            [self.x, self.x2], 
            [self.y, self.y2],
            color=self.color, 
            linewidth=line_width,
            linestyle=line_style,
            alpha=alpha,
            zorder=3 if self.solid else 2
        )
        
    def get_points(self):
        return (self.x, self.y), (self.x2, self.y2)
