from manim import *


class HelloScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.play(circle.animate.set_fill(RED, opacity=0.5))
