import turtle
from typing import List
from components.ghost import Ghost
from components.player import Player
from components.tile_map import TileMap

from components.text_renderer import TextRenderer
from update_context import UpdateContext

GHOST_MULTIPLY_COUNTER = 300
MAX_GHOST_MULTIPLIER = 32


class Game:
    def __init__(
        self,
        tiles: List[int],
        ghosts: List[Ghost],
        player: Player,
        text_renderer: TextRenderer,
    ):
        self.tile_map = TileMap(tiles)
        self.ghosts = ghosts
        self.player = player
        self.text_renderer = text_renderer
        self.score = 0

        self._max_ghosts = MAX_GHOST_MULTIPLIER * len(self.ghosts)
        self._ghost_multiply_counter = GHOST_MULTIPLY_COUNTER

    def start(self):
        """Setup environment and start the event loop."""
        turtle.setup(420, 420, 370, 0)
        turtle.hideturtle()
        turtle.tracer(False)
        turtle.listen()
        turtle.onkey(lambda: self.player.change_aim(5, 0, self.tile_map), "Right")
        turtle.onkey(lambda: self.player.change_aim(-5, 0, self.tile_map), "Left")
        turtle.onkey(lambda: self.player.change_aim(0, 5, self.tile_map), "Up")
        turtle.onkey(lambda: self.player.change_aim(0, -5, self.tile_map), "Down")
        self.tile_map.render_background()
        self.handle_event_loop()
        turtle.done()

    def increment_score(self):
        self.score += 1

    def update_children(self):
        context = UpdateContext(self.tile_map, self.increment_score)
        for ghost in self.ghosts:
            ghost.update(context)
        self.player.update(context)

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
        """Handle collision between a ghost and the player."""
        self.remove_ghost(ghost)

    def multiply_ghosts(self):
        """Duplicate all current ghosts."""
        clones = list(map(lambda ghost: ghost.clone(), self.ghosts))
        self.ghosts += clones

    def is_game_over(self) -> bool:
        """Check game over status."""
        if len(self.ghosts) >= self._max_ghosts:
            return True
        if not self.tile_map.has_dots():
            return True
        return False

    def handle_event_loop(self):
        """This method gets called every tick."""
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
