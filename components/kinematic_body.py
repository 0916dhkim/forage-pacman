from freegames import vector


class KinematicBody:
    def __init__(self, position: vector):
        self._position = position

    def move(self, delta: vector):
        if KinematicBody._valid(self._position + delta):
            self._position += delta

    def _valid(position: vector) -> bool:
        index = find_tile_index(position)

        if tiles[index] == 0:
            return False

        index = find_tile_index(position + 19)

        if tiles[index] == 0:
            return False

        return position.x % 20 == 0 or position.y % 20 == 0
