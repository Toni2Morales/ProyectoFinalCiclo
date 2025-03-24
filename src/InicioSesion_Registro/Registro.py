from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
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