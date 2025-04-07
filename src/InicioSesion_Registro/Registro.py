from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from ..ConexionMySQL import ejecutar_consulta
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

        button1 = Button(
            text="---------------------------------------------------------------->",
            size_hint=(0.4, 0.08),
            pos_hint={"x": 0.3, "y": 0.35},
            background_normal="",
            background_color = (0, 0, 0, 0)
        )

        button2 = Button(
            text="<----------------------------------------------------------------",
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0, "y": 0.9},
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

        textInput3 = TextInput(
            hint_text="Repetir Contraseña",
            multiline=False,  # Para permitir una sola línea de texto
            size_hint_y=None,
            size_hint_x = 0.5,
            pos_hint={"x": 0.25, "y": 0.45},
            height = 30
        )
        label = Label(
            text="REGISTRO",
            font_size=35,
            size_hint=(0.5, 0.2),
            pos_hint={"x": 0.25, "y": 0.7}
        )

        label2 = Label(
            text="",
            font_size=18,
            size_hint=(0.5, 0.2),
            pos_hint={"x": 0.25, "y": 0.2}
        )
    
        def validate_and_switch(instance):
            if textInput2.text == textInput3.text and not comprobar_correo_unico(textInput1.text):
                # Consulta parametrizada para evitar inyección SQL
                consulta = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"
                parametros = (textInput1.text, textInput2.text)
                ejecutar_consulta(consulta, parametros)
                label2.text = "Te has registrado correctamente"
            elif textInput2.text != textInput3.text:
                label2.text = "Las contraseñas deben ser iguales"
            else:
                label2.text = "El correo ya ha sido registrado anteriormente"

        def comprobar_correo_unico(correo):
            # Consulta parametrizada para evitar inyección SQL
            consulta = "SELECT * FROM usuarios WHERE correo = %s"
            parametros = (correo,)
            resultados = ejecutar_consulta(consulta, parametros)

            # Verificar si el correo ya existe
            for fila in resultados:
                if fila[1] == correo:
                    return True
            return False


        button1.bind(on_press=validate_and_switch)
        button2.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(textInput1)
        layout.add_widget(textInput2)
        layout.add_widget(textInput3)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(label)
        layout.add_widget(label2)
        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos