import turtle
from freegames import vector


class TextRenderer:
    def __init__(self, position: vector, color):
        self._turtle = turtle.Turtle(visible=False)
        self._position = position
        self._turtle.color(color)

    def render(self, text):
        self._turtle.clear()
        self._turtle.up()
        self._turtle.goto(self._position.x, self._position.y)
        self._turtle.write(text)
