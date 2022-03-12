import turtle


class TextRenderer:
    def __init__(self, x: int, y: int, color):
        self._turtle = turtle.Turtle(visible=False)
        self._turtle.goto(x, y)
        self._turtle.color(color)
        self._is_first_render = True

    def render(self, text):
        if self._is_first_render:
            self._is_first_render = False
        else:
            self._turtle.undo()
        self._turtle.write(text)
