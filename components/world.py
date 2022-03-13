import turtle
from typing import List
from components.ghost import Ghost
from components.player import Player
from freegames import vector, floor

from components.text_renderer import TextRenderer

GHOST_MULTIPLY_COUNTER = 300
MAX_GHOST_MULTIPLIER = 32


class World:
    def __init__(
        self,
        tiles: List[int],
        ghosts: List[Ghost],
        player: Player,
        text_renderer: TextRenderer,
    ):
        self.tiles = tiles
        self.ghosts = ghosts
        self.player = player
        self.text_renderer = text_renderer
        self.score = 0

        self._max_ghosts = MAX_GHOST_MULTIPLIER * len(self.ghosts)
        self._turtle = turtle.Turtle(visible=False)
        self._ghost_multiply_counter = GHOST_MULTIPLY_COUNTER

    def find_tile_index(self, position: vector) -> int:
        """Return offset of point in tiles."""
        x = (floor(position.x, 20) + 200) / 20
        y = (180 - floor(position.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(self, position: vector) -> bool:
        """Return True if point is valid in tiles."""
        index = self.find_tile_index(position)

        if self.tiles[index] == 0:
            return False

        index = self.find_tile_index(position + 19)

        if self.tiles[index] == 0:
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

        for index in range(len(self.tiles)):
            tile = self.tiles[index]
            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.render_square(x, y)
                if tile == 1:
                    self.render_dot(x, y)

    def update_children(self):
        for ghost in self.ghosts:
            ghost.update(self)
        self.player.update(self)

    def render_children(self):
        self.text_renderer.render(self.score)
        self.player.render()
        for ghost in self.ghosts:
            ghost.render()

    def check_collision(self) -> List[Ghost]:
        collision_list: List[Ghost] = []
        for ghost in self.ghosts:
            if abs(self.player._position - ghost._position) < 20:
                collision_list.append(ghost)
        return collision_list

    def remove_ghost(self, ghost: Ghost):
        self.ghosts.remove(ghost)
        ghost.on_delete()

    def on_collision(self, ghost: Ghost):
        self.remove_ghost(ghost)

    def multiply_ghosts(self):
        clones = list(map(lambda ghost: ghost.clone(), self.ghosts))
        self.ghosts += clones

    def is_game_over(self):
        if len(self.ghosts) >= self._max_ghosts:
            return True
        if all(tile != 1 for tile in self.tiles):
            return True
        return False

    def handle_event_loop(self):
        self.update_children()
        self.render_children()

        
        if self._ghost_multiply_counter <= 0:
            self._ghost_multiply_counter = GHOST_MULTIPLY_COUNTER
            self.multiply_ghosts()
        self._ghost_multiply_counter -= 1

        collision_list = self.check_collision()
        for ghost in collision_list:
            self.on_collision(ghost)

        if self.is_game_over():
            return

        # Repeat on timer.
        turtle.ontimer(self.handle_event_loop, 100)

    def init(self):
        turtle.setup(420, 420, 370, 0)
        turtle.hideturtle()
        turtle.tracer(False)
        turtle.listen()
        turtle.onkey(lambda: self.player.change_aim(5, 0, self), "Right")
        turtle.onkey(lambda: self.player.change_aim(-5, 0, self), "Left")
        turtle.onkey(lambda: self.player.change_aim(0, 5, self), "Up")
        turtle.onkey(lambda: self.player.change_aim(0, -5, self), "Down")
        self.initial_render()
        self.handle_event_loop()
        turtle.done()
