from PIL import Image as PILImage
from kivy.graphics.svg import Gradient
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout

Window.size = (350, 600)


class ImageButton(Image, Button):
    image_source = StringProperty()


class StoryPage(MDFloatLayout):
    story_background = ObjectProperty(None)


class UserImage(Image):
    image_source = StringProperty()



class Stories(MDApp):

    current = 0
    user_list = {"1": "image_1.jpg", "2": "image_2.jpg", "3": "image_3.jpg", "4": "image_4.jpg", "5": "image_5.jpg", "6": "image_6.jpg"}

    def on_start(self):
        for i in self.user_list:
            self.root.get_screen("home_page").ids.grid.add_widget(ImageButton(image_source=f"{i}.jpg"))

    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file("home_page.kv"))
        screen_manager.add_widget(Builder.load_file("story_page.kv"))
        return screen_manager

    def story_background(self, image_color):
        im = PILImage.open(image_color)
        color = max(im.getcolors(im.size[0] * im.size[1]))[1]
        if (color[0] < 230) and (color[1] < 230) and (color[2] < 230):
            self.root.get_screen("story_page").ids.story.story_background = Gradient.vertical(
                (color[0]/255, color[1]/255, color[2]/255, 0.5),
                (color[0]/255, color[1]/255, color[2]/255, 1)
            )
            self.root.get_screen("story_page").ids.user_image.color = \
                (color[0] / 255, color[1] / 255, color[2] / 255, 1)

        else:
            self.root.get_screen("story_page").ids.story.story_background = Gradient.vertical(
                (230/255, 230/255, 230/255, 0.5),
                (230/255, 230/255, 230/255, 1)
            )
            self.root.get_screen("story_page").ids.user_image.color = \
                (230/255, 230/255, 230/255, 1)


    def show_stories(self, user):
        self.current = int(user.split(".")[0])
        self.story_background(user)
        self.root.get_screen("story_page").ids.story_image.source = user.image_source
        self.root.get_screen("story_page").ids.user_image.image_source = user.image_source
        self.root.get_screen("story_page").ids.user_id.text = self.user_list[str(self.current)]


    def previous_stories(self):
        self.current -= 1
        if self.current<= 0:
            self.current= len(self.user_list)
        self.root.get_screen("story_page").ids.story_image.source =f"{self.current}.jpg"
        self.root.get_screen("story_page").ids.user_image.image_source =f"{self.current}.jpg"
        self.root.get_screen("story_page").ids.user_id.text = self.user_list[str(self.current)]
        self.story_background(f"{self.current}.jpg")


    def next_stories(self):
        self.current += 1
        if self.current > len(self.user_list):
            self.current = 1
        self.root.get_screen("story_page").ids.story_image.source =f"{self.current}.jpg"
        self.root.get_screen("story_page").ids.user_image.image_source =f"{self.current}.jpg"
        self.root.get_screen("story_page").ids.user_id.text = self.user_list[str(self.current)]
        self.story_background(f"{self.current}.jpg")


if __name__ == '__main__':
    Stories().run()
