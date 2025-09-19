# rcline/entity.py
class Entity:
    def __init__(self, color):
        self.color = color

    def draw(self, ax):
        pass

    def update(self, dt, entity_list=None):
        pass