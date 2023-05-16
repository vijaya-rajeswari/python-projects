# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.graphics import Rectangle, Color
#
# class MyWidget(Widget):
#     pass
#
# class MyApp(App):
#     def build(self):
#         widget = MyWidget()
#         with widget.canvas.before:
#             # draw a solid color background
#             Color(1, 1, 1, 1)  # white
#             self.rect = Rectangle(size=widget.size, pos=widget.pos)
#         return widget
#
# if __name__ == '__main__':
#     MyApp().run()



# from rembg import remove
# from PIL import Image
# input_path = '2.jpg'
# output_path = 'output.png'
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)



# from kivymd.app import MDApp
# from kivy.uix.image import Image
#
# class MainApp(MDApp):
#     def build(self):
#         wimage = Image(source="1.png")
#         return wimage
#
# MainApp().run()

from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout

class MainApp(MDApp):
    def build(self):
        # create a BoxLayout as the root widget
        root = BoxLayout(orientation="vertical")
        # add the toolbar to the root widget
        toolbar = MDToolbar(title="My App", pos_hint={"top": 1})
        root.add_widget(toolbar)
        # add an Image widget as the background of the root widget
        bg_image = Image(source="1.png", allow_stretch=True, keep_ratio=False)
        root.add_widget(bg_image)
        # create a label and add it to the root widget
        label = MDLabel(text="Hello, world!", halign="center")
        root.add_widget(label)
        return root

MainApp().run()


























# import cv2
# import np as np
# import numpy as np
# from matplotlib import __pyplot as plt
# from numpy.array_api import astype
#
# image_bgr = cv2.imread('imgaes/input_1.jpg')
# image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
# rectangle = (0, 0, 300, 380)
#
# mask = np.zeros(image_rgb.shape[:2], np.unit8)
# bgdModel = np.zeros((1, 65), np.float64)
# fgdModel = np.zeros((1, 65), np.float64)
#
#
# cv2.grabCut(image_rgb, mask, rectangle, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
# mask_2 = np.where((mask == 2)) | (mask == 0), 0, 1).astype('unit8')
# image_rgd_nobg = image_rgb * mask_2 [:, :, np.newaxis]
#
# plt.imshow(image_rgb), plt.axis('off')
# plt.show()