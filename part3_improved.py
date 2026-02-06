from manim import *

# NOTA PARA EL GRUPO:
# Copiar estos métodos dentro de la clase principal en el archivo final.

class Part3Scene(Scene): 
    def construct(self):
        self.part3_building_tree()

    def part3_building_tree(self):
        # 1. Título
        part3_title = Text("Parte 3: Construyendo el árbol", font_size=40, color=YELLOW)
        self.play(Write(part3_title))
        self.wait(1)
        self.play(part3_title.animate.to_edge(UP))

        # 2. Mostrar Dataset
        headers = ["Edad", "Ingreso", "Historial", "¿Aprobar?"]
        data = [
            ["Joven", "Bajo", "Bueno", "NO"],   # Fila 0
            ["Joven", "Alto", "Bueno", "SÍ"],   # Fila 1
            ["Adulto", "Alto", "Bueno", "SÍ"],  # Fila 2
            ["Adulto", "Bajo", "Malo", "NO"],   # Fila 3
            ["Mayor", "Alto", "Bueno", "SÍ"],   # Fila 4
            ["Mayor", "Bajo", "Bueno", "NO"],   # Fila 5
        ]
        
        # Creamos la tabla y la mostramos
        table_group = self.create_table(headers, data)
        table_group.scale(0.8).move_to(UP * 0.5)
        self.play(Create(table_group))
        self.wait(1)

        # 3. Paso 1: Selección de Característica
        step1 = Text("Paso 1: Evaluar características", font_size=24, color=YELLOW).to_edge(UP, buff=1.5)
        self.play(Write(step1))
        
        # Resaltar la columna "Ingreso" (Índice 1)
        highlights = VGroup()
        for row in table_group:
            highlight = SurroundingRectangle(row[1], color=YELLOW, buff=0.05)
            highlights.add(highlight)
            
        self.play(Create(highlights))
        
        gini_text = Text("Gini(Ingreso) = 0.28 (El mejor)", font_size=24, color=GREEN)
        gini_text.next_to(table_group, DOWN)
        self.play(Write(gini_text))
        self.wait(2)
        
        # Limpiamos resaltados pero DEJAMOS la tabla
        self.play(FadeOut(highlights), FadeOut(step1), FadeOut(gini_text))

        # 4. Paso 2: El Split Animado
        step2 = Text("Paso 2: Dividir los datos", font_size=24, color=YELLOW).to_edge(UP, buff=1.5)
        self.play(Write(step2))

        # Crear el nodo raíz visualmente
        root_node = RoundedRectangle(corner_radius=0.1, height=0.6, width=2, color=BLUE)
        root_text = Text("¿Ingreso?", font_size=20)
        root_group = VGroup(root_node, root_text).move_to(UP * 2)
        
        # Transformar el header de la tabla en el nodo raíz
        self.play(
            Transform(table_group[0][1], root_group), 
            FadeOut(table_group[0][0]), 
            FadeOut(table_group[0][2]), 
            FadeOut(table_group[0][3])  
        )
        self.wait(0.5)

        # Animar separación de filas
        # table_group[1] es la fila de datos 0
        left_target = UP * 0.5 + LEFT * 3
        right_target = UP * 0.5 + RIGHT * 3
        
        anims = []
        group_high = VGroup()
        group_low = VGroup()

        for i, row_data in enumerate(data):
            row_visual = table_group[i+1] # +1 porque el 0 es el header
            if row_data[1] == "Alto":
                target = left_target + DOWN * (len(group_high) * 0.6)
                anims.append(row_visual.animate.move_to(target))
                group_high.add(row_visual)
            else:
                target = right_target + DOWN * (len(group_low) * 0.6)
                anims.append(row_visual.animate.move_to(target))
                group_low.add(row_visual)

        self.play(*anims, run_time=2)
        
        # Etiquetas de las ramas
        lbl_high = Text("Alto", font_size=18, color=GREEN).next_to(root_group, DL, buff=0.5)
        lbl_low = Text("Bajo", font_size=18, color=RED).next_to(root_group, DR, buff=0.5)
        line_high = Line(root_group.get_bottom(), lbl_high.get_top())
        line_low = Line(root_group.get_bottom(), lbl_low.get_top())
        
        self.play(Create(line_high), Write(lbl_high), Create(line_low), Write(lbl_low))
        self.wait(1)

        # 5. Transformar filas en Hojas
        leaf_yes = RoundedRectangle(height=0.8, width=1.5, color=GREEN, fill_opacity=0.2)
        text_yes = Text("Aprobar:\nSÍ", font_size=20, color=GREEN)
        leaf_yes_grp = VGroup(leaf_yes, text_yes).move_to(left_target + DOWN * 1.5)
        
        leaf_no = RoundedRectangle(height=0.8, width=1.5, color=RED, fill_opacity=0.2)
        text_no = Text("Aprobar:\nNO", font_size=20, color=RED)
        leaf_no_grp = VGroup(leaf_no, text_no).move_to(right_target + DOWN * 1.5)

        self.play(
            Transform(group_high, leaf_yes_grp),
            Transform(group_low, leaf_no_grp)
        )
        self.wait(1)

        final_text = Text("Gini = 0 (Hojas Puras)", font_size=24, color=YELLOW).move_to(DOWN * 2.5)
        self.play(Write(final_text))
        self.wait(2)
        
        self.clear()
        stop_title = Text("Criterios de Parada", font_size=32, color=ORANGE).to_edge(UP)
        criteria = VGroup(
            Text("1. Pureza Total (Gini = 0)", font_size=24),
            Text("2. Profundidad Máxima", font_size=24),
            Text("3. Mínimo de muestras en hoja", font_size=24)
        ).arrange(DOWN, buff=0.5)
        self.play(Write(stop_title), Write(criteria))
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
