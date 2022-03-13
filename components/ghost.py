from __future__ import annotations
from freegames import vector
from random import choice
from components.circle_renderer import CircleRenderer
from update_context import UpdateContext


class Ghost:
    options = [
        vector(5, 0),
        vector(-5, 0),
        vector(0, 5),
        vector(0, -5),
    ]

    def __init__(self, spawn_position: vector, aim: vector):
        self._position = spawn_position
        self._aim = aim
        self._circle_renderer = CircleRenderer("red")

    def render(self):
        self._circle_renderer.render(self._position)

    def update(self, context: UpdateContext):
        if context.tile_map.valid(self._position + self._aim):
            self._position += self._aim
        else:
            selected_option = choice(self.options)
            self._aim = selected_option.copy()

    def on_delete(self):
        self._circle_renderer.on_delete()

    def clone(self) -> Ghost:
        return Ghost(self._position.copy(), -self._aim.copy())
