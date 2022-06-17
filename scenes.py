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


class SummationFlawScene(Scene):
    """
    Scene for explaining the flaw of ramanujan summation.
    """

    def construct(self):
        reason = Tex(
            r"\justifying {The only flaw in the ramanujan summation is that we can't treat a divergent series as a convergent one.}").scale(0.75).to_corner(UP + LEFT).set_color(RED)
        self.play(Write(reason))
        self.wait(3)

        proof = Tex(r"\justifying {Real answer to the problem:\\$S_{n}=1+2+3+4+...+n$\\$S_{n}=\frac{n(n+1)}{2}$\\$\lim\limits_{n \to \infty} \frac{n(n+1)}{2} = \infty$}").scale(0.75).next_to(
            reason, DOWN).shift(0.4 * DOWN).to_corner(LEFT).set_color(GREEN)
        self.play(Write(proof))
        self.wait(3)

        conclusion = Tex(r"\justifying {As the number of terms in the sum increases, the sum tends to infinity}").scale(0.75).next_to(
            proof, DOWN).shift(0.6 * DOWN).to_corner(LEFT)
        self.play(Write(conclusion))
        self.wait(3)


class SummationFactScene(Scene):
    """
    Scene for explaining the fact about ramanujan summation.
    """

    def construct(self):
        ax = Axes(
            x_range=[-1.8, 0.8, 1],
            y_range=[-0.5, 0.72, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )

        self.play(Create(ax))
        self.wait(1)

        graph = ax.plot(lambda x: x / 2 * (x + 1),
                        x_range=[-1.8, 0.8], use_smoothing=True)
        self.play(Create(graph))
        self.wait(1)

        area = ax.get_area(graph, x_range=(-1.0, 0), color=RED, opacity=0.5)
        self.play(Create(area))
        self.wait(3)

        fact = Tex(r"\justifying {Area of red region = $-1/12$}").scale(
            0.75).next_to(area, LEFT).shift(0.3 * RIGHT + 1.1 * DOWN)
        self.play(Write(fact))
        self.wait(4)


class OutroScene(Scene):
    """
    Scene for the outro of the video.
    """

    def construct(self):
        self.play(Write(Tex(
            r"Thank You!\\And don't forget that sum of all the natural numbers isn't -1/12 ;)").scale(0.9)))
        self.wait(3)
