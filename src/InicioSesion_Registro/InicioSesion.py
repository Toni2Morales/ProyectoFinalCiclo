from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

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
            size_hint_y=None,
            size_hint_x = 0.5,
            pos_hint={"x": 0.25, "y": 0.6},
            height = 30
        )

        textInput2 = TextInput(
            hint_text="Contraseña",
            multiline=False,  # Para permitir una sola línea de texto
            size_hint_y=None,
            size_hint_x = 0.5,
            pos_hint={"x": 0.25, "y": 0.5},
            height = 30
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
