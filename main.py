from manim import *
import numpy as np

class DecisionTreeComplete(Scene):
    def construct(self):
        self.part1_introduction()
        self.clear()

        self.part2_good_split()
        self.clear()

        self.part3_building_tree()
        self.clear()

        self.part4_real_dataset()

    # PARTE 1: INTRODUCCION e INTUICION
    def part1_introduction(self):
        # Título principal
        title = Text("Decision Trees", font_size=72, weight=BOLD, color=BLUE)
        subtitle = Text("Árboles de Decisión", font_size=36, color=GRAY)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Parte 1 - Título
        part1_title = Text("Parte 1: Introducción e Intuición", font_size=48, color=YELLOW)
        self.play(Write(part1_title))
        self.wait(1.5)
        self.play(part1_title.animate.to_edge(UP))

        # Ejemplo cotidiano: ¿Salir a jugar?
        question = Text("¿Debería salir a jugar afuera?", font_size=40, color=WHITE)
        question.move_to(UP * 2)
        self.play(Write(question))
        self.wait(1)

        # Crear árbol simple
        tree = self.create_simple_tree()
        tree.scale(0.8).move_to(DOWN * 0.5)

        self.play(Create(tree))
        self.wait(2)

        # Explicar componentes
        self.explain_tree_components(tree)

    def create_simple_tree(self):
        # Root node
        root = RoundedRectangle(
            corner_radius=0.2,
            height=1,
            width=2.5,
            color=BLUE,
            fill_opacity=0.3
        )
        root_text = Text("¿Está\nlloviendo?", font_size=24)
        root_group = VGroup(root, root_text)
        root_group.move_to(UP * 2)

        # Left branch - Sí
        left_line = Line(root.get_bottom(), root.get_bottom() + DOWN * 1.5 + LEFT * 2)
        left_label = Text("Sí", font_size=20, color=RED).next_to(left_line.get_center(), LEFT, buff=0.1)

        left_leaf = RoundedRectangle(
            corner_radius=0.2,
            height=0.8,
            width=2,
            color=RED,
            fill_opacity=0.5
        )
        left_leaf_text = Text("Quedarme\nen casa", font_size=22, color=WHITE)
        left_leaf_group = VGroup(left_leaf, left_leaf_text)
        left_leaf_group.move_to(root.get_bottom() + DOWN * 2 + LEFT * 2.5)

        # Right branch - No
        right_line = Line(root.get_bottom(), root.get_bottom() + DOWN * 1.5 + RIGHT * 2)
        right_label = Text("No", font_size=20, color=GREEN).next_to(right_line.get_center(), RIGHT, buff=0.1)

        # Internal node
        internal_node = RoundedRectangle(
            corner_radius=0.2,
            height=1,
            width=2.5,
            color=ORANGE,
            fill_opacity=0.3
        )
        internal_text = Text("¿Hace\ncalor?", font_size=24)
        internal_group = VGroup(internal_node, internal_text)
        internal_group.move_to(root.get_bottom() + DOWN * 2 + RIGHT * 2.5)

        # Branches from internal node
        int_left_line = Line(internal_node.get_bottom(), internal_node.get_bottom() + DOWN * 1.2 + LEFT * 1)
        int_left_label = Text("Sí", font_size=18, color=GREEN).next_to(int_left_line.get_center(), LEFT, buff=0.1)

        int_left_leaf = RoundedRectangle(corner_radius=0.2, height=0.8, width=1.8, color=GREEN, fill_opacity=0.5)
        int_left_leaf_text = Text("Ir a la\npiscina", font_size=20, color=WHITE)
        int_left_leaf_group = VGroup(int_left_leaf, int_left_leaf_text)
        int_left_leaf_group.move_to(internal_node.get_bottom() + DOWN * 1.5 + LEFT * 1.5)

        int_right_line = Line(internal_node.get_bottom(), internal_node.get_bottom() + DOWN * 1.2 + RIGHT * 1)
        int_right_label = Text("No", font_size=18, color=GREEN).next_to(int_right_line.get_center(), RIGHT, buff=0.1)

        int_right_leaf = RoundedRectangle(corner_radius=0.2, height=0.8, width=1.8, color=GREEN, fill_opacity=0.5)
        int_right_leaf_text = Text("Ir al\nparque", font_size=20, color=WHITE)
        int_right_leaf_group = VGroup(int_right_leaf, int_right_leaf_text)
        int_right_leaf_group.move_to(internal_node.get_bottom() + DOWN * 1.5 + RIGHT * 1.5)

        return VGroup(
            root_group, left_line, left_label, left_leaf_group,
            right_line, right_label, internal_group,
            int_left_line, int_left_label, int_left_leaf_group,
            int_right_line, int_right_label, int_right_leaf_group
        )

    def explain_tree_components(self, tree):
        # Root Node
        root_arrow = Arrow(start=UP * 3.5 + LEFT * 3, end=UP * 2.5 + LEFT * 0.5, color=YELLOW, buff=0.1)
        root_label = Text("Root Node\n(Nodo Raíz)", font_size=24, color=YELLOW)
        root_label.next_to(root_arrow.get_start(), LEFT)

        self.play(Create(root_arrow), Write(root_label))
        self.wait(1.5)

        # Internal Node
        internal_arrow = Arrow(start=UP * 0.5 + RIGHT * 4.5, end=UP * 0.3 + RIGHT * 3.5, color=ORANGE, buff=0.1)
        internal_label = Text("Internal Node\n(Nodo Interno)", font_size=24, color=ORANGE)
        internal_label.next_to(internal_arrow.get_start(), RIGHT)

        self.play(Create(internal_arrow), Write(internal_label))
        self.wait(1.5)

        # Leaf Nodes
        leaf_arrow = Arrow(start=DOWN * 2 + LEFT * 5, end=DOWN * 2 + LEFT * 3.5, color=GREEN, buff=0.1)
        leaf_label = Text("Leaf Nodes\n(Hojas - Decisiones)", font_size=24, color=GREEN)
        leaf_label.next_to(leaf_arrow.get_start(), LEFT)

        self.play(Create(leaf_arrow), Write(leaf_label))
        self.wait(2)

        self.play(
            FadeOut(root_arrow), FadeOut(root_label),
            FadeOut(internal_arrow), FadeOut(internal_label),
            FadeOut(leaf_arrow), FadeOut(leaf_label)
        )
        self.wait(1)

    # PARTE 2: Qué hace una buena división?
    def part2_good_split(self):
        part2_title = Text("Parte 2: ¿Qué hace una buena división?", font_size=48, color=YELLOW)
        self.play(Write(part2_title))
        self.wait(1.5)
        self.play(part2_title.animate.to_edge(UP))

        # Concepto de pureza
        self.explain_purity()
        self.wait(1)
        self.clear()

        # Gini Impurity
        self.explain_gini_impurity()

    def explain_purity(self):
        title = Text("Concepto de Pureza e Impureza", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Ejemplo visual con frutas
        pure_title = Text("Puro (Homogéneo)", font_size=28, color=GREEN)
        pure_title.move_to(LEFT * 3.5 + UP * 2)

        impure_title = Text("Impuro (Mixto)", font_size=28, color=RED)
        impure_title.move_to(RIGHT * 3.5 + UP * 2)

        self.play(Write(pure_title), Write(impure_title))

        # Grupo puro - solo manzanas
        pure_group = VGroup()
        for i in range(3):
            for j in range(3):
                apple = Circle(radius=0.2, color=RED, fill_opacity=0.8)
                apple.move_to(LEFT * 3.5 + UP * (0.5 - i * 0.5) + RIGHT * (j * 0.5 - 0.5))
                pure_group.add(apple)

        # Grupo impuro - mezcla
        impure_group = VGroup()
        colors = [RED, BLUE, RED, BLUE, RED, BLUE, BLUE, RED, BLUE]
        for i in range(3):
            for j in range(3):
                fruit = Circle(radius=0.2, color=colors[i * 3 + j], fill_opacity=0.8)
                fruit.move_to(RIGHT * 3.5 + UP * (0.5 - i * 0.5) + RIGHT * (j * 0.5 - 0.5))
                impure_group.add(fruit)

        self.play(FadeIn(pure_group), FadeIn(impure_group))
        self.wait(2)

        # Explicación
        pure_exp = Text("Gini = 0\n(Mejor)", font_size=24, color=GREEN)
        pure_exp.next_to(pure_group, DOWN)

        impure_exp = Text("Gini > 0\n(Necesita división)", font_size=24, color=RED)
        impure_exp.next_to(impure_group, DOWN)

        self.play(Write(pure_exp), Write(impure_exp))
        self.wait(2)

    def explain_gini_impurity(self):
        title = Text("Gini Impurity (Impureza de Gini)", font_size=42, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Fórmula
        formula_text = Text("Fórmula:", font_size=32, color=YELLOW)
        formula_text.move_to(UP * 2)

        formula = MathTex(
            r"Gini = 1 - \sum_{i=1}^{n} p_i^2",
            font_size=60,
            color=WHITE
        )
        formula.next_to(formula_text, DOWN, buff=0.5)

        self.play(Write(formula_text))
        self.play(Write(formula))
        self.wait(2)

        # Explicación de la fórmula
        explanation = VGroup(
            Text("donde:", font_size=28),
            MathTex(r"p_i", font_size=40, color=BLUE),
            Text("= probabilidad de clase i", font_size=24),
        ).arrange(RIGHT, buff=0.3)
        explanation.next_to(formula, DOWN, buff=0.8)

        self.play(Write(explanation))
        self.wait(2)

        # Ejemplo numérico
        self.play(FadeOut(formula_text), FadeOut(formula), FadeOut(explanation))

        example = Text("Ejemplo:", font_size=36, color=YELLOW)
        example.move_to(UP * 2.5)
        self.play(Write(example))

        # Escenario
        scenario = Text("10 frutas: 7 manzanas 🍎, 3 naranjas 🍊", font_size=28)
        scenario.next_to(example, DOWN, buff=0.5)
        self.play(Write(scenario))
        self.wait(1)

        # Cálculo paso a paso
        calc_steps = VGroup(
            MathTex(r"p_{manzana} = \frac{7}{10} = 0.7", font_size=36),
            MathTex(r"p_{naranja} = \frac{3}{10} = 0.3", font_size=36),
            MathTex(r"Gini = 1 - (0.7^2 + 0.3^2)", font_size=36),
            #MathTex(r"Gini = 1 - (0.49 + 0.09)", font_size=36),
            MathTex(r"Gini = 1 - 0.58 = 0.42", font_size=36, color=GREEN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        calc_steps.next_to(scenario, DOWN, buff=0.8)

        for step in calc_steps:
            self.play(Write(step))
            self.wait(1)

        self.wait(2)

        # Interpretación
        interpretation = Text(
            "Mayor Gini = Mayor impureza = Necesita división",
            font_size=28,
            color=ORANGE
        )
        interpretation.to_edge(DOWN)
        self.play(Write(interpretation))
        self.wait(3)

    # PARTE 3: CONSTRUCCION DEL ARBOL
    def part3_building_tree(self):
        part3_title = Text("Parte 3: Construyendo el árbol paso a paso", font_size=48, color=YELLOW)
        self.play(Write(part3_title))
        self.wait(1.5)
        self.play(part3_title.animate.to_edge(UP))

        # Mostrar dataset simple
        self.show_simple_dataset()
        self.wait(1)
        self.clear()

        # Construcción recursiva
        self.build_tree_recursively()

    def show_simple_dataset(self):
        title = Text("Dataset: Préstamo Bancario", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Crear tabla
        headers = ["Edad", "Ingreso", "Historial", "¿Aprobar?"]
        data = [
            ["Joven", "Bajo", "Bueno", "NO"],
            ["Joven", "Alto", "Bueno", "SÍ"],
            ["Adulto", "Alto", "Bueno", "SÍ"],
            ["Adulto", "Bajo", "Malo", "NO"],
            ["Mayor", "Alto", "Bueno", "SÍ"],
            ["Mayor", "Bajo", "Bueno", "NO"],
        ]

        table = self.create_table(headers, data)
        table.scale(0.7).move_to(DOWN * 0.5)

        self.play(Create(table))
        self.wait(2)

    def create_table(self, headers, data):
        table = VGroup()

        # Headers
        header_row = VGroup()
        for i, header in enumerate(headers):
            cell = Rectangle(height=0.5, width=1.8, color=BLUE, fill_opacity=0.3)
            text = Text(header, font_size=20, color=WHITE, weight=BOLD)
            text.move_to(cell.get_center())
            cell_group = VGroup(cell, text)
            cell_group.shift(RIGHT * i * 1.8)
            header_row.add(cell_group)

        table.add(header_row)

        # Data rows
        for j, row in enumerate(data):
            data_row = VGroup()
            for i, value in enumerate(row):
                color = GREEN if value == "SÍ" else (RED if value == "NO" else WHITE)
                cell = Rectangle(height=0.5, width=1.8, color=GRAY, fill_opacity=0.1)
                text = Text(value, font_size=18, color=color)
                text.move_to(cell.get_center())
                cell_group = VGroup(cell, text)
                cell_group.shift(RIGHT * i * 1.8 + DOWN * (j + 1) * 0.5)
                data_row.add(cell_group)
            table.add(data_row)

        return table

    def build_tree_recursively(self):
        title = Text("Construcción Recursiva del Árbol", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Paso 1: Calcular Gini para cada característica
        step1 = Text("Paso 1: Calcular Gini para cada característica", font_size=28, color=YELLOW)
        step1.move_to(UP * 2.5)
        self.play(Write(step1))
        self.wait(1)

        gini_results = VGroup(
            Text("Gini(Edad) = 0.35", font_size=26),
            Text("Gini(Ingreso) = 0.28  ← Menor Gini!", font_size=26, color=GREEN),
            Text("Gini(Historial) = 0.40", font_size=26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        gini_results.next_to(step1, DOWN, buff=0.5)

        self.play(Write(gini_results))
        self.wait(2)

        # Paso 2: Dividir por mejor característica
        step2 = Text("Paso 2: Dividir por 'Ingreso' (menor Gini)", font_size=28, color=YELLOW)
        step2.move_to(UP * 0.5)
        self.play(Write(step2))
        self.wait(1)

        # Mostrar división
        split_visual = self.create_split_visualization()
        split_visual.scale(0.6).move_to(DOWN * 1.5)
        self.play(Create(split_visual))
        self.wait(2)

        # Criterio de parada
        self.play(FadeOut(gini_results), FadeOut(split_visual))

        stop_title = Text("Criterios de Parada:", font_size=32, color=ORANGE)
        stop_title.move_to(UP * 1)

        stop_criteria = VGroup(
            Text("✓ Pureza perfecta (Gini = 0)", font_size=24),
            Text("✓ Profundidad máxima alcanzada", font_size=24),
            Text("✓ Número mínimo de muestras", font_size=24),
            Text("✓ No mejora significativa", font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        stop_criteria.next_to(stop_title, DOWN, buff=0.5)

        self.play(Write(stop_title))
        self.play(Write(stop_criteria), run_time=2)
        self.wait(3)

    def create_split_visualization(self):
        # Root node
        root = RoundedRectangle(corner_radius=0.15, height=0.8, width=2, color=BLUE, fill_opacity=0.3)
        root_text = Text("Ingreso", font_size=22)
        root_group = VGroup(root, root_text).move_to(UP * 1.5)

        # Left branch - Alto
        left_line = Line(root.get_bottom(), root.get_bottom() + DOWN + LEFT * 1.5)
        left_label = Text("Alto", font_size=18, color=GREEN).next_to(left_line, LEFT, buff=0.1)

        left_leaf = RoundedRectangle(corner_radius=0.15, height=0.7, width=1.5, color=GREEN, fill_opacity=0.5)
        left_text = Text("SÍ\nGini=0", font_size=20, color=WHITE)
        left_group = VGroup(left_leaf, left_text).move_to(root.get_bottom() + DOWN * 1.5 + LEFT * 2)

        # Right branch - Bajo
        right_line = Line(root.get_bottom(), root.get_bottom() + DOWN + RIGHT * 1.5)
        right_label = Text("Bajo", font_size=18, color=RED).next_to(right_line, RIGHT, buff=0.1)

        right_leaf = RoundedRectangle(corner_radius=0.15, height=0.7, width=1.5, color=RED, fill_opacity=0.5)
        right_text = Text("NO\nGini=0", font_size=20, color=WHITE)
        right_group = VGroup(right_leaf, right_text).move_to(root.get_bottom() + DOWN * 1.5 + RIGHT * 2)

        return VGroup(root_group, left_line, left_label, left_group, right_line, right_label, right_group)

    # PARTE 4: DATASET
    def part4_real_dataset(self):
        part4_title = Text("Parte 4: Dataset Real - Wine Quality", font_size=48, color=YELLOW)
        self.play(Write(part4_title))
        self.wait(1.5)
        self.play(part4_title.animate.to_edge(UP))

        # Mostrar dataset
        self.show_wine_dataset()
        self.wait(1)
        self.clear()

        # Decision boundaries
        self.show_decision_boundaries()
        self.wait(1)
        self.clear()

        # Métricas y overfitting
        self.show_metrics_and_overfitting()

    def show_wine_dataset(self):
        title = Text("Wine Dataset", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Características
        features = VGroup(
            Text("Características principales:", font_size=28, color=YELLOW),
            Text("• Alcohol", font_size=24),
            Text("• Acidez", font_size=24),
            Text("• pH", font_size=24),
            Text("• Azúcares", font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features.move_to(LEFT * 3 + UP * 0.5)

        # Target
        target = VGroup(
            Text("Objetivo:", font_size=28, color=YELLOW),
            Text("Clasificar calidad del vino", font_size=24),
            Text("(Bueno / Regular / Malo)", font_size=22, color=GRAY),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        target.move_to(RIGHT * 3 + UP * 0.5)

        self.play(Write(features), Write(target))
        self.wait(2)

        # Visualización de datos
        axes = Axes(
            x_range=[0, 15, 5],
            y_range=[0, 10, 5],
            x_length=5,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False
        ).move_to(DOWN * 1.5)

        x_label = Text("Alcohol %", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("Acidez", font_size=20).next_to(axes.y_axis, LEFT)

        # Puntos simulados
        np.random.seed(42)
        good_wines = VGroup(*[
            Dot(axes.c2p(np.random.uniform(11, 14), np.random.uniform(6, 9)), color=GREEN, radius=0.06)
            for _ in range(15)
        ])
        bad_wines = VGroup(*[
            Dot(axes.c2p(np.random.uniform(8, 11), np.random.uniform(2, 5)), color=RED, radius=0.06)
            for _ in range(15)
        ])

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(FadeIn(good_wines), FadeIn(bad_wines))
        self.wait(2)

        legend = VGroup(
            VGroup(Dot(color=GREEN, radius=0.08), Text("Bueno", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Dot(color=RED, radius=0.08), Text("Malo", font_size=20)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        legend.to_corner(UR)

        self.play(FadeIn(legend))
        self.wait(2)

    def show_decision_boundaries(self):
        title = Text("Fronteras de Decisión", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Crear ejes
        axes = Axes(
            x_range=[0, 15, 5],
            y_range=[0, 10, 5],
            x_length=6,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False
        ).move_to(ORIGIN)

        x_label = Text("Alcohol %", font_size=22).next_to(axes.x_axis, DOWN)
        y_label = Text("Acidez", font_size=22).next_to(axes.y_axis, LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Puntos
        np.random.seed(42)
        good_wines = VGroup(*[
            Dot(axes.c2p(np.random.uniform(11, 14), np.random.uniform(6, 9)), color=GREEN, radius=0.05)
            for _ in range(20)
        ])
        bad_wines = VGroup(*[
            Dot(axes.c2p(np.random.uniform(8, 11), np.random.uniform(2, 5)), color=RED, radius=0.05)
            for _ in range(20)
        ])

        self.play(FadeIn(good_wines), FadeIn(bad_wines))

        # Fronteras de decisión (líneas verticales y horizontales)
        boundary1 = DashedLine(
            axes.c2p(10.5, 0), axes.c2p(10.5, 10),
            color=YELLOW, stroke_width=3
        )
        boundary2 = DashedLine(
            axes.c2p(0, 5.5), axes.c2p(15, 5.5),
            color=YELLOW, stroke_width=3
        )

        self.play(Create(boundary1), Create(boundary2))
        self.wait(2)

        # Regiones
        region_good = Text("Región:\nBueno", font_size=18, color=GREEN)
        region_good.move_to(axes.c2p(13, 7.5))

        region_bad = Text("Región:\nMalo", font_size=18, color=RED)
        region_bad.move_to(axes.c2p(9, 3.5))

        self.play(Write(region_good), Write(region_bad))
        self.wait(3)

    def show_metrics_and_overfitting(self):
        title = Text("Métricas y Overfitting", font_size=44, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Métricas
        metrics_title = Text("Métricas de Evaluación:", font_size=32, color=YELLOW)
        metrics_title.move_to(UP * 2.2)
        self.play(Write(metrics_title))

        metrics = VGroup(
            VGroup(
                Text("Accuracy:", font_size=26, color=WHITE),
                Text("85%", font_size=26, color=GREEN, weight=BOLD)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Precision:", font_size=26, color=WHITE),
                Text("82%", font_size=26, color=GREEN, weight=BOLD)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Recall:", font_size=26, color=WHITE),
                Text("88%", font_size=26, color=GREEN, weight=BOLD)
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        metrics.move_to(LEFT * 3.5 + UP * 0.3)

        self.play(Write(metrics), run_time=2)
        self.wait(2)

        # Overfitting
        overfitting_title = Text("Problema: Overfitting", font_size=28, color=RED)
        overfitting_title.move_to(RIGHT * 2.5 + UP * 1.5)
        self.play(Write(overfitting_title))

        # Comparación
        comparison = VGroup(
            Text("Árbol Profundo:", font_size=22, color=ORANGE),
            Text("✓ Training: 98%", font_size=20, color=GREEN),
            Text("✗ Testing: 72%", font_size=20, color=RED),
            Text("", font_size=10),
            Text("Árbol Podado:", font_size=22, color=BLUE),
            Text("✓ Training: 85%", font_size=20, color=GREEN),
            Text("✓ Testing: 83%", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        comparison.move_to(RIGHT * 2.5 + DOWN * 0.5)

        self.play(Write(comparison), run_time=3)
        self.wait(2)

        # Soluciones
        solutions_title = Text("Soluciones:", font_size=28, color=GREEN)
        solutions_title.move_to(DOWN * 2.5 + LEFT * 4)

        solutions = VGroup(
            Text("• Limitar profundidad máxima", font_size=20),
            Text("• Poda del árbol (pruning)", font_size=20),
            Text("• Validación cruzada", font_size=20),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        solutions.next_to(solutions_title, RIGHT, buff=0.5)

        self.play(Write(solutions_title), Write(solutions))
        self.wait(3)

        # Final
        final_message = Text(
            "¡Los Decision Trees son poderosos pero necesitan regularización!",
            font_size=26,
            color=YELLOW
        )
        final_message.to_edge(DOWN, buff=0.5)
        self.play(Write(final_message))
        self.wait(3)