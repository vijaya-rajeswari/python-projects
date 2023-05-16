# import tkinter as tk
# from PIL import Image, ImageTk
#
# class MainApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("My App")
#         # load the background image
#         self.bg_image = Image.open("1.png")
#         self.bg_image = self.bg_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()), Image.ANTIALIAS)
#         self.bg_image = ImageTk.PhotoImage(self.bg_image)
#         # create a label widget with the background image
#         self.bg_label = tk.Label(master, image=self.bg_image)
#         self.bg_label.place(relwidth=1, relheight=1)
#         # create a label widget and add it to the root widget
#         self.label = tk.Label(master, text="Hello, world!", font=("Helvetica", 20))
#         self.label.place(relx=0.5, rely=0.5, anchor="center")
#
# root = tk.Tk()
# app = MainApp(root)
# root.mainloop()



# import tkinter as tk
#
# class MainApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("My App")
#         # create a label widget and add it to the root widget
#         self.label = tk.Label(master, text="Hello, world!", font=("Helvetica", 20))
#         self.label.place(relx=0.5, rely=0.5, anchor="center")
#
# root = tk.Tk()
# app = MainApp(root)
# root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("My App")
        # load the transparent background image of the horse
        self.horse_image = Image.open("1.png")
        # create a PhotoImage object from the horse image
        self.horse_photo = ImageTk.PhotoImage(self.horse_image)
        # create a label widget with the horse image
        self.horse_label = tk.Label(master, image=self.horse_photo)
        self.horse_label.place(relx=0.5, rely=0.5, anchor="center")

root = tk.Tk()
app = MainApp(root)
root.mainloop()






























