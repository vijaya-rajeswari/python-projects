from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView, MapMarker


class Mapviewexample(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.map = self.ids.map
        self.map.add_widget(MapMarker(lat=15.8281, lon=78.0373, source='kurnool_marker.png'))

    def return_home(self):
        self.map.center_on(15.8281, 78.0373)


class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        return Mapviewexample()


Main().run()
