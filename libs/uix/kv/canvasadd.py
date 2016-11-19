from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


def canvas_add(instance, color=None):
    if not color:
        color = [0, 0, 0, 1]

    with instance.canvas.before:
        Color(rgba=color)
        canvas_instance = \
            Rectangle(
                pos=(5, 0),
                size=(instance.width, instance.height)
            )

        def on_canvas_pos(instance, value):
            canvas_instance.pos = value

        def on_canvas_size(instance, value):
            canvas_instance.size = value

        instance.bind(size=on_canvas_size, pos=on_canvas_pos)
