from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


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
        city_names = [
            {
                    "name": "Addanki",
                    "id": 57593,
                    "state_id": 4017,
                    "state_code": "AP",
                    "state_name": "Andhra Pradesh",
                    "country_id": 101,
                    "country_code": "IN",
                    "country_name": "India",
                    "latitude": "15.81061000",
                    "longitude": "79.97338000",
                    "wikiDataId": "Q2350169"
            },

            {
                "name": "Adoni",
                "id": 134452,
                "state_id": 4017,
                "state_code": "AP",
                "state_name": "Andhra Pradesh",
                "country_id": 101,
                "country_code": "IN",
                "country_name": "India",
                "latitude": "15.62788000",
                "longitude": "77.27495000",
                "wikiDataId": "Q490906"
           },
            {
                "name": "Akasahebpet",
                "id": 57620,
                "state_id": 4017,
                "state_code": "AP",
                "state_name": "Andhra Pradesh",
                "country_id": 101,
                "country_code": "IN",
                "country_name": "India",
                "latitude": "17.50455000",
                "longitude": "82.56597000",
                "wikiDataId": "Q582949"
            },
            {
                "name": "Akividu",
                "id": 57623,
                "state_id": 4017,
                "state_code": "AP",
                "state_name": "Andhra Pradesh",
                "country_id": 101,
                "country_code": "IN",
                "country_name": "India",
                "latitude": "16.58225000",
                "longitude": "81.38112000",
                "wikiDataId": "Q416835"
            }
        ]
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
