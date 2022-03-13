import turtle
from typing import List
from freegames import vector, floor


class TileMap:
    def __init__(self, tiles: List[int]):
        self._tiles = tiles
        self._turtle = turtle.Turtle(visible=False)

    def get(self, index: int) -> int:
        """Get tile value at index."""
        return self._tiles[index]

    def set(self, index: int, value: int):
        """Set tile value at index."""
        self._tiles[index] = value

    def find_tile_index(self, position: vector) -> int:
        """Return offset of point in tiles."""
        x = (floor(position.x, 20) + 200) / 20
        y = (180 - floor(position.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(self, position: vector) -> bool:
        """Return True if point is valid in tiles."""
        index = self.find_tile_index(position)

        if self._tiles[index] == 0:
            return False

        index = self.find_tile_index(position + 19)

        if self._tiles[index] == 0:
            return False

        return position.x % 20 == 0 or position.y % 20 == 0

    def render_tile(self, index: int):
        position = self._tile_position(index)
        self._turtle.up()
        self._turtle.goto(position.x, position.y)
        self._turtle.down()
        self._turtle.begin_fill()

        for _ in range(4):
            self._turtle.forward(20)
            self._turtle.left(90)

        self._turtle.end_fill()

    def render_dot(self, index: int):
        position = self._tile_position(index)
        self._turtle.up()
        self._turtle.goto(position.x + 10, position.y + 10)
        self._turtle.dot(2, "white")

    def render_background(self):
        turtle.bgcolor("black")
        self._turtle.color("blue")

        for index in range(len(self._tiles)):
            tile = self._tiles[index]
            if tile > 0:
                self.render_tile(index)
                if tile == 1:
                    self.render_dot(index)

    def has_dots(self):
        """True if there is any dots left on this tile map."""
        return any(tile == 1 for tile in self._tiles)

    def _tile_position(self, index: int) -> vector:
        return vector(
            (index % 20) * 20 - 200,
            180 - (index // 20) * 20,
        )
