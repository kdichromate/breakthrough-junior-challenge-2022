from manim import *
from math import sin, cos


class IntroScene(Scene):
    """
    Scene for the intro of the video.
    """

    def construct(self):
        MAX_SIDES = 8
        ref_shape = None
        for side_n in range(3, MAX_SIDES + 1):
            # Regular Polygon animation
            angle = 2 * PI / side_n
            co_ords = [[sin(i * angle), cos(i * angle), 0]
                       for i in range(side_n)]
            polygon = Polygon(*co_ords)
            polygon.set_fill(random_bright_color(), opacity=0.5)

            if not ref_shape:
                ref_shape = polygon
                self.add(ref_shape)
            else:
                self.play(ReplacementTransform(ref_shape, polygon))
                ref_shape = polygon

        self.play(ReplacementTransform(ref_shape, Tex("Hello, World!")))
        self.wait(2)


class ProblemStatingScene(Scene):
    """
    Scene for stating the problem statement.
    """

    def construct(self):
        statement = Tex(
            r"What is the the sum of all the natural numbers?\\1+2+3+4+...+n=?")
        self.play(Write(statement))
        self.wait(3)
