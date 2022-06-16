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
            angle = TAU / side_n
            co_ords = [[sin(i * angle), cos(i * angle), 0]
                       for i in range(side_n)]
            polygon = Polygon(
                *co_ords).set_fill(random_bright_color(), opacity=0.5)

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


class RamanujanSummationScene(Scene):
    """
    Scene for explaining the ramanujan summation.
    """

    def construct(self):
        info = Tex(
            r"\justifying {A great Indian mathematician Sir Srinivasa Ramanujan calculated the sum of all the natural numbers in a very interesting way. We address the method as Ramanujan Summation.}").scale(0.75).to_corner(UP + LEFT)
        self.play(Write(info))
        self.wait(5)

        proof_a = Tex(r"\justifying {Proof:\\$A=1-1+1-1+...$\\$A=1-(1-1+1-1+...)$\\$A=1-A$\\$A=1/2$}").scale(
            0.75).next_to(info, DOWN).shift(DOWN).to_corner(LEFT)
        self.play(Write(proof_a))
        self.wait(6)

        proof_b = Tex(r"\justifying {$B=1-2+3-4+...$\\$A-B=(1-1+1-1+...)-(1-2+3-4+...)$\\$A-B=(1-1)+(-1+2)+(1-3)+(-1+4)+...$\\$A-B=1-2+3-4+...$\\$A-B=B$\\$B=1/4$}").scale(
            0.75).next_to(proof_a, RIGHT).shift(0.1 * DOWN)
        self.play(Write(proof_b))
        self.wait(6)

        self.clear()

        proof_c = Tex(r"\justifying {$S=1+2+3+4+...$\\$B-S=(1-2+3-4+...)-(1+2+3+4+...)$\\$B-S=(1-1)+(-2+2)+(3-3)+(-4+4)+(5-5)+(-6-6)+...$\\$B-S=-4(1+2+3+...)$\\$B-S=-4S$\\$S=-1/12$}").scale(
            0.75).to_corner(UP + LEFT)
        self.play(Write(proof_c))
        self.wait(6)

        self.clear()

        flushed_img = ImageMobject(
            "resources/flushed.png").scale(0.4).to_corner(UP)
        self.add(flushed_img)
        self.wait(1)

        exclamation = Tex(r"\justifying {sum of positive numbers = negative?}").next_to(
            flushed_img, DOWN)
        self.play(Write(exclamation))
        self.wait(1)

        end_line = Tex(r"\justifying {Sir Ramanujan wasn't right here, let's see how!}").next_to(
            exclamation, DOWN).shift(0.6*DOWN)
        self.play(Write(end_line))
        self.wait(2)
