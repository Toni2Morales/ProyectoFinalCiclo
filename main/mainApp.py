from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
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
            Color(0.57, 0.37, 0.57, 0.2)  # Morado en formato RGBA
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Actualizar el fondo al cambiar de tamaño o posición
        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        button1 = Button(
            text="Registrarse",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.3}
        )
        button2 = Button(
            text="Iniciar Sesión",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.5}
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

#Pantalla 1
class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar el fondo morado
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.2)  # Morado
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        label = Label(
            text="Esta es la Pantalla 2",
            font_size=24,
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
            Color(0.2, 0.6, 0.8, 1)  # Azul
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        # Etiqueta (Label) para esta pantalla
        label = Label(
            text="¡Bienvenido a la nueva pantalla!",
            font_size=24,
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.4}
        )
        layout.add_widget(label)
        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

# Pantalla 2
class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar el fondo morado
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.2)  # Morado
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_background, pos=self.update_background)

        # Usar FloatLayout para esta pantalla
        layout = FloatLayout()

        label = Label(
            text="Esta es la Pantalla 1",
            font_size=24,
            size_hint=(0.5, 0.2),
            pos_hint={"x": 0.25, "y": 0.7}
        )
        button1 = Button(
            text="Volver al menú",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.3, "y": 0.2}
        )

        button2 = Button(
            text="Enviar",
            size_hint=(0.4, 0.08),
            pos_hint={"x": 0.3, "y": 0.35}
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
        button1.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        button2.bind(on_press=lambda x: setattr(self.manager, 'current', 'screen_three') if textInput1.text == "correo" and textInput2.text == "contra" else print("Incorrecto"))

        layout.add_widget(textInput1)
        layout.add_widget(textInput2)
        layout.add_widget(label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

# Pantalla 1

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
