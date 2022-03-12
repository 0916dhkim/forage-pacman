from __future__ import annotations
from freegames import vector
from components.dot_renderer import DotRenderer

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from components.world import World


class Player:
    def __init__(self, position: vector, aim: vector):
        self._position = position
        self._aim = aim
        self._dot_renderer = DotRenderer("yellow")

    def render(self):
        self._dot_renderer.render(self._position)

    def update(self, world: World):
        if world.valid(self._position + self._aim):
            self._position += self._aim
        tile_index = world.find_tile_index(self._position)
        if world.tiles[tile_index] == 1:
            world.tiles[tile_index] = 2
            world.score += 1
            x = (tile_index % 20) * 20 - 200
            y = 180 - (tile_index // 20) * 20
            world.render_square(x, y)

    def change_aim(self, x, y, world: World):
        if world.valid(self._position + vector(x, y)):
            self._aim = vector(x, y)
