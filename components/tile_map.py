import turtle
from typing import List
from freegames import vector, floor

class TileMap:
    def __init__(self, tiles: List[int]):
        self._tiles = tiles
        self._turtle = turtle.Turtle(visible=False)

    def get(self, index: int) -> int:
        return self._tiles[index]

    def set(self, index: int, value: int):
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

    def render_square(self, x: int, y: int):
        self._turtle.up()
        self._turtle.goto(x, y)
        self._turtle.down()
        self._turtle.begin_fill()

        for _ in range(4):
            self._turtle.forward(20)
            self._turtle.left(90)

        self._turtle.end_fill()

    def render_dot(self, x: int, y: int):
        self._turtle.up()
        self._turtle.goto(x + 10, y + 10)
        self._turtle.dot(2, "white")

    def initial_render(self):
        turtle.bgcolor("black")
        self._turtle.color("blue")

        for index in range(len(self._tiles)):
            tile = self._tiles[index]
            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.render_square(x, y)
                if tile == 1:
                    self.render_dot(x, y)
                
    def has_dots(self):
        return any(tile == 1 for tile in self._tiles)