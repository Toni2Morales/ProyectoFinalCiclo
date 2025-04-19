from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src import MainScreen, ScreenOne, ScreenTwo, ScreenThree
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
