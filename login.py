from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window


Window.clearcolor = 0, 1, 1, 1  # Remove the comma at the end

# Define the screens
class FirstPage(Screen):
    my_text = StringProperty("Details Here")

    def on_press_button(self):
        """Called when the Register Here button is pressed"""
        self.my_text = "Registration Successful"


class SecondPage(Screen):
    pass


class HomePage(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Tutorial.kv")

# Define the app
class TutorialApp(App):
    def build(self):
        self.title = "My Tutorial App"  # Add a title to the app
        return kv


if __name__ == "__main__":
    TutorialApp().run()