from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

# Pantalla principal con dos botones
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar el fondo morado
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.39)  # Morado en formato RGBA
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Actualizar el fondo al cambiar de tamaño o posición
        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        button1 = Button(
            text="Iniciar Sesión",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.5}
        )
        button2 = Button(
            text="Registrarse",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.3}
        )


        # Vincular botones a las funciones para cambiar de pantalla
        button1.bind(on_press=self.go_to_screen_one)
        button2.bind(on_press=self.go_to_screen_two)

        # Añadir widgets al diseño
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def go_to_screen_one(self, instance):
        self.manager.current = "screen_one"  # Cambia a la pantalla 1

    def go_to_screen_two(self, instance):
        self.manager.current = "screen_two"  # Cambia a la pantalla 2

# Pantalla 1
class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar el fondo morado
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.39)  # Morado
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        label = Label(
            text="INICIAR SESIÓN",
            font_size=35,
            size_hint=(0.5, 0.2),
            pos_hint={"x": 0.25, "y": 0.7}
        )
        button2 = Button(
            text="<----------------------------------------------------------------",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0, "y": 0.9},
            background_normal="",
            background_color = (0, 0, 0, 0)
        )

        button1 = Button(
            text="---------------------------------------------------------------->",
            size_hint=(0.4, 0.08),
            pos_hint={"x": 0.3, "y": 0.35},
            background_normal="",
            background_color = (0, 0, 0, 0)
        )

        textInput1 = TextInput(
            hint_text="Correo electronico",
            multiline=False,  # Para permitir una sola línea de texto
            size_hint=(0.5, 0.05), 
            pos_hint={"x": 0.25, "y": 0.6}
        )

        textInput2 = TextInput(
            hint_text="Contraseña",
            multiline=False,  # Para permitir una sola línea de texto
            size_hint=(0.5, 0.05),
            pos_hint={"x": 0.25, "y": 0.5}
        )

        button1.bind(on_press=lambda x: setattr(self.manager, 'current', 'screen_three') if textInput1.text == "correo" and textInput2.text == "contra" else print("Incorrecto"))
        button2.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        
        layout.add_widget(textInput1)
        layout.add_widget(textInput2)
        layout.add_widget(label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

#Pantalla 2
class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar el fondo morado
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.39)  # Morado
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        label = Label(
            text="REGISTRO",
            font_size=35,
            size_hint=(0.5, 0.2),
            pos_hint={"x": 0.25, "y": 0.7}
        )
        button = Button(
            text="Volver al menú",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.3}
        )

        button.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))

        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos



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
            text="Sección A",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 0.39))
        self.button2 = Button(
            text="Sección B",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 0.39))
        self.button3 = Button(
            text="Sección C",
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
            self.button1.text = "[u]Sección A[/u]"
            self.button2.text = "Sección B"
            self.button3.text = "Sección C"
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
            self.button1.text = "Sección A"
            self.button2.text = "[u]Sección B[/u]"
            self.button3.text = "Sección C"
            self.section_layout.add_widget(Label(
                text="Esta es la Sección B",
                font_size=24,
                size_hint=(0.8, 0.2),
                pos_hint={"x": 0.1, "y": 0.6}
            ))
        elif section_name == "Sección C":
            self.button1.text = "Sección A"
            self.button2.text = "Sección B"
            self.button3.text = "[u]Sección C[/u]"
            self.section_layout.add_widget(Label(
                text="Esta es la Sección C",
                font_size=24,
                size_hint=(0.8, 0.2),
                pos_hint={"x": 0.1, "y": 0.6}
            ))

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

# Clase principal de la aplicación
class MyApp(App):
    def build(self):
        # Crear el ScreenManager y añadir las pantallas
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))  # Pantalla principal
        sm.add_widget(ScreenOne(name="screen_one"))  # Pantalla 1
        sm.add_widget(ScreenTwo(name="screen_two"))  # Pantalla 2
        sm.add_widget(ScreenThree(name="screen_three"))
        return sm


# Ejecutar la aplicación
if __name__ == "__main__":
    MyApp().run()
