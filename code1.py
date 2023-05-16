from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class familyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(familyGrid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Enter father name: "))
        self.father_input = TextInput()
        self.add_widget(self.father_input)

        self.search_button = Button(text="Search")
        self.search_button.bind(on_press=self.search)
        self.add_widget(self.search_button)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def search(self, instance):
        choice = self.father_input.text
        familynames = [
            {
                "father": "rangaswamy",
                "mother": "laxmidevi",
                "daughter-1": "raju",
                "daughter-2": "jeevana",
                "daughter-3": "nikhila",
                "son": "tirumalesh"
            },
            {
                "father": "sudhakar",
                "mother": "saroja",
                "son": "sriram",
                "daughter-1": "sridevi",
                "daughter-2": "usha"
            }
        ]
        found = False
        for family in familynames:
            if choice == family["father"]:
                result = ""
                for key, value in family.items():
                    result += f"{key}: {value}\n"
                self.result_label.text = result
                found = True
                break

        if not found:
            self.result_label.text = "Father name not found in family names"


class My_FamilyApp(App):
    def build(self):
        return familyGrid()


if __name__ == "__main__":
    My_FamilyApp().run()
