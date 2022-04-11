from kivy.lang import Builder
from kivymd.app import MDApp


class Pythinder(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('pythinder.kv')

Pythinder().run()