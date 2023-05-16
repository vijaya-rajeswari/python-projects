from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView, MapMarker


class Mapviewexample(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.map = self.ids.map
        self.map.add_widget(MapMarker(lat = 24.0555,lon= 90.9802,source= "marker.png"))


    def return_home(self):
        self.map.center_on(24.055,90.980)

class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        return Mapviewexample()

Main().run()