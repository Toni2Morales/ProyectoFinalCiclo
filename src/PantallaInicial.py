from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
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
