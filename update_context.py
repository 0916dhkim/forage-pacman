from components.tile_map import TileMap
from typing import Callable

class UpdateContext:
    def __init__(self, tile_map: TileMap, on_score: Callable[[], None]):
        self.tile_map = tile_map
        self.on_score = on_score
