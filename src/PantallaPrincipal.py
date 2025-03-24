from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ScreenThree(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar un fondo de color
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.39)  # Morado
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_background, pos=self.update_background)

        # Diseño principal
        layout = FloatLayout()

        # Área dinámica donde cambiarán las secciones
        self.section_layout = FloatLayout(size_hint=(1, 0.9), pos_hint={"x": 0, "y": 0.1})
        layout.add_widget(self.section_layout)

        # Barra de botones fija en la parte inferior
        buttons_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.1),  # Altura del 10% de la pantalla
            pos_hint={"x": 0, "y": 0}  # Pegada a la parte inferior
        )

        self.button1 = Button(
            text="Creación",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 0.39))
        self.button2 = Button(
            text="Novelas",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 0.39))
        self.button3 = Button(
            text="Perfil",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 0.39))

        # Vincular los botones para cambiar secciones
        self.button1.bind(on_press=lambda x: self.change_section("Sección A"))
        self.button2.bind(on_press=lambda x: self.change_section("Sección B"))
        self.button3.bind(on_press=lambda x: self.change_section("Sección C"))

        # Añadir botones a la barra
        buttons_layout.add_widget(self.button1)
        buttons_layout.add_widget(self.button2)
        buttons_layout.add_widget(self.button3)

        # Añadir la barra de botones y el área dinámica al diseño principal
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

        # Configurar la sección inicial automáticamente
        self.change_section("Sección B")

    def change_section(self, section_name):
        """Actualiza la sección mostrada en el área dinámica."""
        # Limpiar los widgets actuales del área dinámica
        self.section_layout.clear_widgets()

        # Cambiar contenido según la sección
        if section_name == "Sección A":
            self.button1.text = "[u]CREACIÓN[/u]"
            self.button2.text = "NOVELAS"
            self.button3.text = "PERFIL"
            self.section_layout.add_widget(Label(
                text="Esta es la Sección A",
                font_size=24,
                size_hint=(0.8, 0.2),
                pos_hint={"x": 0.1, "y": 0.6}
            ))
            self.section_layout.add_widget(Button(
                text="Botón en Sección A",
                size_hint=(0.4, 0.1),
                pos_hint={"x": 0.3, "y": 0.4}
            ))
        elif section_name == "Sección B":
            self.button1.text = "CREACIÓN"
            self.button2.text = "[u]NOVELAS[/u]"
            self.button3.text = "PERFIL"

            # Crear un FloatLayout para la sección B
            section_b_layout = FloatLayout(size_hint=(1, 1))

            # Crear los botones superiores para las subsecciones
            button_subsection_1 = Button(
                text="Incompletas",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.1, "y": 0.85},  # Parte superior izquierda
                background_normal='',
                background_color=(0.3, 0.5, 0.8, 1)  # Azul claro
            )
            button_subsection_2 = Button(
                text="completas",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.6, "y": 0.85},  # Parte superior derecha
                background_normal='',
                background_color=(0.8, 0.5, 0.3, 1)  # Naranja claro
            )

            # Vincular los botones de subsecciones a funciones
            button_subsection_1.bind(on_press=lambda x: self.show_subsection(scroll_content, 1))
            button_subsection_2.bind(on_press=lambda x: self.show_subsection(scroll_content, 2))

            # Añadir los botones de subsección al diseño de la Sección B
            section_b_layout.add_widget(button_subsection_1)
            section_b_layout.add_widget(button_subsection_2)

            # Crear un ScrollView para permitir el desplazamiento
            scroll_view = ScrollView(
                size_hint=(1, 0.75),  # Ajustar el tamaño para dar espacio a los botones superiores
                pos_hint={"x": 0, "y": 0}
            )

            # Contenedor dentro del ScrollView (BoxLayout)
            scroll_content = BoxLayout(
                orientation="vertical",  # Apilar los widgets verticalmente
                size_hint_y=None         # Habilitar desplazamiento vertical
            )
            scroll_content.bind(minimum_height=scroll_content.setter("height"))  # Ajustar altura dinámica

            # Añadir contenido inicial al contenedor
            for i in range(20):  # Ejemplo: añadir múltiples elementos
                box_ly = BoxLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.5,
                    pos_hint={"x": 0.25},
                )
                float_ly = FloatLayout()

                float_ly.add_widget(Label(
                    text=f"Elemento {i + 1}",
                    font_size=24,
                    size_hint=(0.8, 0.2),
                    pos_hint={"x": 0.1, "y": 0.6}
                ))
                box_ly.add_widget(float_ly)
                box_ly.add_widget(Button(
                    text=f"Elemento {i + 1}",
                    background_normal='',
                    background_color=(0.57, 0.37, 0.57, 0.39)
                ))
                scroll_content.add_widget(box_ly)

            # Añadir el contenido al ScrollView
            scroll_view.add_widget(scroll_content)

            # Añadir el ScrollView al diseño principal de la sección B
            section_b_layout.add_widget(scroll_view)

            # Agregar el diseño completo de la Sección B al área dinámica
            self.section_layout.add_widget(section_b_layout)

        elif section_name == "Sección C":
            self.button1.text = "CREACIÓN"
            self.button2.text = "NOVELAS"
            self.button3.text = "[u]PERFIL[/u]"
            self.section_layout.add_widget(Label(
                text="Esta es la Sección C",
                font_size=24,
                size_hint=(0.8, 0.2),
                pos_hint={"x": 0.1, "y": 0.6}
            ))
    def show_subsection(self, scroll_content, subsection_number):
        """Actualizar el contenido según la subsección seleccionada."""
        # Limpiar el contenido actual del scroll_content
        scroll_content.clear_widgets()

        # Generar contenido para la subsección específica
        if subsection_number == 1:
            self.button1.text = "CREACIÓN"
            self.button2.text = "[u]NOVELAS[/u]"
            self.button3.text = "PERFIL"

            # Crear un FloatLayout para la sección B
            section_b_layout = FloatLayout(size_hint=(1, 1))

            # Crear los botones superiores para las subsecciones
            button_subsection_1 = Button(
                text="Incompletas",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.1, "y": 0.85},  # Parte superior izquierda
                background_normal='',
                background_color=(0.3, 0.5, 0.8, 1)  # Azul claro
            )
            button_subsection_2 = Button(
                text="Completas",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.6, "y": 0.85},  # Parte superior derecha
                background_normal='',
                background_color=(0.8, 0.5, 0.3, 1)  # Naranja claro
            )

            # Vincular los botones de subsecciones a funciones
            button_subsection_1.bind(on_press=lambda x: self.show_subsection(scroll_content, 1))
            button_subsection_2.bind(on_press=lambda x: self.show_subsection(scroll_content, 2))

            # Añadir los botones de subsección al diseño de la Sección B
            section_b_layout.add_widget(button_subsection_1)
            section_b_layout.add_widget(button_subsection_2)

            # Crear un ScrollView para permitir el desplazamiento
            scroll_view = ScrollView(
                size_hint=(1, 0.75),  # Ajustar el tamaño para dar espacio a los botones superiores
                pos_hint={"x": 0, "y": 0}
            )

            # Contenedor dentro del ScrollView (BoxLayout)
            scroll_content = BoxLayout(
                orientation="vertical",  # Apilar los widgets verticalmente
                size_hint_y=None         # Habilitar desplazamiento vertical
            )
            scroll_content.bind(minimum_height=scroll_content.setter("height"))  # Ajustar altura dinámica

            # Añadir contenido inicial al contenedor
            for i in range(20):  # Ejemplo: añadir múltiples elementos
                box_ly = BoxLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.5,
                    pos_hint={"x": 0.25},
                )
                float_ly = FloatLayout()

                float_ly.add_widget(Label(
                    text=f"Elemento {i + 1}",
                    font_size=24,
                    size_hint=(0.8, 0.2),
                    pos_hint={"x": 0.1, "y": 0.6}
                ))
                box_ly.add_widget(float_ly)
                box_ly.add_widget(Button(
                    text=f"Elemento {i + 1}",
                    background_normal='',
                    background_color=(0.57, 0.37, 0.57, 0.39)
                ))
                scroll_content.add_widget(box_ly)

            # Añadir el contenido al ScrollView
            scroll_view.add_widget(scroll_content)

            # Añadir el ScrollView al diseño principal de la sección B
            section_b_layout.add_widget(scroll_view)

            # Agregar el diseño completo de la Sección B al área dinámica
            self.section_layout.add_widget(section_b_layout)

        elif subsection_number == 2:
            for i in range(10):
                scroll_content.add_widget(Label(
                    text=f"Elemento en Subsección 2 - {i + 1}",
                    font_size=20,
                    size_hint_y=None,
                    height=50
                ))

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos