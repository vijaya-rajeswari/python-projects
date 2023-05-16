from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
import json

class CityGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CityGrid, self).__init__(**kwargs)
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
        city_name = self.city_input.text
        api_key = "X-CSCAPI-KEY"
        base_url = "https://api.countrystatecity.in/v1/countries/IN/states/MH/cities?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            city = data["name"]
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            result = f"City: {city}\nWeather: {weather}\nTemperature: {temp}\nHumidity: {humidity}\nWind Speed: {wind_speed}"
            self.result_label.text = result
        else:
            self.result_label.text = "City not found"

class CityApp(App):
    def build(self):
        return CityGrid()

if __name__ == "__main__":
    CityApp().run()
