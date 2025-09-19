# rcline/line.py
import matplotlib.pyplot as plt
from .entity import Entity
from .colors import ENTITY_COLORS

class Line(Entity):
    def __init__(self, start_x, start_y, end_x, end_y, color=None, solid=False):
        if solid:
            color = color or ENTITY_COLORS['solid_line']
        else:
            color = color or ENTITY_COLORS['line']
        super().__init__(color)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.solid = solid
        self.type = 'line'
        self.hover = False

    def update(self, dt, entity_list):
        pass

    def draw(self, ax):
        line_width = 2.0 if self.solid else 1.0
        line_style = '-' if self.solid else '--'
        alpha = 1.0 if self.hover else 0.85

        if self.solid:
            ax.plot(
                [self.start_x, self.end_x], 
                [self.start_y - 0.03, self.end_y - 0.03],
                color='black', 
                linewidth=line_width + 1,
                linestyle=line_style,
                alpha=0.15
            )
        
        ax.plot(
            [self.start_x, self.end_x], 
            [self.start_y, self.end_y],
            color=self.color, 
            linewidth=line_width,
            linestyle=line_style,
            alpha=alpha,
            zorder=3 if self.solid else 2
        )
        
    def get_points(self):
        return (self.start_x, self.start_y), (self.end_x, self.end_y)