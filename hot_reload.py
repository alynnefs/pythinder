from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp


class HotReload(MDApp):
    KV_FILES = ["app/pythinder.kv"]
    DEBUG = True

    def build_app(self):
        return Builder.load_file("app/pythinder.kv")


HotReload().run()
