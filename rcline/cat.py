import matplotlib.pyplot as plt
import numpy as np
from .entity import Entity
from .collide import Collide
from .colors import ENTITY_COLORS, ACCENT_COLOR
import keyboard

class Cat(Entity):
    def __init__(self, point, radius=1, color=None, vx=0, vy=0, ax=0, ay=0, move_acceleration=2,
                 friction=1, controllable=False):
        color = color or ENTITY_COLORS['cat']
        super().__init__(color)
        self.x = point[0]
        self.y = point[1]
        self.type = 'circle'
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.controllable = controllable
        self.friction = friction
        self.move_acceleration = move_acceleration
        self.colliding = False
        self.pulse_factor = 1.0
        self.pulse_direction = 0.001
        self.collision_normal = None

    def draw(self, ax):
        circle_color = ACCENT_COLOR if self.colliding else self.color
        current_radius = self.radius * self.pulse_factor if self.colliding else self.radius
        
        circle = plt.Circle(
            (self.x, self.y), 
            current_radius, 
            color=circle_color, 
            fill=True,
            edgecolor='white',
            linewidth=1.2,
            alpha=0.95,
            zorder=4
        )
        ax.add_patch(circle)
        
        if self.controllable:
            speed = np.hypot(self.vx, self.vy)
            if speed > 0.1:
                dir_len = current_radius * 0.7
                ax.arrow(
                    self.x, self.y,
                    self.vx * dir_len / speed, self.vy * dir_len / speed,
                    head_width=self.radius*0.3, head_length=self.radius * 0.4,
                    fc='white', ec='white',
                    linewidth=1.0,
                    zorder=5
                )
        
        if self.colliding:
            circle = plt.Circle(
                (self.x, self.y), 
                current_radius * 1.2, 
                color=circle_color, 
                fill=False,
                linewidth=1.0,
                alpha=0.6,
                zorder=4
            )
            ax.add_patch(circle)

    def update(self, dt, entity_list):
        self.ax = 0
        self.ay = 0

        if self.controllable:
            self._handle_keyboard()

        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.vx *= self.friction
        self.vy *= self.friction

        old_x, old_y = self.x, self.y
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.collision_normal = None
        self.colliding = self._check_collision(entity_list)
        
        if self.colliding:
            self.x, self.y = old_x, old_y
            
            if self.controllable:
                self.vx *= 0
                self.vy *= 0
            else:
                if self.collision_normal is not None:
                    self._reflect_velocity()
            
            self.pulse_factor = 1.2
        
        self._update_pulse()

    def _reflect_velocity(self):
        if self.collision_normal is None:
            return
            
        nx, ny = self.collision_normal
        norm = np.hypot(nx, ny)
        if norm == 0:
            return
        nx /= norm
        ny /= norm
        
        v = np.array([self.vx, self.vy])
        dot_product = np.dot(v, [nx, ny])
        reflected_v = v - 2 * dot_product * np.array([nx, ny])
        
        restitution = 1
        self.vx, self.vy = reflected_v * restitution

    def _update_pulse(self):
        if self.colliding:
            self.pulse_factor = max(1.0, self.pulse_factor - 0.05)
        else:
            self.pulse_factor = 1.0
            self.pulse_direction = 0.001

    def _handle_keyboard(self):
        if keyboard.is_pressed('down'):
            self.ay = -self.move_acceleration
        if keyboard.is_pressed('up'):
            self.ay = self.move_acceleration
        if keyboard.is_pressed('right'):
            self.ax = self.move_acceleration
        if keyboard.is_pressed('left'):
            self.ax = -self.move_acceleration

    def _check_collision(self, entity_list):
        for entity in entity_list:
            if entity is self:
                continue
            
            if entity.type == 'polygon' and entity.solid:
                for line in entity.get_lines():
                    if line.solid and Collide.check_collision(self, line):
                        (x1, y1), (x2, y2) = line.get_points()
                        dx = x2 - x1
                        dy = y2 - y1
                        self.collision_normal = (dy, -dx)
                        return True
            
            if Collide.check_collision(self, entity):
                if entity.type == 'line' and entity.solid:
                    (x1, y1), (x2, y2) = entity.get_points()
                    dx = x2 - x1
                    dy = y2 - y1
                    self.collision_normal = (dy, -dx)
                elif entity.type == 'circle':
                    dx = self.x - entity.x
                    dy = self.y - entity.y
                    self.collision_normal = (dx, dy)
                return True
        return False