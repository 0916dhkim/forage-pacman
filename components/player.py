from components.tile_map import TileMap
from update_context import UpdateContext
from freegames import vector
from components.circle_renderer import CircleRenderer


class Player:
    def __init__(self, position: vector, aim: vector):
        self._position = position
        self._aim = aim
        self._circle_renderer = CircleRenderer("yellow")

    def render(self):
        self._circle_renderer.render(self._position)

    def update(self, context: UpdateContext):
        if context.tile_map.valid(self._position + self._aim):
            self._position += self._aim
        tile_index = context.tile_map.find_tile_index(self._position)
        if context.tile_map.get(tile_index) == 1:
            context.tile_map.set(tile_index, 2)
            context.on_score()
            context.tile_map.render_tile(tile_index)

    def change_aim(self, x, y, tile_map: TileMap):
        if tile_map.valid(self._position + vector(x, y)):
            self._aim = vector(x, y)
