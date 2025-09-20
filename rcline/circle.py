import matplotlib.pyplot as plt
import numpy as np
from .entity import Entity
from .colors import ENTITY_COLORS

class Circle(Entity):
    def __init__(self, point, radius, color=None, solid=True):
        color = color or (ENTITY_COLORS['solid_line'] if solid else ENTITY_COLORS['line'])
        super().__init__(color)
        
        self.x = point[0]
        self.y = point[1]
        self.radius = radius
        self.solid = solid
        self.type = 'circle'
        self.hover = False

    def draw(self, ax):
        line_width = 2.0 if self.solid else 1.0
        alpha = 1.0 if self.hover else 0.85

        circle = plt.Circle(
            (self.x, self.y),
            self.radius,
            color=self.color,
            fill=False,
            linewidth=line_width,
            alpha=alpha,
            zorder=3 if self.solid else 2
        )
        ax.add_patch(circle)

    def update(self, dt, entity_list):
        pass

    def get_center(self):
        return (self.x, self.y)