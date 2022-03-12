from __future__ import annotations
from freegames import vector
from random import choice
from components.dot_renderer import DotRenderer

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from components.world import World


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
        self._dot_renderer = DotRenderer("red")

    def render(self):
        self._dot_renderer.render(self._position)

    def update(self, world: World):
        if world.valid(self._position + self._aim):
            self._position += self._aim
        else:
            selected_option = choice(self.options)
            self._aim = selected_option.copy()

    def on_delete(self):
        self._dot_renderer.on_delete()