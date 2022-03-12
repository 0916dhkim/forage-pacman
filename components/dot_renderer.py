import turtle
from freegames import vector


class DotRenderer:
    def __init__(self, color):
        self._turtle = turtle.Turtle(visible=False)
        self._color = color

    def render(self, position: vector):
        self._turtle.clear()
        self._turtle.up()
        self._turtle.goto(position.x + 10, position.y + 10)
        self._turtle.dot(20, self._color)

    def on_delete(self):
        self._turtle.clear()
