from manim import *
import random

# NOTA PARA EL GRUPO:
# Copiar este método dentro de la clase principal en el archivo final.

class Part2Scene(Scene): 
    def construct(self):
        self.part2_good_split()

    def part2_good_split(self):
        # 1. Título de Sección
        part2_title = Text("Parte 2: ¿Qué hace una buena división?", font_size=40, color=YELLOW)
        self.play(Write(part2_title))
        self.wait(1)
        self.play(part2_title.animate.to_edge(UP))

        # 2. INTUICIÓN VISUAL
        self.visual_split_intuition()
        self.clear()
        
        # Restauramos título para la teoría
        part2_title = Text("Parte 2: La Matemática (Gini)", font_size=36, color=YELLOW).to_edge(UP)
        self.add(part2_title)

        # 3. TEORÍA
        self.explain_purity()
        self.wait(1)
        self.clear()
        self.add(part2_title)
        
        self.explain_gini_impurity()

    def visual_split_intuition(self):
        sub = Text("Intuición: Separar el desorden", font_size=24, color=GRAY).next_to(ORIGIN, UP*3)
        self.play(FadeIn(sub))

        box = Rectangle(height=4, width=6, color=WHITE)
        dots = VGroup()
        red_dots = VGroup()
        blue_dots = VGroup()
        
        for _ in range(10): 
            d = Dot(color=RED, point=[random.uniform(-2.5, 2.5), random.uniform(-1.5, 1.5), 0])
            red_dots.add(d)
            dots.add(d)
        for _ in range(10): 
            d = Dot(color=BLUE, point=[random.uniform(-2.5, 2.5), random.uniform(-1.5, 1.5), 0])
            blue_dots.add(d)
            dots.add(d)

        self.play(Create(box), Create(dots))
        self.wait(1)

        # CASO 1: MAL SPLIT
        split_line = DashedLine(start=[0, 2, 0], end=[0, -2, 0], color=YELLOW)
        bad_label = Text("¿Mal corte?", color=YELLOW, font_size=28).next_to(split_line, UP)
        self.play(Create(split_line), Write(bad_label))
        self.wait(1)
        feedback = Text("Gini Alto (Mucha mezcla)", color=RED, font_size=24).next_to(box, DOWN)
        self.play(Write(feedback))
        self.wait(1)
        self.play(FadeOut(split_line), FadeOut(bad_label), FadeOut(feedback))

        # CASO 2: BUEN SPLIT
        good_label = Text("¡Buen corte!", color=GREEN, font_size=28).move_to([0, 2.5, 0])
        split_line_solid = Line(start=[0, 2, 0], end=[0, -2, 0], color=GREEN)

        anims = []
        for dot in red_dots:
            target = [random.uniform(-2.8, -0.2), random.uniform(-1.8, 1.8), 0]
            anims.append(dot.animate.move_to(target))
        for dot in blue_dots:
            target = [random.uniform(0.2, 2.8), random.uniform(-1.8, 1.8), 0]
            anims.append(dot.animate.move_to(target))

        self.play(Write(good_label), Create(split_line_solid))
        self.play(*anims, run_time=2) 

        feedback_good = Text("Gini Bajo (Grupos Puros)", color=GREEN, font_size=24).next_to(box, DOWN)
        self.play(Write(feedback_good))
        self.wait(2)

    def explain_purity(self):
        title = Text("Concepto de Pureza e Impureza", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        pure_title = Text("Puro (Homogéneo)", font_size=28, color=GREEN).move_to(LEFT * 3.5 + UP * 2)
        impure_title = Text("Impuro (Mixto)", font_size=28, color=RED).move_to(RIGHT * 3.5 + UP * 2)
        self.play(Write(pure_title), Write(impure_title))
        
        pure_group = VGroup()
        for i in range(3):
            for j in range(3):
                apple = Circle(radius=0.2, color=RED, fill_opacity=0.8).move_to(LEFT * 3.5 + UP * (0.5 - i * 0.5) + RIGHT * (j * 0.5 - 0.5))
                pure_group.add(apple)
        
        impure_group = VGroup()
        colors = [RED, BLUE, RED, BLUE, RED, BLUE, BLUE, RED, BLUE]
        for i in range(3):
            for j in range(3):
                fruit = Circle(radius=0.2, color=colors[i * 3 + j], fill_opacity=0.8).move_to(RIGHT * 3.5 + UP * (0.5 - i * 0.5) + RIGHT * (j * 0.5 - 0.5))
                impure_group.add(fruit)

        self.play(FadeIn(pure_group), FadeIn(impure_group))
        self.wait(2)

    def explain_gini_impurity(self):
        title = Text("Gini Impurity (Impureza de Gini)", font_size=42, color=BLUE).to_edge(UP)
        self.play(Write(title))
        formula = MathTex(r"Gini = 1 - \sum_{i=1}^{n} p_i^2", font_size=60, color=WHITE)
        self.play(Write(formula))
        self.wait(2)
