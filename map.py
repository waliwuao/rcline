from cProfile import label
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import numpy as np
from .entity import Entity
from .line import Line
from .cat import Cat
from .collide import Collide
from .colors import BACKGROUND_COLOR, GRID_MAJOR_COLOR, GRID_MINOR_COLOR, DARK_GRAY, ENTITY_COLORS


class Map:
    def __init__(self, width=10, height=10, title="Simulation Map", grid=1):
        self.width = width
        self.height = height
        self.title = title
        self.grid_step = grid
        self.entity_list = []
        self.fig, self.ax = plt.subplots(facecolor=BACKGROUND_COLOR, figsize=(8, 8))
        self.animation = None
        self.bg_color = BACKGROUND_COLOR
        self.grid_major_color = GRID_MAJOR_COLOR
        self.grid_minor_color = GRID_MINOR_COLOR
        self.frame_count = 0
        self.setup_legend()
        self._add_boundary_lines()

    def _add_boundary_lines(self):
        top_line = Line([(0, self.height), (self.width, self.height)], solid=True)
        bottom_line = Line([(0, 0), (self.width, 0)], solid=True)
        left_line = Line([(0, 0), (0, self.height)], solid=True)
        right_line = Line([(self.width, 0), (self.width, self.height)], solid=True)
        for line in [top_line, bottom_line, left_line, right_line]:
            self.add_entity(line)

    def setup_legend(self):
        cat_patch = mpatches.Patch(color=ENTITY_COLORS['cat'], label='Cat')
        solid_line = mpatches.Patch(color=ENTITY_COLORS['solid_line'], label='Solid Line')
        line_patch = mpatches.Patch(color=ENTITY_COLORS['line'], label='Line')

        legend = self.fig.legend(
            handles=[cat_patch, solid_line, line_patch],
            loc='upper center',
            bbox_to_anchor=(0.5, 0.92),
            ncol=3,
            frameon=True,
            framealpha=0.9,
            edgecolor=GRID_MAJOR_COLOR,
            fontsize=9,
            handlelength=1.5,
            columnspacing=1.0
        )
        legend.get_frame().set_facecolor('none')

    def add_entity(self, entity):
        if isinstance(entity, Entity):
            self.entity_list.append(entity)
        else:
            raise ValueError("只能添加Entity子类的实例")

    def remove_entity(self, entity):
        if entity in self.entity_list:
            self.entity_list.remove(entity)

    def _draw_grid(self):
        self.ax.grid(
            True,
            which='major',
            color=self.grid_major_color,
            linestyle='-',
            linewidth=0.8,
            zorder=1
        )

        self.ax.grid(
            True,
            which='minor',
            color=self.grid_minor_color,
            linestyle='-',
            linewidth=0.3,
            alpha=0.7,
            zorder=1
        )

        self.ax.set_xticks(np.arange(0, self.width + self.grid_step, self.grid_step), minor=False)
        self.ax.set_yticks(np.arange(0, self.height + self.grid_step, self.grid_step), minor=False)

        sub_step = self.grid_step / 5
        self.ax.set_xticks(np.arange(0, self.width + sub_step, sub_step), minor=True)
        self.ax.set_yticks(np.arange(0, self.height + sub_step, sub_step), minor=True)

        self.ax.tick_params(
            axis='both',
            which='both',
            colors=DARK_GRAY,
            labelsize=8,
            width=0.5
        )

    def _init_plot(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_title(
            self.title,
            color=DARK_GRAY,
            fontsize=14,
            pad=20,
            fontweight='medium'
        )
        self.ax.set_aspect('equal')
        self.ax.set_facecolor(self.bg_color)
        self._draw_grid()
        self.setup_legend()

        for spine in ['top', 'right']:
            self.ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            self.ax.spines[spine].set_visible(True)
            self.ax.spines[spine].set_color(GRID_MAJOR_COLOR)
            self.ax.spines[spine].set_linewidth(0.8)

        return self.ax,

    def _update_frame(self, frame):
        self.frame_count += 1
        self.ax.clear()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_title(
            self.title,
            color=DARK_GRAY,
            fontsize=14,
            pad=20,
            fontweight='medium'
        )
        self.ax.set_aspect('equal')
        self.ax.set_facecolor(self.bg_color)
        self._draw_grid()
        self.setup_legend()

        for spine in ['top', 'right']:
            self.ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            self.ax.spines[spine].set_visible(True)
            self.ax.spines[spine].set_color(GRID_MAJOR_COLOR)
            self.ax.spines[spine].set_linewidth(0.8)

        for entity in self.entity_list:
            entity.update(dt=0.05, entity_list=self.entity_list)

        for entity in self.entity_list:
            entity.draw(self.ax)

        return self.ax,

    def start_simulation(self, interval=50):
        self.animation = animation.FuncAnimation(
            self.fig,
            self._update_frame,
            init_func=self._init_plot,
            interval=interval,
            blit=True
        )
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def stop_simulation(self):
        if self.animation:
            self.animation.event_source.stop()