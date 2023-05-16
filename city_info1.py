from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import from_api


class cityGrid(GridLayout):
    def __init__(self, **kwargs):
        super(cityGrid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Enter city name: "))
        self.city_input = TextInput()
        self.add_widget(self.city_input)

        self.search_button = Button(text="Search")
        self.search_button.bind(on_press=self.search)
        self.add_widget(self.search_button)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def search(self, instance):
        choice = self.city_input.text
        city_names = from_api.all_cities
        found = False
        for c in city_names:
            if choice == c["name"]:
                result = ""
                for key, value in c.items():
                    result += f"{key}: {value}\n"
                self.result_label.text = result
                found = True
                break

        if not found:
            self.result_label.text = "city name not found in city names"


class City_App(App):
    def build(self):
        return cityGrid()


if __name__ == "__main__":
    City_App().run()