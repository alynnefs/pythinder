from kivy.lang import Builder
from kivymd.app import MDApp


class Pythinder(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('app/pythinder.kv')

