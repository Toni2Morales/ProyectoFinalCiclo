from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from .ConexionMongoDB import MongoDBManager
from PIL import Image as PILImage
import io
import os

class ScreenThree(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dibujar un fondo de color
        with self.canvas.before:
            Color(0.57, 0.37, 0.57, 0.39)  # Morado
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_background, pos=self.update_background)

        # Crear el gestor de MongoDB
        self.gestor = MongoDBManager("mongodb://localhost:27017/", "BaseMongoProyectoFinal", "Novelas")
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
            background_color=(0.57, 0.37, 0.57, 1))
        self.button2 = Button(
            text="Novelas",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 1))
        self.button3 = Button(
            text="Perfil",
            markup = True,
            background_color=(0.57, 0.37, 0.57, 1))

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
                text="TUS CREACIONES",
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
                text="[u]Incompletas[/u]",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.1, "y": 0.85},  # Parte superior izquierda
                background_color=(0.57, 0.37, 0.57, 1),
                markup = True
            )
            button_subsection_2 = Button(
                text="Completas",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.6, "y": 0.85},  # Parte superior derecha
                background_color=(0.57, 0.37, 0.57, 1),
                markup = True
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
            
            resultados = self.gestor.consultar_documentos()
            # Añadir contenido inicial al contenedor
            for novela in resultados:  # Ejemplo: añadir múltiples elementos
                box_ly = BoxLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.7,
                    pos_hint={"x": 0.25},
                )
                float_ly = FloatLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.5,
                    pos_hint={"x": 0.25},
                )
                Button1 = Button(
                    text=novela["páginas"][0] + "\nLeer más...",
                    background_normal='',
                    background_color=(0.57, 0.37, 0.57, 0.39),
                    pos_hint={"x": 0.4, "y": 0},
                    size_hint=(0.6, 1),
                    valign = "center",
                    halign = "left",
                    text_size=(None, None))
                Button1.bind(
                    size=lambda instance, value: setattr(instance, 'text_size', value)
                )

                # Decodificar la imagen de la novela
                # Convertir la imagen de bytes a un objeto PIL 
                imagen = PILImage.open(io.BytesIO(novela["img"]))
                nombre_archivo = novela["nombre"].replace(" ", "_").replace("/", "_")

                imagen.save("../assets/imgTemporales/" + nombre_archivo + ".png")  # Guardar la imagen en un archivo
                # Guardar la imagen decodificada en un archivo temporal

                float_ly.add_widget(Button1)
                float_ly.add_widget(Button(
                    pos_hint={"x": 0, "y": 0.9},
                    background_normal = "assets/images/CorazonBlanco.png",
                    size_hint=(0.02, 0.02))
                )
                float_ly.add_widget(Button(
                    background_normal = "assets/images/Comentarios.png",
                    pos_hint={"x": 0.1, "y": 0.9},
                    size_hint=(0.02, 0.02))
                )
                float_ly.add_widget(Image(
                    source="../assets/imgTemporales/" + nombre_archivo + ".png",
                    fit_mode = "scale-down",
                    pos_hint={"x": -0.28, "y": 0},
                    size_hint=(0.7, 0.7),
                    keep_ratio=True)  # Mantiene la proporción de aspecto
                )

                box_ly.add_widget(float_ly)
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

            # Diseño para la sección C
            section_c_layout = FloatLayout(size_hint=(1, 1))

            # Crear un botón para seleccionar la imagen
            select_image_button = Button(
                text="Seleccionar Imagen",
                background_normal="assets/images/Perfil.png",  # Imagen de muestra
                size_hint=(None, None),  # Desactivamos el ajuste proporcional
                size=(180, 180),
                pos_hint={"x": 0.1, "y": 0.73}
            )

            # Función para abrir el FileChooser
            def open_file_chooser(instance):
                # Crear el FileChooserPopup
                file_chooser = FileChooserListView(
                    size_hint=(0.8, 0.8),
                    pos_hint={"x": 0.1, "y": 0.2},  # Ajusta la posición
                )
                
                # Botón de confirmación
                confirm_button = Button(
                    text="Confirmar selección",
                    size_hint=(0.8, 0.1),
                    pos_hint={"x": 0.1, "y": 0.05}
                )
                
                # Contenedor del popup (FileChooser + botón de confirmación)
                popup_content = FloatLayout()
                popup_content.add_widget(file_chooser)
                popup_content.add_widget(confirm_button)
                
                popup = Popup(
                    title="Selecciona una imagen",
                    content=popup_content,
                    size_hint=(0.9, 0.9)
                )
                
                def confirm_selection(instance):
                    if file_chooser.selection:  # Verifica si hay selección
                        select_image_button.background_normal = file_chooser.selection[0]
                        popup.dismiss()  # Cierra el Popup
                
                # Vincula el botón de confirmación al evento
                confirm_button.bind(on_press=confirm_selection)
                
                popup.open()


            # Vincular el botón con la función de abrir el FileChooser
            select_image_button.bind(on_press=open_file_chooser)

            # Añadir el botón al diseño de la sección C
            section_c_layout.add_widget(select_image_button)

            # Añadir el NICKNAME en grande debajo del botón
            nickname_label = Label(
                text="NICKNAME",  # Aquí puedes cambiar el texto a lo que quieras
                font_size=48,
                size_hint=(None, None),
                size=(400, 100),
                pos_hint={"x": 0, "y": 0.6},
                bold=True,
                color=(1, 1, 1, 1)  # Color blanco
            )
            section_c_layout.add_widget(nickname_label)

            # Crear los 3 rectángulos azules con texto dentro
            def create_rectangle_with_text(pos_hint, text):
                # Rectángulo Azul
                with section_c_layout.canvas:
                    Color(0, 0.5, 0.5, 1)  # Color azul
                    rect = Rectangle(
                        pos=(pos_hint['x'] * self.width, pos_hint['y'] * self.height),
                        size=(self.width * 0.3, 50)  # Tamaño del rectángulo
                    )
                
                # Crear un Label dentro del rectángulo
                rect_label = Label(
                    text=text,
                    font_size=24,
                    size_hint=(None, None),
                    size=(self.width * 0.25, 100),
                    pos_hint=pos_hint,
                    color=(1, 1, 1, 1),  # Color blanco
                    valign="middle",
                    halign="center"
                )
                
                section_c_layout.add_widget(rect_label)

            # Llamar a la función para crear los rectángulos con texto
            create_rectangle_with_text(pos_hint={"x": 0.1, "y": 0.5}, text="24 seguidos")
            create_rectangle_with_text(pos_hint={"x": 0.35, "y": 0.5}, text="65 seguidores")
            create_rectangle_with_text(pos_hint={"x": 0.65, "y": 0.5}, text="4 amigos")
            
            section_c_layout.add_widget(Label(
                text="Logros",
                font_size=24,
                size_hint=(0, 0),
                pos_hint={"x": 0.15, "y": 0.5}
            ))

            section_c_layout.add_widget(Button(
                text="Logro1",
                size_hint=(0.3, 0.3),
                pos_hint={"x": 0.1, "y": 0.1}
            ))
            section_c_layout.add_widget(Button(
                text="Logro2",
                size_hint=(0.3, 0.3),
                pos_hint={"x": 0.4, "y": 0.1}
            ))
            section_c_layout.add_widget(Button(
                text="Logro3",
                size_hint=(0.3, 0.3),
                pos_hint={"x": 0.7, "y": 0.1}
            ))
            # Agregar el diseño a la sección dinámica
            self.section_layout.add_widget(section_c_layout)



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
                text="[u]Incompletas[/u]",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.1, "y": 0.85},  # Parte superior izquierda
                background_color=(0.57, 0.37, 0.57, 1),
                markup = True
            )
            button_subsection_2 = Button(
                text="Completas",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.6, "y": 0.85},  # Parte superior derecha
                background_color=(0.57, 0.37, 0.57, 1),
                markup = True
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

            resultados = self.gestor.consultar_documentos()
            # Añadir contenido inicial al contenedor
            for novela in resultados:  # Ejemplo: añadir múltiples elementos
                box_ly = BoxLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.7,
                    pos_hint={"x": 0.25},
                )
                float_ly = FloatLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.5,
                    pos_hint={"x": 0.25},
                )
                Button1 = Button(
                    text=novela["páginas"][0] + "\nLeer más...",
                    background_normal='',
                    background_color=(0.57, 0.37, 0.57, 0.39),
                    pos_hint={"x": 0.4, "y": 0},
                    size_hint=(0.6, 1),
                    valign = "center",
                    halign = "left",
                    text_size=(None, None))
                Button1.bind(
                    size=lambda instance, value: setattr(instance, 'text_size', value)
                )

                float_ly.add_widget(Button1)
                float_ly.add_widget(Button(
                    pos_hint={"x": 0, "y": 0.9},
                    background_normal = "assets/images/CorazonBlanco.png",
                    size_hint=(0.02, 0.02))
                )
                float_ly.add_widget(Button(
                    background_normal = "assets/images/Comentarios.png",
                    pos_hint={"x": 0.1, "y": 0.9},
                    size_hint=(0.02, 0.02))
                )
                float_ly.add_widget(Image(
                    source='assets/images/LosJuegosDelHambreSinsajoParte1.jpg',
                    fit_mode = "scale-down",
                    pos_hint={"x": -0.28, "y": 0},
                    size_hint=(0.7, 0.7),
                    keep_ratio=True)  # Mantiene la proporción de aspecto
                )

                box_ly.add_widget(float_ly)
                scroll_content.add_widget(box_ly)

            # Añadir el contenido al ScrollView
            scroll_view.add_widget(scroll_content)

            # Añadir el ScrollView al diseño principal de la sección B
            section_b_layout.add_widget(scroll_view)

            # Agregar el diseño completo de la Sección B al área dinámica
            self.section_layout.add_widget(section_b_layout)

        elif subsection_number == 2:
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
                background_color=(0.57, 0.37, 0.57, 1),
                markup = True
            )
            button_subsection_2 = Button(
                text="[u]Completas[/u]",
                size_hint=(0.3, 0.1),
                pos_hint={"x": 0.6, "y": 0.85},  # Parte superior derecha
                background_color=(0.57, 0.37, 0.57, 1),
                markup = True
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
            scroll_content.bind(minimum_height=scroll_content.setter("height"))  # Ajustar altura 
            
            resultados = self.gestor.consultar_documentos()
            # Añadir contenido inicial al contenedor            
            for novela in resultados:  # Ejemplo: añadir múltiples elementos
                box_ly = BoxLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.7,
                    pos_hint={"x": 0.25},
                )
                float_ly = FloatLayout(
                    size_hint_y=None,
                    height=200,
                    size_hint_x=0.5,
                    pos_hint={"x": 0.25},
                )
                Button1 = Button(
                    text=novela["páginas"][0] + "\nLeer más...",
                    background_normal='',
                    background_color=(0.57, 0.37, 0.57, 0.39),
                    pos_hint={"x": 0.4, "y": 0},
                    size_hint=(0.6, 1),
                    valign = "center",
                    halign = "left",
                    text_size=(None, None))
                Button1.bind(
                    size=lambda instance, value: setattr(instance, 'text_size', value)
                )

                float_ly.add_widget(Button1)
                float_ly.add_widget(Button(
                    pos_hint={"x": 0, "y": 0.9},
                    background_normal = "assets/images/CorazonBlanco.png",
                    size_hint=(0.02, 0.02))
                )
                float_ly.add_widget(Button(
                    background_normal = "assets/images/Comentarios.png",
                    pos_hint={"x": 0.1, "y": 0.9},
                    size_hint=(0.02, 0.02))
                )
                float_ly.add_widget(Image(
                    source='assets/images/LosJuegosDelHambreSinsajoParte1.jpg',
                    fit_mode = "scale-down",
                    pos_hint={"x": -0.28, "y": 0},
                    size_hint=(0.7, 0.7),
                    keep_ratio=True)  # Mantiene la proporción de aspecto
                )

                box_ly.add_widget(float_ly)
                scroll_content.add_widget(box_ly)

            # Añadir el contenido al ScrollView
            scroll_view.add_widget(scroll_content)

            # Añadir el ScrollView al diseño principal de la sección B
            section_b_layout.add_widget(scroll_view)

            # Agregar el diseño completo de la Sección B al área dinámica
            self.section_layout.add_widget(section_b_layout)

    def update_background(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos